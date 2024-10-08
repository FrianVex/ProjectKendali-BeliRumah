# Imported UI Files
from FrontUIVer110 import Ui_MainWindow
from Account import Account
from PerhitunganKredit import HitungKredit
from Houses import Housing
from AkuAdalahAlgoritma import ElbowCanvas
import AppIcons_rc

# Needed Libraries
import time
import json
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Custom Matplotlib Widget
class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super(MatplotlibWidget, self).__init__(fig)
        self.setParent(parent)

# Popup Window for Matplotlib
class MatplotlibPopup(QDialog):
    def __init__(self, parent=None):
        super(MatplotlibPopup, self).__init__(parent)
        self.setWindowTitle("Matplotlib Sketch")
        self.setGeometry(100, 100, 800, 600)
        
        layout = QVBoxLayout(self)
        self.matplotlib_widget = MatplotlibWidget(self)
        layout.addWidget(self.matplotlib_widget)
        
        self.setLayout(layout)
        
    def plot_graph(self, graph):
        graph.PlottingGraph(self.matplotlib_widget.axes)
        self.matplotlib_widget.draw()

class MainWindow(QMainWindow, Ui_MainWindow):

    # Window Setup and Settings
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.accounts = Account()
        self.kredit = HitungKredit()
        self.yeah_houses = Housing()
        self.graph = ElbowCanvas()

        # Stored Flags
        self.is_login = False
        self.is_match = False
        self.is_this_button_clicked = False
        self.is_on_reset_password = False
        self.Price_Button = 0

        # Variables to store the position of the mouse
        self._is_dragging = False
        self._start_pos = None

        # Connect buttons to close, minimize, and maximize the program
        self.CloseButton.clicked.connect(self.close_program)
        self.Minimize.clicked.connect(self.minimize_program)
        self.Resize.clicked.connect(self.resize_program)

        # Connect buttons to switch pages
        self.Rumah.clicked.connect(self.list_rumah_page)
        self.Kredit.clicked.connect(self.kredit_page)
        self.Beli.clicked.connect(self.beli_page)
        self.Bantuan.clicked.connect(self.bantuan_page)
        self.Pengaturan.clicked.connect(self.pengaturan_page)
        self.User.clicked.connect(self.user_page)
        self.Notifcation.clicked.connect(self.notification_page)
        self.Preferences.clicked.connect(self.preferences_page)
        self.ProfileLoginButton.clicked.connect(self.login_page)
        self.ProfileRegisterButton.clicked.connect(self.register_page)
        
        # Navigation Buttons
        self.GoBackToHomeButton.clicked.connect(self.list_rumah_page)
        self.ProfilePageExitButton.clicked.connect(self.close_notification_page)
        self.NotificationsCloseContainerButton.clicked.connect(self.close_notification_page)
        self.SearchPreferencesCloseButton.clicked.connect(self.close_notification_page)

        # User Account
        self.LoginButton.clicked.connect(self.process_login)
        self.GoResetPasswordButton.clicked.connect(self.setup_reset_password_email)
        self.BuatAkunButton.clicked.connect(self.process_account_creation)
        self.SimpanDataButton.clicked.connect(self.process_account_data)
        self.ProcessResetPassword.clicked.connect(self.process_reset_password_email)
        self.DashboardEditDataButton.clicked.connect(self.logout_data)

        # Kredit
        self.BungaTetapcheckBox.setChecked(True)
        self.BungaTetapcheckBox.stateChanged.connect(self.set_page_fixed_rate)
        self.BungaBerjenjangcheckBox.stateChanged.connect(self.set_page_layered_rate)
        self.PerhitunganKPRCalculateButton.clicked.connect(self.process_kredit_calculations)

        # Housing
        self.Price_1.clicked.connect(self.price_1_clicked)
        self.Price_2.clicked.connect(self.price_2_clicked)
        self.Price_3.clicked.connect(self.price_3_clicked)
        self.Price_4.clicked.connect(self.price_4_clicked)

        # Graphing
        self.MatplotlibSketch.clicked.connect(self.show_matplotlib_popup)

        # Set up the First Condition to Boot up the Program
        self.ContentFrame.setCurrentIndex(0)
        self.NotificatioFrame.hide()
        self.read_random_houses()

# Program Panel Functions______________________________________________________________________________________________________________________
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._is_dragging = True
            self._start_pos = event.pos()

    def mouseMoveEvent(self, event):
        if self._is_dragging:
            self.move(self.pos() + event.pos() - self._start_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._is_dragging = False

    def contextMenuEvent(self, event):

        menu = QMenu(self)
        restore_action = menu.addAction("Restore")
        # restore_action.setIcon(QIcon(":/feather/copy.svg"))
        move_action = menu.addAction("Move")
        size_action = menu.addAction("Size")
        minimize_action = menu.addAction("Minimize")
        # minimize_action.setIcon(QIcon(":/feather/minus.svg"))
        maximize_action = menu.addAction("Maximize")
        # maximize_action.setIcon(QIcon(":/feather/square.svg"))
        close_action = menu.addAction("Close Program")
        # close_action.setIcon(QIcon(":/feather/x.svg"))
        # Icons broke idk why

        action = menu.exec_(self.mapToGlobal(event.pos()))
                
        if action == restore_action:
            self.showNormal()
        elif action == move_action:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.show()
        elif action == size_action:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.showMaximized()
        elif action == minimize_action:
            self.minimize_program()
        elif action == maximize_action:
            self.resize_program()
        elif action == close_action:
            self.close()

    def close_program(self):
        self.close()
    
    def minimize_program(self):
        self.animate_window(QRect(self.x(), self.y(), self.width(), self.height()), QRect(self.x(), self.y(), self.width(), 0))
        self.showMinimized()

    def resize_program(self):
        if self.isMaximized():
            self.animate_window(QRect(self.x(), self.y(), self.width(), self.height()), QRect(self.x(), self.y(), 800, 600))
            self.showNormal()
        else:
            self.animate_window(QRect(self.x(), self.y(), self.width(), self.height()), QRect(self.x(), self.y(), self.screen().size().width(), self.screen().size().height()))
            self.showMaximized()

    def animate_window(self, start_rect, end_rect):
        animation = QPropertyAnimation(self, b"geometry")
        animation.setDuration(500)  # Duration in milliseconds
        animation.setStartValue(start_rect)
        animation.setEndValue(end_rect)
        animation.start()

# Page Switching Functions______________________________________________________________________________________________________________________
    def beli_page(self):
        self.ContentFrame.setCurrentIndex(4)

    def bantuan_page(self):
        self.ContentFrame.setCurrentIndex(5)

    def pengaturan_page(self):
        self.ContentFrame.setCurrentIndex(6)

    def user_page(self):
        if self.NotificatioFrame.isVisible():
            self.NotificatioFrame.hide()
        else:
            self.NotificatioFrame.show()

        if self.is_login == False:
            self.ProfilePagePhotoContainer.hide()
            self.DashboardControlContainer.hide()
            self.ProfilePageLoginContainer.show()
        else:
            username = self.accounts.read_credentials()
            self.ProfilePagePhoto.setText("Selamat Datang " + username + "!")

            self.ProfilePagePhotoContainer.show()
            self.DashboardControlContainer.show()
            self.ProfilePageLoginContainer.hide()

        self.NotificatioFrame.setCurrentIndex(0)

    def notification_page(self):
        if self.NotificatioFrame.isVisible():
            self.NotificatioFrame.hide()
        else:
            self.NotificatioFrame.show()
        self.NotificatioFrame.setCurrentIndex(1)

    def preferences_page(self):
        if self.NotificatioFrame.isVisible():
            self.NotificatioFrame.hide()
        else:
            self.NotificatioFrame.show()
        self.NotificatioFrame.setCurrentIndex(2)    

    def close_notification_page(self):
        self.NotificatioFrame.hide()

    

# Account Functions______________________________________________________________________________________________________________________
    
    # Handles Login
    def login_page(self):
        self.ResetPasswordContainer.hide()
        self.LoginLabelStatus.hide()
        self.NotificatioFrame.hide()
        self.ContentFrame.setCurrentIndex(1)

    def process_login(self):
        parse_username = self.UsernameBox.toPlainText()
        parse_password = self.PasswordBox.toPlainText()
        self.is_login = self.accounts.user_login(parse_username, parse_password)
        
        if self.is_login == True:
            self.LoginLabelStatus.show()
            self.LoginLabelStatus.setText("Selamat Datang!")
            time.sleep(2)
            self.ContentFrame.setCurrentIndex(0)
            self.ProfilePageLoginContainer.hide()
            self.UsernameBox.clear()
            self.PasswordBox.clear()
        else:
            self.LoginLabelStatus.show()
            time.sleep(2)
            self.LoginLabelStatus.setText("Username atau Password Salah!")
            self.PasswordBox.clear()

    # Handles Logout
    def logout_data(self):
        self.is_login = False # Ain't that so shrimple?
        self.ProfilePageLoginContainer.show()
        self.ProfilePagePhotoContainer.hide()
        self.DashboardControlContainer.hide()
        self.ContentFrame.setCurrentIndex(0)

    # Offended Register
    def register_page(self):
        self.RegisterFlag.hide()
        self.NotificatioFrame.hide()
        self.ContentFrame.setCurrentIndex(2)
        self.KolomData.hide()

    def register_data_page(self):
        self.SavedFlag.hide()
        self.KolomAkun.hide()
        self.KolomData.show()

    def process_account_creation(self):
        # I'm Sorry there is no other way to do this
        if self.is_this_button_clicked == False: # This If Statement Handles the Creation of Account
            parse_username = self.BuatUserBox.toPlainText()
            parse_password = self.BuatPasswordBox.toPlainText()
            parse_repassword = self.RePassBox.toPlainText()
            self.is_match = self.accounts.create_account_username_password(parse_username, parse_password, parse_repassword)

            if self.is_match == True:
                self.RegisterFlag.show()
                self.RegisterFlag.setText("Selamat Akun Anda Telah Dibuat!")
                time.sleep(2)
                self.register_data_page()
                self.is_match = False
            else:
                self.RegisterFlag.show()
                self.RegisterFlag.setText("Password Tidak Cocok!")
                time.sleep(2)
                self.RegisterFlag.setText("Silahkan Coba Lagi!")
        
        else:   # This If Statement Handles the Changing of Password
            parse_password = self.BuatPasswordBox.toPlainText()
            parse_repassword = self.RePassBox.toPlainText()
            self.is_match = self.accounts.reset_user_password(parse_password, parse_repassword)

            if self.is_match == True:
                self.RegisterFlag.show()
                self.RegisterFlag.setText("Password Telah Diubah!")
                time.sleep(2)
                self.RegisterFlag.setText("Silahkan Login!")
                self.ContentFrame.setCurrentIndex(1)
                self.is_match = False
            else:
                self.RegisterFlag.show()
                self.RegisterFlag.setText("Password Tidak Cocok!")
                time.sleep(2)
                self.RegisterFlag.setText("Silahkan Coba Lagi!")
    
    def process_account_data(self): # Shrimple Applying Data to the json file
        parse_nama = self.NamaBox.toPlainText()
        parse_pekerjaan = self.PekerjaanBox.toPlainText()
        parse_email = self.AlamatEmailBox.toPlainText()
        parse_gaji = self.GajiBox.toPlainText()
        parse_tempat_kerja = self.TempatKerjaBox.toPlainText()
        parse_tanggungan = self.TanggunganBox.toPlainText()
        parse_cicilan = self.CicilanBox.toPlainText()
        parse_tabungan = self.TabunganBox.toPlainText()
        self.accounts.create_account_data(parse_nama, parse_pekerjaan, parse_email, parse_gaji, parse_tempat_kerja, parse_tanggungan, parse_cicilan, parse_tabungan)
        time.sleep(2)
        self.SavedFlag.show()
        self.SavedFlag.setText("Data Anda Telah Tersimpan!")
        time.sleep(2)
        self.is_login = True
        self.ContentFrame.setCurrentIndex(0)

    # Reset Balls I mean Password
    def setup_reset_password_email(self): # Set up the Login Page as Reset Password Page
        self.ResetFlagStatus.hide()
        self.UsernameContainer.hide()
        self.PasswordContainer.hide()
        self.LoginButtonContainer.hide()
        self.ResetPasswordContainer.show()
        self.ResetFlagStatus.hide()
        self.ContentFrame.setCurrentIndex(1)

    def process_reset_password_email(self): # Process the Email Searching
        parse_email = self.EmailBox.toPlainText()
        self.is_on_reset_password = self.accounts.search_user_email(parse_email)

        if self.is_on_reset_password == True:
            self.setup_reset_password()
            self.is_on_reset_password = False
        else:
            self.ResetFlagStatus.show()
            self.ResetFlagStatus.setText("Email Tidak Terdaftar!")
            time.sleep(2)
            self.ResetFlagStatus.setText("Silahkan Coba Lagi!")
    
    def setup_reset_password(self): # Set up the Input New Password Page
        self.KolomData.hide()
        self.RegisterFlag.hide()
        self.BuatUserContainer.hide()
        self.BuatPasswordBox.clear()
        self.RePassBox.clear()
        self.BuatAkunLabel.setText("Reset Password")
        self.BuatAkunButton.setText("Tetapkan Password Baru")
        self.ContentFrame.setCurrentIndex(2)

# Kredit Functions______________________________________________________________________________________________________________________
    
    # We Go calc some Credits
    def kredit_page(self):
        self.ContentFrame.setCurrentIndex(3)
        self.OutputPerhitunganPageContainer.hide()

    def set_page_fixed_rate(self):
        if self.BungaTetapcheckBox.isChecked() == True:
            self.BungaBerjenjangcheckBox.setChecked(False)
            self.TipeTipeBunga.setCurrentIndex(0)

    def set_page_layered_rate(self):
        if self.BungaBerjenjangcheckBox.isChecked() == True:
            self.BungaTetapcheckBox.setChecked(False)
            self.TipeTipeBunga.setCurrentIndex(1)

    # Math Scary
    def process_kredit_calculations(self):
        parse_property_value = self.PerhitunganKPRUangMukaTextEdit.toPlainText()
        parse_down_payment = self.PerhitunganKPRHargaPropertiTextEdit.toPlainText()

        if self.BungaTetapcheckBox.isChecked() == True:
            parse_intereset_rate = self.PerhitunganKPRMasaKreditLabelTextEdit.toPlainText()
            parse_fixed_rate_tenor = self.PerhitunganKPRJangkaWaktuKreditTextEdit.toPlainText()
            parse_maximum_payment_time = self.PerhitunganKPRPersentaseSukuBungaLabelTextEdit.toPlainText()

            parsed_data = self.kredit.fixed_rate(float(parse_property_value), float(parse_down_payment), float(parse_intereset_rate), float(parse_fixed_rate_tenor), float(parse_maximum_payment_time))

            self.OutputPerhitunganPageContainer.show()
            self.PenulisanHargaJangkaTahunPertamaLabel.setText("Rp. " + str(parsed_data[2]))
            self.PenulisanHargaJangkaTahunSetelahLabel.setText("Rp. " + str(parsed_data[3]))
            self.PenulisanHargaEstimasiJumlahBayarLabel.setText("Rp. " + str(parsed_data[4]))
            self.PenulisanHargaUangMukaLabel.setText("Rp. " + str(parse_down_payment))
            self.PenulisanHargaAngsuranPertamaLabel.setText("Rp. " + str(parsed_data[2]))
            self.PenulisanHargaEstimasiPembayaranLabel.setText("Rp. " + str(parsed_data[1]))
            self.PenulisanHargaDetailPinjamanLabel.setText("Rp. " + str(parsed_data[5]))
            self.PenulisanHargaPinjamanPokokLabel.setText("Rp. " + str(parsed_data[0]))
            self.PenulisanHargaEstimasiBungaPinjamanLabel.setText("Rp. " + str(parsed_data[6]))
        
        elif self.BungaBerjenjangcheckBox.isChecked() == True:
            parse_numbers_of_layers = self.spinBox.value()
            parse_first_interest_rate = self.PerhitunganKPRPersentaseLamaKreditBerjenjangBox.toPlainText()
            parse_increment_interest_rate = self.EskalasiBungaBox.toPlainText()
            parse_layered_rate_tenor = self.PerhitunganKPRJangkaWaktuMasaKreditBerjenjang.toPlainText()

            parsed_data = self.kredit.floating_rate(float(parse_property_value), float(parse_down_payment), float(parse_numbers_of_layers), float(parse_first_interest_rate), float(parse_increment_interest_rate), float(parse_layered_rate_tenor))
            yearly_payment = parsed_data[2]

            self.OutputPerhitunganPageContainer.show()
            self.HargaJangkaTahunPertamaLabel.setText("Harga Jangka Tahun Pertama dan Setelahnya")
            self.PenulisanHargaJangkaTahunPertamaLabel.setText("Rp. " + str(parsed_data[2]))
            self.PenulisanHargaJangkaTahunSetelahLabel.setText("Rp. " + str(parsed_data[3]))
            self.PenulisanHargaEstimasiJumlahBayarLabel.setText("Rp. " + str(parsed_data[4]))
            self.PenulisanHargaUangMukaLabel.setText("Rp. " + str(parse_down_payment))
            self.PenulisanHargaAngsuranPertamaLabel.setText("Rp. " + str(yearly_payment[0]))
            self.PenulisanHargaEstimasiPembayaranLabel.setText("Rp. " + str(parsed_data[1]))
            self.PenulisanHargaDetailPinjamanLabel.setText("Rp. " + str(parsed_data[5]))
            self.PenulisanHargaPinjamanPokokLabel.setText("Rp. " + str(parsed_data[0]))
            self.PenulisanHargaEstimasiBungaPinjamanLabel.setText("Rp. " + str(parsed_data[6]))
            
# Housing Display Functions______________________________________________________________________________________________________________________

    def list_rumah_page(self):
        self.ContentFrame.setCurrentIndex(0)

    def price_1_clicked(self):
        self.Price_Button = 1
        self.displaying_house_context()

    def price_2_clicked(self):
        self.Price_Button = 2
        self.displaying_house_context()

    def price_3_clicked(self):
        self.Price_Button = 3
        self.displaying_house_context()

    def price_4_clicked(self):
        self.Price_Button = 4
        self.displaying_house_context()

    def displaying_house_context(self):
        if self.Price_Button == 1:
            self.ContentFrame.setCurrentIndex(7)
            exported_data = self.yeah_houses.get_houses(self.house_data_entry_1[3])

            for _ in exported_data:
                title = exported_data[1]
                price = exported_data[0]
                img_source = exported_data[3]
                address = exported_data[2]
                landsize = exported_data[4]
                building_size = exported_data[5]
                certificate = exported_data[6]
                electricity = exported_data[7]
                # property_condition = exported_data[8]
                floors = exported_data[8]
                garages = exported_data[9]
                bedrooms = exported_data[10]
                bathrooms = exported_data[11]
                facilities = exported_data[12]

                # Do something with the elements

            self.JudulRumah.setText(f"{title}\n\n{price}")
            self.FotoRumahLabel.load(QUrl(img_source))
            self.AlamatRumah.setText(address)
            self.DeskripsiRumah.setText(f"Ukuran Tanah: {landsize}\nLuas Bangunan: {building_size}\nSertifikat: {certificate}\nBeban Listrik: {electricity}\nLantai: {floors}")
            self.IsiRumah.setText(f"Garages: {garages}\nBedrooms: {bedrooms}\nBathrooms: {bathrooms}\nFacilities: {facilities}")

        elif self.Price_Button == 2:
            self.ContentFrame.setCurrentIndex(7)
            exported_data = self.yeah_houses.get_houses(self.house_data_entry_2[3])

            for _ in exported_data:
                title = exported_data[1]
                price = exported_data[0]
                img_source = exported_data[3]
                address = exported_data[2]
                landsize = exported_data[4]
                building_size = exported_data[5]
                certificate = exported_data[6]
                electricity = exported_data[7]
                # property_condition = exported_data[8]
                floors = exported_data[8]
                garages = exported_data[9]
                bedrooms = exported_data[10]
                bathrooms = exported_data[11]
                facilities = exported_data[12]

                # Do something with the elements

            self.JudulRumah.setText(f"{title}\n\n{price}")
            self.FotoRumahLabel.load(QUrl(img_source))
            self.AlamatRumah.setText(address)
            self.DeskripsiRumah.setText(f"Ukuran Tanah: {landsize}\nLuas Bangunan: {building_size}\nSertifikat: {certificate}\nBeban Listrik: {electricity}\nLantai: {floors}")
            self.IsiRumah.setText(f"Garages: {garages}\nBedrooms: {bedrooms}\nBathrooms: {bathrooms}\nFacilities: {facilities}")

        elif self.Price_Button == 3:
            self.ContentFrame.setCurrentIndex(7)
            exported_data = self.yeah_houses.get_houses(self.house_data_entry_3[3])
            
            for _ in exported_data:
                title = exported_data[1]
                price = exported_data[0]
                img_source = exported_data[3]
                address = exported_data[2]
                landsize = exported_data[4]
                building_size = exported_data[5]
                certificate = exported_data[6]
                electricity = exported_data[7]
                # property_condition = exported_data[8]
                floors = exported_data[8]
                garages = exported_data[9]
                bedrooms = exported_data[10]
                bathrooms = exported_data[11]
                facilities = exported_data[12]

                # Do something with the elements

            self.JudulRumah.setText(f"{title}\n\n{price}")
            self.FotoRumahLabel.load(QUrl(img_source))
            self.AlamatRumah.setText(address)
            self.DeskripsiRumah.setText(f"Ukuran Tanah: {landsize}\nLuas Bangunan: {building_size}\nSertifikat: {certificate}\nBeban Listrik: {electricity}\nLantai: {floors}")
            self.IsiRumah.setText(f"Garages: {garages}\nBedrooms: {bedrooms}\nBathrooms: {bathrooms}\nFacilities: {facilities}")

        elif self.Price_Button == 4:
            self.ContentFrame.setCurrentIndex(7)
            exported_data = self.yeah_houses.get_houses(self.house_data_entry_4[3])     

            for _ in exported_data:
                title = exported_data[1]
                price = exported_data[0]
                img_source = exported_data[3]
                address = exported_data[2]
                landsize = exported_data[4]
                building_size = exported_data[5]
                certificate = exported_data[6]
                electricity = exported_data[7]
                # property_condition = exported_data[8]
                floors = exported_data[8]
                garages = exported_data[9]
                bedrooms = exported_data[10]
                bathrooms = exported_data[11]
                facilities = exported_data[12]

                # Do something with the elements

            self.JudulRumah.setText(f"{title}\n\n{price}")
            self.FotoRumahLabel.load(QUrl(img_source))
            self.AlamatRumah.setText(address)
            self.DeskripsiRumah.setText(f"Ukuran Tanah: {landsize}\nLuas Bangunan: {building_size}\nSertifikat: {certificate}\nBeban Listrik: {electricity}\nLantai: {floors}")
            self.IsiRumah.setText(f"Garages: {garages}\nBedrooms: {bedrooms}\nBathrooms: {bathrooms}\nFacilities: {facilities}")


    def read_random_houses(self):
        for i in range(4):
            house_data = self.yeah_houses.read_random_houses()
            if i == 0:
                self.house_data_entry_1 = house_data
                self.Img_1.load(QUrl(self.house_data_entry_1[0]))
                self.Desc_1.setText(self.house_data_entry_1[1])
                self.Desc_1.setWordWrap(True)
                self.Price_1.setText(f"{self.house_data_entry_1[2]}\n\nLihat ini!")
            elif i == 1:
                self.house_data_entry_2 = house_data
                self.Img_2.load(QUrl(self.house_data_entry_2[0]))
                self.Desc_2.setText(self.house_data_entry_2[1])
                self.Desc_2.setWordWrap(True)
                self.Price_2.setText(f"{self.house_data_entry_2[2]}\n\nLihat ini!")
            elif i == 2:
                self.house_data_entry_3 = house_data
                self.Img_3.load(QUrl(self.house_data_entry_3[0]))
                self.Desc_3.setText(self.house_data_entry_3[1])
                self.Desc_3.setWordWrap(True)
                self.Price_3.setText(f"{self.house_data_entry_3[2]}\n\nLihat ini!")
            elif i == 3:
                self.house_data_entry_4 = house_data
                self.Img_4.load(QUrl(self.house_data_entry_4[0]))
                self.Desc_4.setText(self.house_data_entry_4[1])
                self.Desc_4.setWordWrap(True)
                self.Price_4.setText(f"{self.house_data_entry_4[2]}\n\nLihat ini!")

    def refresh_houses(self):
        self.read_random_houses()

# Algorithms Functions______________________________________________________________________________________________________________________

    # Setelah install sklearn dan seaborn, satu environment rusak installasi PySide2 nya. Too Bad - Raffly
    # Plotting Graphs
    def show_matplotlib_popup(self):
        self.popup = MatplotlibPopup(self)
        self.popup.plot_graph(self.graph)
        self.popup.exec_()

    # KMeans Clustering
    def kmeans_clustering(self):
        self.graph.KCluster()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())