# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrontUIVer1wbjkIS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from PySide2.QtWebEngineWidgets import QWebEngineView


import AppIcons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1208, 885)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"*{\n"
"	border: yes;\n"
"	background-color: #000;\n"
"	background: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #000;\n"
"}\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 3px 5px;\n"
"}")
        self.Central = QWidget(MainWindow)
        self.Central.setObjectName(u"Central")
        self.Central.setAutoFillBackground(False)
        self.gridLayout_7 = QGridLayout(self.Central)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.SubProgramWidget = QWidget(self.Central)
        self.SubProgramWidget.setObjectName(u"SubProgramWidget")
        self.verticalLayout = QVBoxLayout(self.SubProgramWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ProgramPanelContainer = QWidget(self.SubProgramWidget)
        self.ProgramPanelContainer.setObjectName(u"ProgramPanelContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.ProgramPanelContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Logo = QFrame(self.ProgramPanelContainer)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setFrameShape(QFrame.StyledPanel)
        self.Logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Logo)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LogoLabel = QLabel(self.Logo)
        self.LogoLabel.setObjectName(u"LogoLabel")
        self.LogoLabel.setPixmap(QPixmap(u":/FeatherIcons/feather/home.svg"))

        self.horizontalLayout_5.addWidget(self.LogoLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.horizontalLayout_4.addWidget(self.Logo)

        self.MinimizeContainer = QFrame(self.ProgramPanelContainer)
        self.MinimizeContainer.setObjectName(u"MinimizeContainer")
        self.MinimizeContainer.setFrameShape(QFrame.StyledPanel)
        self.MinimizeContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.MinimizeContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Minimize = QPushButton(self.MinimizeContainer)
        self.Minimize.setObjectName(u"Minimize")
        icon = QIcon()
        icon.addFile(u":/FeatherIcons/feather/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Minimize.setIcon(icon)
        self.Minimize.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.Minimize, 0, Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.MinimizeContainer, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.ResizeContainer = QFrame(self.ProgramPanelContainer)
        self.ResizeContainer.setObjectName(u"ResizeContainer")
        self.ResizeContainer.setFrameShape(QFrame.StyledPanel)
        self.ResizeContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.ResizeContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Resize = QPushButton(self.ResizeContainer)
        self.Resize.setObjectName(u"Resize")
        icon1 = QIcon()
        icon1.addFile(u":/FeatherIcons/feather/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Resize.setIcon(icon1)
        self.Resize.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.Resize)


        self.horizontalLayout_4.addWidget(self.ResizeContainer, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.CloseButtonContainer = QFrame(self.ProgramPanelContainer)
        self.CloseButtonContainer.setObjectName(u"CloseButtonContainer")
        self.CloseButtonContainer.setFrameShape(QFrame.StyledPanel)
        self.CloseButtonContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.CloseButtonContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CloseButton = QPushButton(self.CloseButtonContainer)
        self.CloseButton.setObjectName(u"CloseButton")
        icon2 = QIcon()
        icon2.addFile(u":/FeatherIcons/feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseButton.setIcon(icon2)
        self.CloseButton.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.CloseButton)


        self.horizontalLayout_4.addWidget(self.CloseButtonContainer, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout.addWidget(self.ProgramPanelContainer)

        self.UserControlPanelContainer = QWidget(self.SubProgramWidget)
        self.UserControlPanelContainer.setObjectName(u"UserControlPanelContainer")
        self.horizontalLayout_6 = QHBoxLayout(self.UserControlPanelContainer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 9, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.RumahContainer = QFrame(self.UserControlPanelContainer)
        self.RumahContainer.setObjectName(u"RumahContainer")
        self.RumahContainer.setFrameShape(QFrame.StyledPanel)
        self.RumahContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.RumahContainer)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.Rumah = QPushButton(self.RumahContainer)
        self.Rumah.setObjectName(u"Rumah")
        icon3 = QIcon()
        icon3.addFile(u":/FeatherIcons/feather/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Rumah.setIcon(icon3)
        self.Rumah.setIconSize(QSize(24, 24))
        self.Rumah.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.Rumah)


        self.horizontalLayout_6.addWidget(self.RumahContainer)

        self.KreditContainer = QFrame(self.UserControlPanelContainer)
        self.KreditContainer.setObjectName(u"KreditContainer")
        self.KreditContainer.setFrameShape(QFrame.StyledPanel)
        self.KreditContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.KreditContainer)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Kredit = QPushButton(self.KreditContainer)
        self.Kredit.setObjectName(u"Kredit")
        icon4 = QIcon()
        icon4.addFile(u":/FeatherIcons/feather/percent.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Kredit.setIcon(icon4)
        self.Kredit.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.Kredit)


        self.horizontalLayout_6.addWidget(self.KreditContainer)

        self.Pembelian = QFrame(self.UserControlPanelContainer)
        self.Pembelian.setObjectName(u"Pembelian")
        self.Pembelian.setFrameShape(QFrame.StyledPanel)
        self.Pembelian.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.Pembelian)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Beli = QPushButton(self.Pembelian)
        self.Beli.setObjectName(u"Beli")
        icon5 = QIcon()
        icon5.addFile(u":/FeatherIcons/feather/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Beli.setIcon(icon5)
        self.Beli.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.Beli)


        self.horizontalLayout_6.addWidget(self.Pembelian)

        self.BantuanContainer = QFrame(self.UserControlPanelContainer)
        self.BantuanContainer.setObjectName(u"BantuanContainer")
        self.BantuanContainer.setFrameShape(QFrame.StyledPanel)
        self.BantuanContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.BantuanContainer)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Bantuan = QPushButton(self.BantuanContainer)
        self.Bantuan.setObjectName(u"Bantuan")
        icon6 = QIcon()
        icon6.addFile(u":/FeatherIcons/feather/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Bantuan.setIcon(icon6)
        self.Bantuan.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.Bantuan)


        self.horizontalLayout_6.addWidget(self.BantuanContainer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.PreferencesContainer = QFrame(self.UserControlPanelContainer)
        self.PreferencesContainer.setObjectName(u"PreferencesContainer")
        self.PreferencesContainer.setFrameShape(QFrame.StyledPanel)
        self.PreferencesContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.PreferencesContainer)
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.Preferences = QPushButton(self.PreferencesContainer)
        self.Preferences.setObjectName(u"Preferences")
        icon7 = QIcon()
        icon7.addFile(u":/FeatherIcons/feather/sliders.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Preferences.setIcon(icon7)
        self.Preferences.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.Preferences)


        self.horizontalLayout_6.addWidget(self.PreferencesContainer)

        self.NotifcationContainer = QFrame(self.UserControlPanelContainer)
        self.NotifcationContainer.setObjectName(u"NotifcationContainer")
        self.NotifcationContainer.setFrameShape(QFrame.StyledPanel)
        self.NotifcationContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.NotifcationContainer)
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.Notifcation = QPushButton(self.NotifcationContainer)
        self.Notifcation.setObjectName(u"Notifcation")
        icon8 = QIcon()
        icon8.addFile(u":/FeatherIcons/feather/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Notifcation.setIcon(icon8)
        self.Notifcation.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.Notifcation)


        self.horizontalLayout_6.addWidget(self.NotifcationContainer)

        self.UserContainer = QFrame(self.UserControlPanelContainer)
        self.UserContainer.setObjectName(u"UserContainer")
        self.UserContainer.setFrameShape(QFrame.StyledPanel)
        self.UserContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.UserContainer)
        self.horizontalLayout_7.setSpacing(7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.User = QPushButton(self.UserContainer)
        self.User.setObjectName(u"User")
        icon9 = QIcon()
        icon9.addFile(u":/FeatherIcons/feather/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.User.setIcon(icon9)
        self.User.setIconSize(QSize(24, 24))
        self.User.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.User)


        self.horizontalLayout_6.addWidget(self.UserContainer)

        self.PengaturanContainer = QFrame(self.UserControlPanelContainer)
        self.PengaturanContainer.setObjectName(u"PengaturanContainer")
        self.PengaturanContainer.setFrameShape(QFrame.StyledPanel)
        self.PengaturanContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.PengaturanContainer)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.Pengaturan = QPushButton(self.PengaturanContainer)
        self.Pengaturan.setObjectName(u"Pengaturan")
        icon10 = QIcon()
        icon10.addFile(u":/FeatherIcons/feather/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Pengaturan.setIcon(icon10)
        self.Pengaturan.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.Pengaturan)


        self.horizontalLayout_6.addWidget(self.PengaturanContainer)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.UserControlPanelContainer)

        self.ContentWindow = QWidget(self.SubProgramWidget)
        self.ContentWindow.setObjectName(u"ContentWindow")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContentWindow.sizePolicy().hasHeightForWidth())
        self.ContentWindow.setSizePolicy(sizePolicy)
        self.ContentWindow.setAutoFillBackground(False)
        self.horizontalLayout_11 = QHBoxLayout(self.ContentWindow)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.ContentFrame = QStackedWidget(self.ContentWindow)
        self.ContentFrame.setObjectName(u"ContentFrame")
        self.ContentPage = QWidget()
        self.ContentPage.setObjectName(u"ContentPage")
        self.verticalLayout_4 = QVBoxLayout(self.ContentPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.ContentPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.ScrollAreaContentSubContainer = QWidget()
        self.ScrollAreaContentSubContainer.setObjectName(u"ScrollAreaContentSubContainer")
        self.ScrollAreaContentSubContainer.setGeometry(QRect(0, 0, 700, 758))
        self.gridLayout_9 = QGridLayout(self.ScrollAreaContentSubContainer)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.Content4 = QFrame(self.ScrollAreaContentSubContainer)
        self.Content4.setObjectName(u"Content4")
        self.Content4.setFrameShape(QFrame.StyledPanel)
        self.Content4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.Content4)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.Img_4 = QWebEngineView(self.Content4)
        self.Img_4.setObjectName(u"Img_4")
        self.Img_4.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_18.addWidget(self.Img_4)

        self.Desc_4 = QLabel(self.Content4)
        self.Desc_4.setObjectName(u"Desc_4")

        self.horizontalLayout_18.addWidget(self.Desc_4)

        self.Price_4 = QPushButton(self.Content4)
        self.Price_4.setObjectName(u"Price_4")

        self.horizontalLayout_18.addWidget(self.Price_4)


        self.gridLayout_9.addWidget(self.Content4, 0, 0, 1, 1)

        self.Content3 = QFrame(self.ScrollAreaContentSubContainer)
        self.Content3.setObjectName(u"Content3")
        self.Content3.setFrameShape(QFrame.StyledPanel)
        self.Content3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.Content3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.Img_3 = QWebEngineView(self.Content3)
        self.Img_3.setObjectName(u"Img_3")
        self.Img_3.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_19.addWidget(self.Img_3)

        self.Desc_3 = QLabel(self.Content3)
        self.Desc_3.setObjectName(u"Desc_3")

        self.horizontalLayout_19.addWidget(self.Desc_3)

        self.Price_3 = QPushButton(self.Content3)
        self.Price_3.setObjectName(u"Price_3")

        self.horizontalLayout_19.addWidget(self.Price_3)


        self.gridLayout_9.addWidget(self.Content3, 1, 0, 1, 1)

        self.Content2 = QFrame(self.ScrollAreaContentSubContainer)
        self.Content2.setObjectName(u"Content2")
        self.Content2.setFrameShape(QFrame.StyledPanel)
        self.Content2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.Content2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.Img_2 = QWebEngineView(self.Content2)
        self.Img_2.setObjectName(u"Img_2")
        self.Img_2.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_20.addWidget(self.Img_2)

        self.Desc_2 = QLabel(self.Content2)
        self.Desc_2.setObjectName(u"Desc_2")

        self.horizontalLayout_20.addWidget(self.Desc_2)

        self.Price_2 = QPushButton(self.Content2)
        self.Price_2.setObjectName(u"Price_2")

        self.horizontalLayout_20.addWidget(self.Price_2)


        self.gridLayout_9.addWidget(self.Content2, 2, 0, 1, 1)

        self.Content1 = QFrame(self.ScrollAreaContentSubContainer)
        self.Content1.setObjectName(u"Content1")
        self.Content1.setFrameShape(QFrame.StyledPanel)
        self.Content1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.Content1)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.Img_1 = QWebEngineView(self.Content1)
        self.Img_1.setObjectName(u"Img_1")
        self.Img_1.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_21.addWidget(self.Img_1)

        self.Desc_1 = QLabel(self.Content1)
        self.Desc_1.setObjectName(u"Desc_1")

        self.horizontalLayout_21.addWidget(self.Desc_1)

        self.Price_1 = QPushButton(self.Content1)
        self.Price_1.setObjectName(u"Price_1")

        self.horizontalLayout_21.addWidget(self.Price_1)


        self.gridLayout_9.addWidget(self.Content1, 3, 0, 1, 1)

        self.HomeNavigateContainer = QWidget(self.ScrollAreaContentSubContainer)
        self.HomeNavigateContainer.setObjectName(u"HomeNavigateContainer")
        self.horizontalLayout_17 = QHBoxLayout(self.HomeNavigateContainer)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.PreviousButton = QPushButton(self.HomeNavigateContainer)
        self.PreviousButton.setObjectName(u"PreviousButton")

        self.horizontalLayout_17.addWidget(self.PreviousButton, 0, Qt.AlignLeft)

        self.KClusterButton = QPushButton(self.HomeNavigateContainer)
        self.KClusterButton.setObjectName(u"KClusterButton")

        self.horizontalLayout_17.addWidget(self.KClusterButton)

        self.NextButton = QPushButton(self.HomeNavigateContainer)
        self.NextButton.setObjectName(u"NextButton")

        self.horizontalLayout_17.addWidget(self.NextButton, 0, Qt.AlignRight)


        self.gridLayout_9.addWidget(self.HomeNavigateContainer, 4, 0, 1, 1, Qt.AlignBottom)

        self.scrollArea.setWidget(self.ScrollAreaContentSubContainer)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.ContentFrame.addWidget(self.ContentPage)
        self.LoginPage = QWidget()
        self.LoginPage.setObjectName(u"LoginPage")
        self.gridLayout_8 = QGridLayout(self.LoginPage)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(9, 0, 9, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 3, 0, 1, 1)

        self.LoginTextContainer = QWidget(self.LoginPage)
        self.LoginTextContainer.setObjectName(u"LoginTextContainer")
        self.verticalLayout_6 = QVBoxLayout(self.LoginTextContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.LoginText = QLabel(self.LoginTextContainer)
        self.LoginText.setObjectName(u"LoginText")

        self.verticalLayout_6.addWidget(self.LoginText, 0, Qt.AlignLeft|Qt.AlignTop)


        self.gridLayout_8.addWidget(self.LoginTextContainer, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 3, 3, 1, 1)

        self.LoginButtonContainer = QWidget(self.LoginPage)
        self.LoginButtonContainer.setObjectName(u"LoginButtonContainer")
        self.gridLayout_12 = QGridLayout(self.LoginButtonContainer)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.LoginLabelStatus = QLabel(self.LoginButtonContainer)
        self.LoginLabelStatus.setObjectName(u"LoginLabelStatus")

        self.gridLayout_12.addWidget(self.LoginLabelStatus, 0, 0, 1, 1)

        self.LoginButton = QPushButton(self.LoginButtonContainer)
        self.LoginButton.setObjectName(u"LoginButton")

        self.gridLayout_12.addWidget(self.LoginButton, 2, 0, 1, 1)

        self.GoResetPasswordButton = QPushButton(self.LoginButtonContainer)
        self.GoResetPasswordButton.setObjectName(u"GoResetPasswordButton")

        self.gridLayout_12.addWidget(self.GoResetPasswordButton, 2, 1, 1, 1)


        self.gridLayout_8.addWidget(self.LoginButtonContainer, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.PasswordContainer = QWidget(self.LoginPage)
        self.PasswordContainer.setObjectName(u"PasswordContainer")
        self.verticalLayout_8 = QVBoxLayout(self.PasswordContainer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.PasswordLabel = QLabel(self.PasswordContainer)
        self.PasswordLabel.setObjectName(u"PasswordLabel")

        self.verticalLayout_8.addWidget(self.PasswordLabel, 0, Qt.AlignTop)

        self.PasswordBox = QTextEdit(self.PasswordContainer)
        self.PasswordBox.setObjectName(u"PasswordBox")
        self.PasswordBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_8.addWidget(self.PasswordBox)


        self.gridLayout_8.addWidget(self.PasswordContainer, 3, 1, 1, 1, Qt.AlignTop)

        self.UsernameContainer = QWidget(self.LoginPage)
        self.UsernameContainer.setObjectName(u"UsernameContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.UsernameContainer.sizePolicy().hasHeightForWidth())
        self.UsernameContainer.setSizePolicy(sizePolicy1)
        self.verticalLayout_9 = QVBoxLayout(self.UsernameContainer)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.UsernameLabel = QLabel(self.UsernameContainer)
        self.UsernameLabel.setObjectName(u"UsernameLabel")

        self.verticalLayout_9.addWidget(self.UsernameLabel)

        self.UsernameBox = QTextEdit(self.UsernameContainer)
        self.UsernameBox.setObjectName(u"UsernameBox")
        sizePolicy1.setHeightForWidth(self.UsernameBox.sizePolicy().hasHeightForWidth())
        self.UsernameBox.setSizePolicy(sizePolicy1)
        self.UsernameBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_9.addWidget(self.UsernameBox)


        self.gridLayout_8.addWidget(self.UsernameContainer, 2, 1, 1, 1)

        self.ResetPasswordContainer = QWidget(self.LoginPage)
        self.ResetPasswordContainer.setObjectName(u"ResetPasswordContainer")
        self.verticalLayout_7 = QVBoxLayout(self.ResetPasswordContainer)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ResetEmailLabel = QLabel(self.ResetPasswordContainer)
        self.ResetEmailLabel.setObjectName(u"ResetEmailLabel")

        self.verticalLayout_7.addWidget(self.ResetEmailLabel)

        self.EmailBox = QTextEdit(self.ResetPasswordContainer)
        self.EmailBox.setObjectName(u"EmailBox")
        self.EmailBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_7.addWidget(self.EmailBox)

        self.ResetFlagStatus = QLabel(self.ResetPasswordContainer)
        self.ResetFlagStatus.setObjectName(u"ResetFlagStatus")

        self.verticalLayout_7.addWidget(self.ResetFlagStatus)

        self.ProcessResetPassword = QPushButton(self.ResetPasswordContainer)
        self.ProcessResetPassword.setObjectName(u"ProcessResetPassword")

        self.verticalLayout_7.addWidget(self.ProcessResetPassword)


        self.gridLayout_8.addWidget(self.ResetPasswordContainer, 5, 1, 1, 1, Qt.AlignTop)

        self.ContentFrame.addWidget(self.LoginPage)
        self.CreatePage = QWidget()
        self.CreatePage.setObjectName(u"CreatePage")
        self.horizontalLayout_22 = QHBoxLayout(self.CreatePage)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.CreatePageSubContainer = QWidget(self.CreatePage)
        self.CreatePageSubContainer.setObjectName(u"CreatePageSubContainer")
        self.horizontalLayout_24 = QHBoxLayout(self.CreatePageSubContainer)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_7)

        self.KolomAkun = QWidget(self.CreatePageSubContainer)
        self.KolomAkun.setObjectName(u"KolomAkun")
        self.verticalLayout_10 = QVBoxLayout(self.KolomAkun)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.BuatAkunContainer = QWidget(self.KolomAkun)
        self.BuatAkunContainer.setObjectName(u"BuatAkunContainer")
        self.verticalLayout_11 = QVBoxLayout(self.BuatAkunContainer)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.BuatAkunLabel = QLabel(self.BuatAkunContainer)
        self.BuatAkunLabel.setObjectName(u"BuatAkunLabel")

        self.verticalLayout_11.addWidget(self.BuatAkunLabel, 0, Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.BuatAkunContainer, 0, Qt.AlignTop)

        self.verticalSpacer_4 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.BuatUserContainer = QWidget(self.KolomAkun)
        self.BuatUserContainer.setObjectName(u"BuatUserContainer")
        self.verticalLayout_12 = QVBoxLayout(self.BuatUserContainer)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.BuatUsernameLabel = QLabel(self.BuatUserContainer)
        self.BuatUsernameLabel.setObjectName(u"BuatUsernameLabel")

        self.verticalLayout_12.addWidget(self.BuatUsernameLabel)

        self.BuatUserBox = QTextEdit(self.BuatUserContainer)
        self.BuatUserBox.setObjectName(u"BuatUserBox")
        self.BuatUserBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_12.addWidget(self.BuatUserBox)


        self.verticalLayout_10.addWidget(self.BuatUserContainer, 0, Qt.AlignTop)

        self.BuatPasswordContainer = QWidget(self.KolomAkun)
        self.BuatPasswordContainer.setObjectName(u"BuatPasswordContainer")
        self.verticalLayout_13 = QVBoxLayout(self.BuatPasswordContainer)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.BuatPasswordLabel = QLabel(self.BuatPasswordContainer)
        self.BuatPasswordLabel.setObjectName(u"BuatPasswordLabel")

        self.verticalLayout_13.addWidget(self.BuatPasswordLabel)

        self.BuatPasswordBox = QTextEdit(self.BuatPasswordContainer)
        self.BuatPasswordBox.setObjectName(u"BuatPasswordBox")
        self.BuatPasswordBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_13.addWidget(self.BuatPasswordBox)


        self.verticalLayout_10.addWidget(self.BuatPasswordContainer, 0, Qt.AlignTop)

        self.RePassContainer = QWidget(self.KolomAkun)
        self.RePassContainer.setObjectName(u"RePassContainer")
        self.verticalLayout_14 = QVBoxLayout(self.RePassContainer)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.RePassLabel = QLabel(self.RePassContainer)
        self.RePassLabel.setObjectName(u"RePassLabel")

        self.verticalLayout_14.addWidget(self.RePassLabel)

        self.RePassBox = QTextEdit(self.RePassContainer)
        self.RePassBox.setObjectName(u"RePassBox")
        self.RePassBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_14.addWidget(self.RePassBox)


        self.verticalLayout_10.addWidget(self.RePassContainer, 0, Qt.AlignTop)

        self.BuatAkunButContainer = QWidget(self.KolomAkun)
        self.BuatAkunButContainer.setObjectName(u"BuatAkunButContainer")
        self.verticalLayout_5 = QVBoxLayout(self.BuatAkunButContainer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.RegisterFlag = QLabel(self.BuatAkunButContainer)
        self.RegisterFlag.setObjectName(u"RegisterFlag")

        self.verticalLayout_5.addWidget(self.RegisterFlag)

        self.BuatAkunButton = QPushButton(self.BuatAkunButContainer)
        self.BuatAkunButton.setObjectName(u"BuatAkunButton")

        self.verticalLayout_5.addWidget(self.BuatAkunButton)


        self.verticalLayout_10.addWidget(self.BuatAkunButContainer, 0, Qt.AlignTop)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)


        self.horizontalLayout_24.addWidget(self.KolomAkun)

        self.KolomData = QWidget(self.CreatePageSubContainer)
        self.KolomData.setObjectName(u"KolomData")
        self.verticalLayout_15 = QVBoxLayout(self.KolomData)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.IsiDataContainer = QWidget(self.KolomData)
        self.IsiDataContainer.setObjectName(u"IsiDataContainer")
        self.verticalLayout_16 = QVBoxLayout(self.IsiDataContainer)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.IsiDataLabel = QLabel(self.IsiDataContainer)
        self.IsiDataLabel.setObjectName(u"IsiDataLabel")

        self.verticalLayout_16.addWidget(self.IsiDataLabel, 0, Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.IsiDataContainer, 0, Qt.AlignTop)

        self.NamaContainer = QWidget(self.KolomData)
        self.NamaContainer.setObjectName(u"NamaContainer")
        self.verticalLayout_17 = QVBoxLayout(self.NamaContainer)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.NamaLabel = QLabel(self.NamaContainer)
        self.NamaLabel.setObjectName(u"NamaLabel")

        self.verticalLayout_17.addWidget(self.NamaLabel)

        self.NamaBox = QTextEdit(self.NamaContainer)
        self.NamaBox.setObjectName(u"NamaBox")
        self.NamaBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_17.addWidget(self.NamaBox)


        self.verticalLayout_15.addWidget(self.NamaContainer, 0, Qt.AlignTop)

        self.PekerjaanContainer = QWidget(self.KolomData)
        self.PekerjaanContainer.setObjectName(u"PekerjaanContainer")
        self.verticalLayout_18 = QVBoxLayout(self.PekerjaanContainer)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.PekerjaanLabel = QLabel(self.PekerjaanContainer)
        self.PekerjaanLabel.setObjectName(u"PekerjaanLabel")

        self.verticalLayout_18.addWidget(self.PekerjaanLabel)

        self.PekerjaanBox = QTextEdit(self.PekerjaanContainer)
        self.PekerjaanBox.setObjectName(u"PekerjaanBox")
        self.PekerjaanBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_18.addWidget(self.PekerjaanBox)


        self.verticalLayout_15.addWidget(self.PekerjaanContainer, 0, Qt.AlignTop)

        self.AlamatEmailContainer = QWidget(self.KolomData)
        self.AlamatEmailContainer.setObjectName(u"AlamatEmailContainer")
        self.verticalLayout_2 = QVBoxLayout(self.AlamatEmailContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.AlamatEmailLabel = QLabel(self.AlamatEmailContainer)
        self.AlamatEmailLabel.setObjectName(u"AlamatEmailLabel")

        self.verticalLayout_2.addWidget(self.AlamatEmailLabel)

        self.AlamatEmailBox = QTextEdit(self.AlamatEmailContainer)
        self.AlamatEmailBox.setObjectName(u"AlamatEmailBox")
        self.AlamatEmailBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_2.addWidget(self.AlamatEmailBox)


        self.verticalLayout_15.addWidget(self.AlamatEmailContainer)

        self.GajiContainer = QWidget(self.KolomData)
        self.GajiContainer.setObjectName(u"GajiContainer")
        self.verticalLayout_19 = QVBoxLayout(self.GajiContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.GajiLabel = QLabel(self.GajiContainer)
        self.GajiLabel.setObjectName(u"GajiLabel")

        self.verticalLayout_19.addWidget(self.GajiLabel)

        self.GajiBox = QTextEdit(self.GajiContainer)
        self.GajiBox.setObjectName(u"GajiBox")
        self.GajiBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_19.addWidget(self.GajiBox)


        self.verticalLayout_15.addWidget(self.GajiContainer, 0, Qt.AlignTop)

        self.TempatKerjaContainer = QWidget(self.KolomData)
        self.TempatKerjaContainer.setObjectName(u"TempatKerjaContainer")
        self.verticalLayout_20 = QVBoxLayout(self.TempatKerjaContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.TempatKerjaLabel = QLabel(self.TempatKerjaContainer)
        self.TempatKerjaLabel.setObjectName(u"TempatKerjaLabel")

        self.verticalLayout_20.addWidget(self.TempatKerjaLabel)

        self.TempatKerjaBox = QTextEdit(self.TempatKerjaContainer)
        self.TempatKerjaBox.setObjectName(u"TempatKerjaBox")
        self.TempatKerjaBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_20.addWidget(self.TempatKerjaBox)


        self.verticalLayout_15.addWidget(self.TempatKerjaContainer, 0, Qt.AlignTop)

        self.TanggunganContainer = QWidget(self.KolomData)
        self.TanggunganContainer.setObjectName(u"TanggunganContainer")
        self.verticalLayout_21 = QVBoxLayout(self.TanggunganContainer)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.TanggunganLabel = QLabel(self.TanggunganContainer)
        self.TanggunganLabel.setObjectName(u"TanggunganLabel")

        self.verticalLayout_21.addWidget(self.TanggunganLabel)

        self.TanggunganBox = QTextEdit(self.TanggunganContainer)
        self.TanggunganBox.setObjectName(u"TanggunganBox")
        self.TanggunganBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_21.addWidget(self.TanggunganBox)


        self.verticalLayout_15.addWidget(self.TanggunganContainer, 0, Qt.AlignTop)

        self.CicilanContainer = QWidget(self.KolomData)
        self.CicilanContainer.setObjectName(u"CicilanContainer")
        self.verticalLayout_22 = QVBoxLayout(self.CicilanContainer)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.CicilanLabel = QLabel(self.CicilanContainer)
        self.CicilanLabel.setObjectName(u"CicilanLabel")

        self.verticalLayout_22.addWidget(self.CicilanLabel)

        self.CicilanBox = QTextEdit(self.CicilanContainer)
        self.CicilanBox.setObjectName(u"CicilanBox")
        self.CicilanBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_22.addWidget(self.CicilanBox)


        self.verticalLayout_15.addWidget(self.CicilanContainer, 0, Qt.AlignTop)

        self.TabunganContainer = QWidget(self.KolomData)
        self.TabunganContainer.setObjectName(u"TabunganContainer")
        self.verticalLayout_23 = QVBoxLayout(self.TabunganContainer)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.TabunganLabel = QLabel(self.TabunganContainer)
        self.TabunganLabel.setObjectName(u"TabunganLabel")

        self.verticalLayout_23.addWidget(self.TabunganLabel)

        self.TabunganBox = QTextEdit(self.TabunganContainer)
        self.TabunganBox.setObjectName(u"TabunganBox")
        self.TabunganBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_23.addWidget(self.TabunganBox)


        self.verticalLayout_15.addWidget(self.TabunganContainer, 0, Qt.AlignTop)

        self.SimpanDataContainer = QWidget(self.KolomData)
        self.SimpanDataContainer.setObjectName(u"SimpanDataContainer")
        self.verticalLayout_24 = QVBoxLayout(self.SimpanDataContainer)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.SavedFlag = QLabel(self.SimpanDataContainer)
        self.SavedFlag.setObjectName(u"SavedFlag")

        self.verticalLayout_24.addWidget(self.SavedFlag)

        self.SimpanDataButton = QPushButton(self.SimpanDataContainer)
        self.SimpanDataButton.setObjectName(u"SimpanDataButton")

        self.verticalLayout_24.addWidget(self.SimpanDataButton)


        self.verticalLayout_15.addWidget(self.SimpanDataContainer, 0, Qt.AlignLeft)


        self.horizontalLayout_24.addWidget(self.KolomData, 0, Qt.AlignTop)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_22.addWidget(self.CreatePageSubContainer)

        self.ContentFrame.addWidget(self.CreatePage)
        self.PerhitunganKPRPage = QWidget()
        self.PerhitunganKPRPage.setObjectName(u"PerhitunganKPRPage")
        self.gridLayout_13 = QGridLayout(self.PerhitunganKPRPage)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_9, 0, 3, 1, 1)

        self.OutputPerhitunganPageContainer = QWidget(self.PerhitunganKPRPage)
        self.OutputPerhitunganPageContainer.setObjectName(u"OutputPerhitunganPageContainer")
        self.verticalLayout_49 = QVBoxLayout(self.OutputPerhitunganPageContainer)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.OutputPerhitunganPageDetailPembayaranContainer = QFrame(self.OutputPerhitunganPageContainer)
        self.OutputPerhitunganPageDetailPembayaranContainer.setObjectName(u"OutputPerhitunganPageDetailPembayaranContainer")
        self.OutputPerhitunganPageDetailPembayaranContainer.setFrameShape(QFrame.StyledPanel)
        self.OutputPerhitunganPageDetailPembayaranContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.OutputPerhitunganPageDetailPembayaranContainer)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.OutputPerhitunganPageDetailPembayaranLabel = QLabel(self.OutputPerhitunganPageDetailPembayaranContainer)
        self.OutputPerhitunganPageDetailPembayaranLabel.setObjectName(u"OutputPerhitunganPageDetailPembayaranLabel")

        self.verticalLayout_52.addWidget(self.OutputPerhitunganPageDetailPembayaranLabel, 0, Qt.AlignTop)


        self.verticalLayout_49.addWidget(self.OutputPerhitunganPageDetailPembayaranContainer)

        self.OutputPerhitunganPageHargaBungaContainer = QFrame(self.OutputPerhitunganPageContainer)
        self.OutputPerhitunganPageHargaBungaContainer.setObjectName(u"OutputPerhitunganPageHargaBungaContainer")
        self.OutputPerhitunganPageHargaBungaContainer.setFrameShape(QFrame.StyledPanel)
        self.OutputPerhitunganPageHargaBungaContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.OutputPerhitunganPageHargaBungaContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.EstimasiHargaBungaLabel = QLabel(self.OutputPerhitunganPageHargaBungaContainer)
        self.EstimasiHargaBungaLabel.setObjectName(u"EstimasiHargaBungaLabel")

        self.gridLayout.addWidget(self.EstimasiHargaBungaLabel, 1, 0, 1, 1)

        self.HargaJangkaTahunSetelahLabel = QLabel(self.OutputPerhitunganPageHargaBungaContainer)
        self.HargaJangkaTahunSetelahLabel.setObjectName(u"HargaJangkaTahunSetelahLabel")

        self.gridLayout.addWidget(self.HargaJangkaTahunSetelahLabel, 5, 0, 1, 1)

        self.HargaJangkaTahunPertamaLabel = QLabel(self.OutputPerhitunganPageHargaBungaContainer)
        self.HargaJangkaTahunPertamaLabel.setObjectName(u"HargaJangkaTahunPertamaLabel")

        self.gridLayout.addWidget(self.HargaJangkaTahunPertamaLabel, 3, 0, 1, 1)

        self.PenulisanHargaJangkaTahunSetelahLabel = QLabel(self.OutputPerhitunganPageHargaBungaContainer)
        self.PenulisanHargaJangkaTahunSetelahLabel.setObjectName(u"PenulisanHargaJangkaTahunSetelahLabel")

        self.gridLayout.addWidget(self.PenulisanHargaJangkaTahunSetelahLabel, 5, 1, 1, 1)

        self.PenulisanHargaJangkaTahunPertamaLabel = QLabel(self.OutputPerhitunganPageHargaBungaContainer)
        self.PenulisanHargaJangkaTahunPertamaLabel.setObjectName(u"PenulisanHargaJangkaTahunPertamaLabel")

        self.gridLayout.addWidget(self.PenulisanHargaJangkaTahunPertamaLabel, 3, 1, 1, 1)


        self.verticalLayout_49.addWidget(self.OutputPerhitunganPageHargaBungaContainer)

        self.OutputPerhitunganPageEstimasiPembayaranContainer = QFrame(self.OutputPerhitunganPageContainer)
        self.OutputPerhitunganPageEstimasiPembayaranContainer.setObjectName(u"OutputPerhitunganPageEstimasiPembayaranContainer")
        self.OutputPerhitunganPageEstimasiPembayaranContainer.setFrameShape(QFrame.StyledPanel)
        self.OutputPerhitunganPageEstimasiPembayaranContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.OutputPerhitunganPageEstimasiPembayaranContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.EstimasiPembayaranLabel = QLabel(self.OutputPerhitunganPageEstimasiPembayaranContainer)
        self.EstimasiPembayaranLabel.setObjectName(u"EstimasiPembayaranLabel")

        self.gridLayout_2.addWidget(self.EstimasiPembayaranLabel, 0, 0, 1, 1)

        self.EstimasiPembayaranLainnyaLabel = QLabel(self.OutputPerhitunganPageEstimasiPembayaranContainer)
        self.EstimasiPembayaranLainnyaLabel.setObjectName(u"EstimasiPembayaranLainnyaLabel")

        self.gridLayout_2.addWidget(self.EstimasiPembayaranLainnyaLabel, 3, 0, 1, 1)

        self.AngsuranPertamaLabel = QLabel(self.OutputPerhitunganPageEstimasiPembayaranContainer)
        self.AngsuranPertamaLabel.setObjectName(u"AngsuranPertamaLabel")

        self.gridLayout_2.addWidget(self.AngsuranPertamaLabel, 2, 0, 1, 1)

        self.UangMukaLabel = QLabel(self.OutputPerhitunganPageEstimasiPembayaranContainer)
        self.UangMukaLabel.setObjectName(u"UangMukaLabel")

        self.gridLayout_2.addWidget(self.UangMukaLabel, 1, 0, 1, 1)

        self.PenulisanHargaUangMukaLabel = QLabel(self.OutputPerhitunganPageEstimasiPembayaranContainer)
        self.PenulisanHargaUangMukaLabel.setObjectName(u"PenulisanHargaUangMukaLabel")

        self.gridLayout_2.addWidget(self.PenulisanHargaUangMukaLabel, 1, 1, 1, 1)

        self.PenulisanHargaAngsuranPertamaLabel = QLabel(self.OutputPerhitunganPageEstimasiPembayaranContainer)
        self.PenulisanHargaAngsuranPertamaLabel.setObjectName(u"PenulisanHargaAngsuranPertamaLabel")

        self.gridLayout_2.addWidget(self.PenulisanHargaAngsuranPertamaLabel, 2, 1, 1, 1)

        self.PenulisanHargaEstimasiPembayaranLabel = QLabel(self.OutputPerhitunganPageEstimasiPembayaranContainer)
        self.PenulisanHargaEstimasiPembayaranLabel.setObjectName(u"PenulisanHargaEstimasiPembayaranLabel")

        self.gridLayout_2.addWidget(self.PenulisanHargaEstimasiPembayaranLabel, 3, 1, 1, 1)

        self.PenulisanHargaEstimasiJumlahBayarLabel = QLabel(self.OutputPerhitunganPageEstimasiPembayaranContainer)
        self.PenulisanHargaEstimasiJumlahBayarLabel.setObjectName(u"PenulisanHargaEstimasiJumlahBayarLabel")

        self.gridLayout_2.addWidget(self.PenulisanHargaEstimasiJumlahBayarLabel, 0, 1, 1, 1)


        self.verticalLayout_49.addWidget(self.OutputPerhitunganPageEstimasiPembayaranContainer)

        self.OutputPerhitunganPageDetailPinjamanContainer = QFrame(self.OutputPerhitunganPageContainer)
        self.OutputPerhitunganPageDetailPinjamanContainer.setObjectName(u"OutputPerhitunganPageDetailPinjamanContainer")
        self.OutputPerhitunganPageDetailPinjamanContainer.setFrameShape(QFrame.StyledPanel)
        self.OutputPerhitunganPageDetailPinjamanContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.OutputPerhitunganPageDetailPinjamanContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.PinjamanPokokLabel = QLabel(self.OutputPerhitunganPageDetailPinjamanContainer)
        self.PinjamanPokokLabel.setObjectName(u"PinjamanPokokLabel")

        self.gridLayout_3.addWidget(self.PinjamanPokokLabel, 2, 0, 1, 1)

        self.PenulisanHargaDetailPinjamanLabel = QLabel(self.OutputPerhitunganPageDetailPinjamanContainer)
        self.PenulisanHargaDetailPinjamanLabel.setObjectName(u"PenulisanHargaDetailPinjamanLabel")

        self.gridLayout_3.addWidget(self.PenulisanHargaDetailPinjamanLabel, 0, 1, 1, 1)

        self.DetailPinjamanLabel = QLabel(self.OutputPerhitunganPageDetailPinjamanContainer)
        self.DetailPinjamanLabel.setObjectName(u"DetailPinjamanLabel")

        self.gridLayout_3.addWidget(self.DetailPinjamanLabel, 0, 0, 1, 1)

        self.EstimasiBungaPinjamanLabel = QLabel(self.OutputPerhitunganPageDetailPinjamanContainer)
        self.EstimasiBungaPinjamanLabel.setObjectName(u"EstimasiBungaPinjamanLabel")

        self.gridLayout_3.addWidget(self.EstimasiBungaPinjamanLabel, 3, 0, 1, 1)

        self.PenulisanHargaPinjamanPokokLabel = QLabel(self.OutputPerhitunganPageDetailPinjamanContainer)
        self.PenulisanHargaPinjamanPokokLabel.setObjectName(u"PenulisanHargaPinjamanPokokLabel")

        self.gridLayout_3.addWidget(self.PenulisanHargaPinjamanPokokLabel, 2, 1, 1, 1)

        self.PenulisanHargaEstimasiBungaPinjamanLabel = QLabel(self.OutputPerhitunganPageDetailPinjamanContainer)
        self.PenulisanHargaEstimasiBungaPinjamanLabel.setObjectName(u"PenulisanHargaEstimasiBungaPinjamanLabel")

        self.gridLayout_3.addWidget(self.PenulisanHargaEstimasiBungaPinjamanLabel, 3, 1, 1, 1)


        self.verticalLayout_49.addWidget(self.OutputPerhitunganPageDetailPinjamanContainer)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_10)


        self.gridLayout_13.addWidget(self.OutputPerhitunganPageContainer, 0, 2, 1, 1)

        self.InputPerhitunganPageContainer = QWidget(self.PerhitunganKPRPage)
        self.InputPerhitunganPageContainer.setObjectName(u"InputPerhitunganPageContainer")
        self.verticalLayout_44 = QVBoxLayout(self.InputPerhitunganPageContainer)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.PerhitunganKPRContainer = QWidget(self.InputPerhitunganPageContainer)
        self.PerhitunganKPRContainer.setObjectName(u"PerhitunganKPRContainer")
        self.verticalLayout_45 = QVBoxLayout(self.PerhitunganKPRContainer)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.PerhitunganKPRLabel = QLabel(self.PerhitunganKPRContainer)
        self.PerhitunganKPRLabel.setObjectName(u"PerhitunganKPRLabel")

        self.verticalLayout_45.addWidget(self.PerhitunganKPRLabel)


        self.verticalLayout_44.addWidget(self.PerhitunganKPRContainer)

        self.PerhitunganKPRHargaContainer = QWidget(self.InputPerhitunganPageContainer)
        self.PerhitunganKPRHargaContainer.setObjectName(u"PerhitunganKPRHargaContainer")
        self.verticalLayout_46 = QVBoxLayout(self.PerhitunganKPRHargaContainer)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.PerhitunganKPRHargaPropertiLabel = QLabel(self.PerhitunganKPRHargaContainer)
        self.PerhitunganKPRHargaPropertiLabel.setObjectName(u"PerhitunganKPRHargaPropertiLabel")

        self.verticalLayout_46.addWidget(self.PerhitunganKPRHargaPropertiLabel)

        self.PerhitunganKPRUangMukaTextEdit = QTextEdit(self.PerhitunganKPRHargaContainer)
        self.PerhitunganKPRUangMukaTextEdit.setObjectName(u"PerhitunganKPRUangMukaTextEdit")
        self.PerhitunganKPRUangMukaTextEdit.setMaximumSize(QSize(300, 20))

        self.verticalLayout_46.addWidget(self.PerhitunganKPRUangMukaTextEdit)

        self.PerhitunganKPRUangMukaLabel = QLabel(self.PerhitunganKPRHargaContainer)
        self.PerhitunganKPRUangMukaLabel.setObjectName(u"PerhitunganKPRUangMukaLabel")

        self.verticalLayout_46.addWidget(self.PerhitunganKPRUangMukaLabel)

        self.PerhitunganKPRHargaPropertiTextEdit = QTextEdit(self.PerhitunganKPRHargaContainer)
        self.PerhitunganKPRHargaPropertiTextEdit.setObjectName(u"PerhitunganKPRHargaPropertiTextEdit")
        self.PerhitunganKPRHargaPropertiTextEdit.setMaximumSize(QSize(300, 20))

        self.verticalLayout_46.addWidget(self.PerhitunganKPRHargaPropertiTextEdit)

        self.BungaTetapcheckBox = QCheckBox(self.PerhitunganKPRHargaContainer)
        self.BungaTetapcheckBox.setObjectName(u"BungaTetapcheckBox")

        self.verticalLayout_46.addWidget(self.BungaTetapcheckBox)

        self.BungaBerjenjangcheckBox = QCheckBox(self.PerhitunganKPRHargaContainer)
        self.BungaBerjenjangcheckBox.setObjectName(u"BungaBerjenjangcheckBox")

        self.verticalLayout_46.addWidget(self.BungaBerjenjangcheckBox)


        self.verticalLayout_44.addWidget(self.PerhitunganKPRHargaContainer, 0, Qt.AlignTop)

        self.TipeTipeBunga = QStackedWidget(self.InputPerhitunganPageContainer)
        self.TipeTipeBunga.setObjectName(u"TipeTipeBunga")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_30 = QVBoxLayout(self.page_3)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.PerhitunganKPRPersentaseSukuBungaLabel = QLabel(self.page_3)
        self.PerhitunganKPRPersentaseSukuBungaLabel.setObjectName(u"PerhitunganKPRPersentaseSukuBungaLabel")

        self.verticalLayout_30.addWidget(self.PerhitunganKPRPersentaseSukuBungaLabel)

        self.PerhitunganKPRMasaKreditLabelTextEdit = QTextEdit(self.page_3)
        self.PerhitunganKPRMasaKreditLabelTextEdit.setObjectName(u"PerhitunganKPRMasaKreditLabelTextEdit")
        self.PerhitunganKPRMasaKreditLabelTextEdit.setMaximumSize(QSize(300, 20))

        self.verticalLayout_30.addWidget(self.PerhitunganKPRMasaKreditLabelTextEdit)

        self.PerhitunganKPRMasaKreditLabel = QLabel(self.page_3)
        self.PerhitunganKPRMasaKreditLabel.setObjectName(u"PerhitunganKPRMasaKreditLabel")

        self.verticalLayout_30.addWidget(self.PerhitunganKPRMasaKreditLabel)

        self.PerhitunganKPRJangkaWaktuKreditTextEdit = QTextEdit(self.page_3)
        self.PerhitunganKPRJangkaWaktuKreditTextEdit.setObjectName(u"PerhitunganKPRJangkaWaktuKreditTextEdit")
        self.PerhitunganKPRJangkaWaktuKreditTextEdit.setMaximumSize(QSize(300, 20))

        self.verticalLayout_30.addWidget(self.PerhitunganKPRJangkaWaktuKreditTextEdit)

        self.PerhitunganKPRJangkaWaktuKreditLabel = QLabel(self.page_3)
        self.PerhitunganKPRJangkaWaktuKreditLabel.setObjectName(u"PerhitunganKPRJangkaWaktuKreditLabel")

        self.verticalLayout_30.addWidget(self.PerhitunganKPRJangkaWaktuKreditLabel)

        self.PerhitunganKPRPersentaseSukuBungaLabelTextEdit = QTextEdit(self.page_3)
        self.PerhitunganKPRPersentaseSukuBungaLabelTextEdit.setObjectName(u"PerhitunganKPRPersentaseSukuBungaLabelTextEdit")
        self.PerhitunganKPRPersentaseSukuBungaLabelTextEdit.setMaximumSize(QSize(300, 20))

        self.verticalLayout_30.addWidget(self.PerhitunganKPRPersentaseSukuBungaLabelTextEdit)

        self.TipeTipeBunga.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_39 = QVBoxLayout(self.page_4)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.PerhitunganKPRPersentaseLamaKreditBerjenjangLabel = QLabel(self.page_4)
        self.PerhitunganKPRPersentaseLamaKreditBerjenjangLabel.setObjectName(u"PerhitunganKPRPersentaseLamaKreditBerjenjangLabel")

        self.verticalLayout_39.addWidget(self.PerhitunganKPRPersentaseLamaKreditBerjenjangLabel)

        self.spinBox = QSpinBox(self.page_4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(300, 16777215))
        self.spinBox.setMinimum(1)

        self.verticalLayout_39.addWidget(self.spinBox)

        self.PerhitunganKPRBungaPerTahunKreditBerjenjangLabel = QLabel(self.page_4)
        self.PerhitunganKPRBungaPerTahunKreditBerjenjangLabel.setObjectName(u"PerhitunganKPRBungaPerTahunKreditBerjenjangLabel")

        self.verticalLayout_39.addWidget(self.PerhitunganKPRBungaPerTahunKreditBerjenjangLabel)

        self.PerhitunganKPRPersentaseLamaKreditBerjenjangBox = QTextEdit(self.page_4)
        self.PerhitunganKPRPersentaseLamaKreditBerjenjangBox.setObjectName(u"PerhitunganKPRPersentaseLamaKreditBerjenjangBox")
        self.PerhitunganKPRPersentaseLamaKreditBerjenjangBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_39.addWidget(self.PerhitunganKPRPersentaseLamaKreditBerjenjangBox)

        self.BungaEskalasiLabel = QLabel(self.page_4)
        self.BungaEskalasiLabel.setObjectName(u"BungaEskalasiLabel")

        self.verticalLayout_39.addWidget(self.BungaEskalasiLabel)

        self.EskalasiBungaBox = QTextEdit(self.page_4)
        self.EskalasiBungaBox.setObjectName(u"EskalasiBungaBox")
        self.EskalasiBungaBox.setMaximumSize(QSize(300, 25))

        self.verticalLayout_39.addWidget(self.EskalasiBungaBox)

        self.PerhitunganKPRJangkaWaktuKreditBerjenjangLabel = QLabel(self.page_4)
        self.PerhitunganKPRJangkaWaktuKreditBerjenjangLabel.setObjectName(u"PerhitunganKPRJangkaWaktuKreditBerjenjangLabel")

        self.verticalLayout_39.addWidget(self.PerhitunganKPRJangkaWaktuKreditBerjenjangLabel)

        self.PerhitunganKPRJangkaWaktuMasaKreditBerjenjang = QTextEdit(self.page_4)
        self.PerhitunganKPRJangkaWaktuMasaKreditBerjenjang.setObjectName(u"PerhitunganKPRJangkaWaktuMasaKreditBerjenjang")
        self.PerhitunganKPRJangkaWaktuMasaKreditBerjenjang.setMaximumSize(QSize(300, 25))

        self.verticalLayout_39.addWidget(self.PerhitunganKPRJangkaWaktuMasaKreditBerjenjang)

        self.TipeTipeBunga.addWidget(self.page_4)

        self.verticalLayout_44.addWidget(self.TipeTipeBunga, 0, Qt.AlignTop)

        self.PerhitunganKPRCalculateButtonContainer = QWidget(self.InputPerhitunganPageContainer)
        self.PerhitunganKPRCalculateButtonContainer.setObjectName(u"PerhitunganKPRCalculateButtonContainer")
        self.verticalLayout_48 = QVBoxLayout(self.PerhitunganKPRCalculateButtonContainer)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.PerhitunganKPRCalculateButton = QPushButton(self.PerhitunganKPRCalculateButtonContainer)
        self.PerhitunganKPRCalculateButton.setObjectName(u"PerhitunganKPRCalculateButton")

        self.verticalLayout_48.addWidget(self.PerhitunganKPRCalculateButton)


        self.verticalLayout_44.addWidget(self.PerhitunganKPRCalculateButtonContainer, 0, Qt.AlignTop)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_9)


        self.gridLayout_13.addWidget(self.InputPerhitunganPageContainer, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_10, 0, 1, 1, 1)

        self.ContentFrame.addWidget(self.PerhitunganKPRPage)
        self.DetailPembayaranPage = QWidget()
        self.DetailPembayaranPage.setObjectName(u"DetailPembayaranPage")
        self.verticalLayout_50 = QVBoxLayout(self.DetailPembayaranPage)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.DetailPembayaranPageContainer = QFrame(self.DetailPembayaranPage)
        self.DetailPembayaranPageContainer.setObjectName(u"DetailPembayaranPageContainer")
        self.DetailPembayaranPageContainer.setFrameShape(QFrame.StyledPanel)
        self.DetailPembayaranPageContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.DetailPembayaranPageContainer)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.DetailPembayaranPageLabel = QLabel(self.DetailPembayaranPageContainer)
        self.DetailPembayaranPageLabel.setObjectName(u"DetailPembayaranPageLabel")

        self.verticalLayout_51.addWidget(self.DetailPembayaranPageLabel, 0, Qt.AlignTop)


        self.verticalLayout_50.addWidget(self.DetailPembayaranPageContainer)

        self.DetailPembayaranPageContentContainer = QFrame(self.DetailPembayaranPage)
        self.DetailPembayaranPageContentContainer.setObjectName(u"DetailPembayaranPageContentContainer")
        self.DetailPembayaranPageContentContainer.setFrameShape(QFrame.StyledPanel)
        self.DetailPembayaranPageContentContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.DetailPembayaranPageContentContainer)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.GambarRumahImage = QLabel(self.DetailPembayaranPageContentContainer)
        self.GambarRumahImage.setObjectName(u"GambarRumahImage")

        self.gridLayout_4.addWidget(self.GambarRumahImage, 0, 0, 1, 1)

        self.DeskripsiPembayaranLabel = QLabel(self.DetailPembayaranPageContentContainer)
        self.DeskripsiPembayaranLabel.setObjectName(u"DeskripsiPembayaranLabel")

        self.gridLayout_4.addWidget(self.DeskripsiPembayaranLabel, 1, 0, 1, 1)

        self.JumlahDibayarLabel = QLabel(self.DetailPembayaranPageContentContainer)
        self.JumlahDibayarLabel.setObjectName(u"JumlahDibayarLabel")

        self.gridLayout_4.addWidget(self.JumlahDibayarLabel, 0, 2, 1, 1)

        self.PenulisanHargaJumlahDibayarLabel = QLabel(self.DetailPembayaranPageContentContainer)
        self.PenulisanHargaJumlahDibayarLabel.setObjectName(u"PenulisanHargaJumlahDibayarLabel")

        self.gridLayout_4.addWidget(self.PenulisanHargaJumlahDibayarLabel, 1, 2, 1, 1)


        self.verticalLayout_50.addWidget(self.DetailPembayaranPageContentContainer)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_50.addItem(self.verticalSpacer_11)

        self.ContentFrame.addWidget(self.DetailPembayaranPage)
        self.ContactPage = QWidget()
        self.ContactPage.setObjectName(u"ContactPage")
        self.verticalLayout_53 = QVBoxLayout(self.ContactPage)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.ContactPageContainer = QFrame(self.ContactPage)
        self.ContactPageContainer.setObjectName(u"ContactPageContainer")
        self.ContactPageContainer.setFrameShape(QFrame.StyledPanel)
        self.ContactPageContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.ContactPageContainer)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.ContactPageLabel = QLabel(self.ContactPageContainer)
        self.ContactPageLabel.setObjectName(u"ContactPageLabel")

        self.verticalLayout_54.addWidget(self.ContactPageLabel, 0, Qt.AlignTop)


        self.verticalLayout_53.addWidget(self.ContactPageContainer)

        self.ContactPersonPageContainer = QFrame(self.ContactPage)
        self.ContactPersonPageContainer.setObjectName(u"ContactPersonPageContainer")
        self.ContactPersonPageContainer.setFrameShape(QFrame.StyledPanel)
        self.ContactPersonPageContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.ContactPersonPageContainer)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.EmailLabel = QLabel(self.ContactPersonPageContainer)
        self.EmailLabel.setObjectName(u"EmailLabel")

        self.gridLayout_5.addWidget(self.EmailLabel, 3, 0, 1, 1)

        self.MarketingLabel = QLabel(self.ContactPersonPageContainer)
        self.MarketingLabel.setObjectName(u"MarketingLabel")

        self.gridLayout_5.addWidget(self.MarketingLabel, 1, 0, 1, 1)

        self.ContactPersonLabel = QLabel(self.ContactPersonPageContainer)
        self.ContactPersonLabel.setObjectName(u"ContactPersonLabel")

        self.gridLayout_5.addWidget(self.ContactPersonLabel, 0, 0, 1, 1)

        self.CustomerServiceLabel = QLabel(self.ContactPersonPageContainer)
        self.CustomerServiceLabel.setObjectName(u"CustomerServiceLabel")

        self.gridLayout_5.addWidget(self.CustomerServiceLabel, 2, 0, 1, 1)

        self.MarketingNumberLabel = QLabel(self.ContactPersonPageContainer)
        self.MarketingNumberLabel.setObjectName(u"MarketingNumberLabel")

        self.gridLayout_5.addWidget(self.MarketingNumberLabel, 1, 1, 1, 1)

        self.CustomerServiceNumberLabel = QLabel(self.ContactPersonPageContainer)
        self.CustomerServiceNumberLabel.setObjectName(u"CustomerServiceNumberLabel")

        self.gridLayout_5.addWidget(self.CustomerServiceNumberLabel, 2, 1, 1, 1)

        self.label_4 = QLabel(self.ContactPersonPageContainer)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 3, 1, 1, 1)


        self.verticalLayout_53.addWidget(self.ContactPersonPageContainer)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_12)

        self.ContentFrame.addWidget(self.ContactPage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.verticalLayout_55 = QVBoxLayout(self.SettingsPage)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.SettingsPageLabelContainer = QFrame(self.SettingsPage)
        self.SettingsPageLabelContainer.setObjectName(u"SettingsPageLabelContainer")
        self.SettingsPageLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.SettingsPageLabelContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.SettingsPageLabelContainer)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.SettingsPageLabel = QLabel(self.SettingsPageLabelContainer)
        self.SettingsPageLabel.setObjectName(u"SettingsPageLabel")

        self.verticalLayout_56.addWidget(self.SettingsPageLabel)


        self.verticalLayout_55.addWidget(self.SettingsPageLabelContainer)

        self.SettingsPageControlContainer = QWidget(self.SettingsPage)
        self.SettingsPageControlContainer.setObjectName(u"SettingsPageControlContainer")
        self.verticalLayout_57 = QVBoxLayout(self.SettingsPageControlContainer)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.DarkModeLabel = QLabel(self.SettingsPageControlContainer)
        self.DarkModeLabel.setObjectName(u"DarkModeLabel")

        self.verticalLayout_57.addWidget(self.DarkModeLabel)

        self.DarkModeCheckBox = QCheckBox(self.SettingsPageControlContainer)
        self.DarkModeCheckBox.setObjectName(u"DarkModeCheckBox")

        self.verticalLayout_57.addWidget(self.DarkModeCheckBox)


        self.verticalLayout_55.addWidget(self.SettingsPageControlContainer)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_13)

        self.ContentFrame.addWidget(self.SettingsPage)
        self.DisplayContentPage = QWidget()
        self.DisplayContentPage.setObjectName(u"DisplayContentPage")
        self.gridLayout_6 = QGridLayout(self.DisplayContentPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea_2 = QScrollArea(self.DisplayContentPage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 700, 758))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.widget_9 = QWidget(self.scrollAreaWidgetContents)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.AlamatRumah = QLabel(self.widget_9)
        self.AlamatRumah.setObjectName(u"AlamatRumah")

        self.horizontalLayout_28.addWidget(self.AlamatRumah)

        self.KontakPengurus = QLabel(self.widget_9)
        self.KontakPengurus.setObjectName(u"KontakPengurus")

        self.horizontalLayout_28.addWidget(self.KontakPengurus)

        self.MatplotlibSketch = QPushButton(self.widget_9)
        self.MatplotlibSketch.setObjectName(u"MatplotlibSketch")

        self.horizontalLayout_28.addWidget(self.MatplotlibSketch)


        self.gridLayout_10.addWidget(self.widget_9, 5, 0, 1, 1)

        self.widget_8 = QWidget(self.scrollAreaWidgetContents)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_26 = QVBoxLayout(self.widget_8)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.GoBackToHomeButton = QPushButton(self.widget_8)
        self.GoBackToHomeButton.setObjectName(u"GoBackToHomeButton")
        icon11 = QIcon()
        icon11.addFile(u":/FeatherIcons/feather/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.GoBackToHomeButton.setIcon(icon11)

        self.verticalLayout_26.addWidget(self.GoBackToHomeButton)


        self.gridLayout_10.addWidget(self.widget_8, 0, 0, 1, 1, Qt.AlignTop)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.DeskripsiRumah = QLabel(self.widget_7)
        self.DeskripsiRumah.setObjectName(u"DeskripsiRumah")

        self.horizontalLayout_23.addWidget(self.DeskripsiRumah)

        self.IsiRumah = QLabel(self.widget_7)
        self.IsiRumah.setObjectName(u"IsiRumah")

        self.horizontalLayout_23.addWidget(self.IsiRumah)

        self.LokasiGarisBesar = QWebEngineView(self.widget_7)
        self.LokasiGarisBesar.setObjectName(u"LokasiGarisBesar")
        self.LokasiGarisBesar.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_23.addWidget(self.LokasiGarisBesar)


        self.gridLayout_10.addWidget(self.widget_7, 4, 0, 1, 1)

        self.SubContentWidget_1 = QWidget(self.scrollAreaWidgetContents)
        self.SubContentWidget_1.setObjectName(u"SubContentWidget_1")
        self.gridLayout_11 = QGridLayout(self.SubContentWidget_1)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.FotoRumahLabel = QWebEngineView(self.SubContentWidget_1)
        self.FotoRumahLabel.setObjectName(u"FotoRumahLabel")
        self.FotoRumahLabel.setUrl(QUrl(u"about:blank"))

        self.gridLayout_11.addWidget(self.FotoRumahLabel, 0, 1, 1, 1)

        self.JudulRumah = QLabel(self.SubContentWidget_1)
        self.JudulRumah.setObjectName(u"JudulRumah")

        self.gridLayout_11.addWidget(self.JudulRumah, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.SubContentWidget_1, 1, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.ContentFrame.addWidget(self.DisplayContentPage)

        self.horizontalLayout_11.addWidget(self.ContentFrame)

        self.NotificatioFrame = QStackedWidget(self.ContentWindow)
        self.NotificatioFrame.setObjectName(u"NotificatioFrame")
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.verticalLayout_25 = QVBoxLayout(self.Dashboard)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.ProfilePageExitContainer = QWidget(self.Dashboard)
        self.ProfilePageExitContainer.setObjectName(u"ProfilePageExitContainer")
        self.horizontalLayout_27 = QHBoxLayout(self.ProfilePageExitContainer)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.ProfilePageExitButton = QPushButton(self.ProfilePageExitContainer)
        self.ProfilePageExitButton.setObjectName(u"ProfilePageExitButton")
        icon12 = QIcon()
        icon12.addFile(u":/FeatherIcons/feather/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ProfilePageExitButton.setIcon(icon12)
        self.ProfilePageExitButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.ProfilePageExitButton)

        self.label_11 = QLabel(self.ProfilePageExitContainer)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_27.addWidget(self.label_11)


        self.verticalLayout_25.addWidget(self.ProfilePageExitContainer, 0, Qt.AlignLeft|Qt.AlignTop)

        self.ProfilePageLoginContainer = QWidget(self.Dashboard)
        self.ProfilePageLoginContainer.setObjectName(u"ProfilePageLoginContainer")
        self.verticalLayout_3 = QVBoxLayout(self.ProfilePageLoginContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ProfileRegisterButton = QPushButton(self.ProfilePageLoginContainer)
        self.ProfileRegisterButton.setObjectName(u"ProfileRegisterButton")

        self.verticalLayout_3.addWidget(self.ProfileRegisterButton)

        self.ProfileLoginButton = QPushButton(self.ProfilePageLoginContainer)
        self.ProfileLoginButton.setObjectName(u"ProfileLoginButton")

        self.verticalLayout_3.addWidget(self.ProfileLoginButton)


        self.verticalLayout_25.addWidget(self.ProfilePageLoginContainer)

        self.ProfilePagePhotoContainer = QWidget(self.Dashboard)
        self.ProfilePagePhotoContainer.setObjectName(u"ProfilePagePhotoContainer")
        self.verticalLayout_27 = QVBoxLayout(self.ProfilePagePhotoContainer)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.ProfilePagePhoto = QLabel(self.ProfilePagePhotoContainer)
        self.ProfilePagePhoto.setObjectName(u"ProfilePagePhoto")
        self.ProfilePagePhoto.setFrameShape(QFrame.Box)

        self.verticalLayout_27.addWidget(self.ProfilePagePhoto)


        self.verticalLayout_25.addWidget(self.ProfilePagePhotoContainer)

        self.DashboardControlContainer = QWidget(self.Dashboard)
        self.DashboardControlContainer.setObjectName(u"DashboardControlContainer")
        self.verticalLayout_28 = QVBoxLayout(self.DashboardControlContainer)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.EditDataButton = QPushButton(self.DashboardControlContainer)
        self.EditDataButton.setObjectName(u"EditDataButton")

        self.verticalLayout_28.addWidget(self.EditDataButton)

        self.DashboardTransaksiButton = QPushButton(self.DashboardControlContainer)
        self.DashboardTransaksiButton.setObjectName(u"DashboardTransaksiButton")

        self.verticalLayout_28.addWidget(self.DashboardTransaksiButton)

        self.DashboardEditDataButton = QPushButton(self.DashboardControlContainer)
        self.DashboardEditDataButton.setObjectName(u"DashboardEditDataButton")

        self.verticalLayout_28.addWidget(self.DashboardEditDataButton)


        self.verticalLayout_25.addWidget(self.DashboardControlContainer)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_6)

        self.NotificatioFrame.addWidget(self.Dashboard)
        self.Notifications = QWidget()
        self.Notifications.setObjectName(u"Notifications")
        self.verticalLayout_29 = QVBoxLayout(self.Notifications)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.NotificationsCloseContainer = QWidget(self.Notifications)
        self.NotificationsCloseContainer.setObjectName(u"NotificationsCloseContainer")
        self.horizontalLayout_26 = QHBoxLayout(self.NotificationsCloseContainer)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.NotificationsCloseContainerButton = QPushButton(self.NotificationsCloseContainer)
        self.NotificationsCloseContainerButton.setObjectName(u"NotificationsCloseContainerButton")
        self.NotificationsCloseContainerButton.setIcon(icon12)
        self.NotificationsCloseContainerButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.NotificationsCloseContainerButton)

        self.NotificationsLabel = QLabel(self.NotificationsCloseContainer)
        self.NotificationsLabel.setObjectName(u"NotificationsLabel")

        self.horizontalLayout_26.addWidget(self.NotificationsLabel)


        self.verticalLayout_29.addWidget(self.NotificationsCloseContainer, 0, Qt.AlignLeft|Qt.AlignTop)

        self.NotificationsDefaultContainer = QWidget(self.Notifications)
        self.NotificationsDefaultContainer.setObjectName(u"NotificationsDefaultContainer")
        self.verticalLayout_31 = QVBoxLayout(self.NotificationsDefaultContainer)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.NotificationsDefaultText = QLabel(self.NotificationsDefaultContainer)
        self.NotificationsDefaultText.setObjectName(u"NotificationsDefaultText")

        self.verticalLayout_31.addWidget(self.NotificationsDefaultText, 0, Qt.AlignHCenter)


        self.verticalLayout_29.addWidget(self.NotificationsDefaultContainer)

        self.NotificationsContentOneContainer = QWidget(self.Notifications)
        self.NotificationsContentOneContainer.setObjectName(u"NotificationsContentOneContainer")
        self.verticalLayout_32 = QVBoxLayout(self.NotificationsContentOneContainer)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.NotificationsContentOneCloseContainer = QFrame(self.NotificationsContentOneContainer)
        self.NotificationsContentOneCloseContainer.setObjectName(u"NotificationsContentOneCloseContainer")
        self.NotificationsContentOneCloseContainer.setFrameShape(QFrame.StyledPanel)
        self.NotificationsContentOneCloseContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.NotificationsContentOneCloseContainer)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.NotificationsContentOneCloseButton = QPushButton(self.NotificationsContentOneCloseContainer)
        self.NotificationsContentOneCloseButton.setObjectName(u"NotificationsContentOneCloseButton")
        self.NotificationsContentOneCloseButton.setIcon(icon12)
        self.NotificationsContentOneCloseButton.setIconSize(QSize(24, 24))

        self.verticalLayout_33.addWidget(self.NotificationsContentOneCloseButton, 0, Qt.AlignTop)


        self.verticalLayout_32.addWidget(self.NotificationsContentOneCloseContainer, 0, Qt.AlignTop)

        self.NotificationsContentOneTextContainer = QFrame(self.NotificationsContentOneContainer)
        self.NotificationsContentOneTextContainer.setObjectName(u"NotificationsContentOneTextContainer")
        self.NotificationsContentOneTextContainer.setFrameShape(QFrame.StyledPanel)
        self.NotificationsContentOneTextContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.NotificationsContentOneTextContainer)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.JudulContentOne = QLabel(self.NotificationsContentOneTextContainer)
        self.JudulContentOne.setObjectName(u"JudulContentOne")

        self.verticalLayout_34.addWidget(self.JudulContentOne)

        self.IsiContentOne = QLabel(self.NotificationsContentOneTextContainer)
        self.IsiContentOne.setObjectName(u"IsiContentOne")

        self.verticalLayout_34.addWidget(self.IsiContentOne)


        self.verticalLayout_32.addWidget(self.NotificationsContentOneTextContainer)


        self.verticalLayout_29.addWidget(self.NotificationsContentOneContainer)

        self.NotificationsContentTwoContainer = QWidget(self.Notifications)
        self.NotificationsContentTwoContainer.setObjectName(u"NotificationsContentTwoContainer")
        self.verticalLayout_35 = QVBoxLayout(self.NotificationsContentTwoContainer)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.NotificationsContentTwoCloseContainer = QFrame(self.NotificationsContentTwoContainer)
        self.NotificationsContentTwoCloseContainer.setObjectName(u"NotificationsContentTwoCloseContainer")
        self.NotificationsContentTwoCloseContainer.setFrameShape(QFrame.StyledPanel)
        self.NotificationsContentTwoCloseContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.NotificationsContentTwoCloseContainer)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.NotificationsContentTwoCloseButton = QPushButton(self.NotificationsContentTwoCloseContainer)
        self.NotificationsContentTwoCloseButton.setObjectName(u"NotificationsContentTwoCloseButton")
        self.NotificationsContentTwoCloseButton.setIcon(icon12)
        self.NotificationsContentTwoCloseButton.setIconSize(QSize(24, 24))

        self.verticalLayout_36.addWidget(self.NotificationsContentTwoCloseButton)


        self.verticalLayout_35.addWidget(self.NotificationsContentTwoCloseContainer, 0, Qt.AlignTop)

        self.NotificationsContentTwoTextContainer = QFrame(self.NotificationsContentTwoContainer)
        self.NotificationsContentTwoTextContainer.setObjectName(u"NotificationsContentTwoTextContainer")
        self.NotificationsContentTwoTextContainer.setFrameShape(QFrame.StyledPanel)
        self.NotificationsContentTwoTextContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.NotificationsContentTwoTextContainer)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.JudulContentTwo = QLabel(self.NotificationsContentTwoTextContainer)
        self.JudulContentTwo.setObjectName(u"JudulContentTwo")

        self.verticalLayout_37.addWidget(self.JudulContentTwo)

        self.IsiContentTwo = QLabel(self.NotificationsContentTwoTextContainer)
        self.IsiContentTwo.setObjectName(u"IsiContentTwo")

        self.verticalLayout_37.addWidget(self.IsiContentTwo)


        self.verticalLayout_35.addWidget(self.NotificationsContentTwoTextContainer)


        self.verticalLayout_29.addWidget(self.NotificationsContentTwoContainer)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_7)

        self.NotificatioFrame.addWidget(self.Notifications)
        self.SearchPreferences = QWidget()
        self.SearchPreferences.setObjectName(u"SearchPreferences")
        self.verticalLayout_38 = QVBoxLayout(self.SearchPreferences)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.SearchPreferencesControlContainer = QWidget(self.SearchPreferences)
        self.SearchPreferencesControlContainer.setObjectName(u"SearchPreferencesControlContainer")
        self.horizontalLayout_10 = QHBoxLayout(self.SearchPreferencesControlContainer)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.SearchPreferencesCloseButton = QPushButton(self.SearchPreferencesControlContainer)
        self.SearchPreferencesCloseButton.setObjectName(u"SearchPreferencesCloseButton")
        self.SearchPreferencesCloseButton.setIcon(icon12)
        self.SearchPreferencesCloseButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.SearchPreferencesCloseButton)

        self.SearchPreferencesLabel = QLabel(self.SearchPreferencesControlContainer)
        self.SearchPreferencesLabel.setObjectName(u"SearchPreferencesLabel")

        self.horizontalLayout_10.addWidget(self.SearchPreferencesLabel)


        self.verticalLayout_38.addWidget(self.SearchPreferencesControlContainer, 0, Qt.AlignLeft|Qt.AlignTop)

        self.SearchPreferencesRuangKamarContainer = QWidget(self.SearchPreferences)
        self.SearchPreferencesRuangKamarContainer.setObjectName(u"SearchPreferencesRuangKamarContainer")
        self.verticalLayout_40 = QVBoxLayout(self.SearchPreferencesRuangKamarContainer)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.SearchPreferencesRuangKamarLabel = QLabel(self.SearchPreferencesRuangKamarContainer)
        self.SearchPreferencesRuangKamarLabel.setObjectName(u"SearchPreferencesRuangKamarLabel")

        self.verticalLayout_40.addWidget(self.SearchPreferencesRuangKamarLabel)

        self.SearchPreferencesRuangKamarContainerCheckBox = QCheckBox(self.SearchPreferencesRuangKamarContainer)
        self.SearchPreferencesRuangKamarContainerCheckBox.setObjectName(u"SearchPreferencesRuangKamarContainerCheckBox")

        self.verticalLayout_40.addWidget(self.SearchPreferencesRuangKamarContainerCheckBox)

        self.SearchPreferencesRuangKamarContainerCheckBox_2 = QCheckBox(self.SearchPreferencesRuangKamarContainer)
        self.SearchPreferencesRuangKamarContainerCheckBox_2.setObjectName(u"SearchPreferencesRuangKamarContainerCheckBox_2")

        self.verticalLayout_40.addWidget(self.SearchPreferencesRuangKamarContainerCheckBox_2)

        self.SearchPreferencesRuangKamarContainerCheckBox_3 = QCheckBox(self.SearchPreferencesRuangKamarContainer)
        self.SearchPreferencesRuangKamarContainerCheckBox_3.setObjectName(u"SearchPreferencesRuangKamarContainerCheckBox_3")

        self.verticalLayout_40.addWidget(self.SearchPreferencesRuangKamarContainerCheckBox_3)


        self.verticalLayout_38.addWidget(self.SearchPreferencesRuangKamarContainer)

        self.SearchPreferencesRentangHargaContainer = QWidget(self.SearchPreferences)
        self.SearchPreferencesRentangHargaContainer.setObjectName(u"SearchPreferencesRentangHargaContainer")
        self.verticalLayout_42 = QVBoxLayout(self.SearchPreferencesRentangHargaContainer)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.SearchPreferencesRentangHargaLabel = QLabel(self.SearchPreferencesRentangHargaContainer)
        self.SearchPreferencesRentangHargaLabel.setObjectName(u"SearchPreferencesRentangHargaLabel")

        self.verticalLayout_42.addWidget(self.SearchPreferencesRentangHargaLabel, 0, Qt.AlignTop)

        self.SearchPreferencesRentangHargaBawahLabel = QLabel(self.SearchPreferencesRentangHargaContainer)
        self.SearchPreferencesRentangHargaBawahLabel.setObjectName(u"SearchPreferencesRentangHargaBawahLabel")

        self.verticalLayout_42.addWidget(self.SearchPreferencesRentangHargaBawahLabel, 0, Qt.AlignTop)

        self.SearchPreferencesRentangHargaBawahTextEdit = QPlainTextEdit(self.SearchPreferencesRentangHargaContainer)
        self.SearchPreferencesRentangHargaBawahTextEdit.setObjectName(u"SearchPreferencesRentangHargaBawahTextEdit")
        self.SearchPreferencesRentangHargaBawahTextEdit.setMaximumSize(QSize(300, 20))

        self.verticalLayout_42.addWidget(self.SearchPreferencesRentangHargaBawahTextEdit)

        self.SearchPreferencesRentangHargaAtasLabel = QLabel(self.SearchPreferencesRentangHargaContainer)
        self.SearchPreferencesRentangHargaAtasLabel.setObjectName(u"SearchPreferencesRentangHargaAtasLabel")

        self.verticalLayout_42.addWidget(self.SearchPreferencesRentangHargaAtasLabel)

        self.SearchPreferencesRentangHargaAtasTextEdit = QPlainTextEdit(self.SearchPreferencesRentangHargaContainer)
        self.SearchPreferencesRentangHargaAtasTextEdit.setObjectName(u"SearchPreferencesRentangHargaAtasTextEdit")
        self.SearchPreferencesRentangHargaAtasTextEdit.setMaximumSize(QSize(300, 20))

        self.verticalLayout_42.addWidget(self.SearchPreferencesRentangHargaAtasTextEdit)


        self.verticalLayout_38.addWidget(self.SearchPreferencesRentangHargaContainer, 0, Qt.AlignTop)

        self.SearchPreferensiTransportasiContainer = QWidget(self.SearchPreferences)
        self.SearchPreferensiTransportasiContainer.setObjectName(u"SearchPreferensiTransportasiContainer")
        self.verticalLayout_41 = QVBoxLayout(self.SearchPreferensiTransportasiContainer)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.SearchPreferensiTransportasiLabel = QLabel(self.SearchPreferensiTransportasiContainer)
        self.SearchPreferensiTransportasiLabel.setObjectName(u"SearchPreferensiTransportasiLabel")

        self.verticalLayout_41.addWidget(self.SearchPreferensiTransportasiLabel)

        self.KRLCommuterCheckBox = QCheckBox(self.SearchPreferensiTransportasiContainer)
        self.KRLCommuterCheckBox.setObjectName(u"KRLCommuterCheckBox")

        self.verticalLayout_41.addWidget(self.KRLCommuterCheckBox)

        self.TransjakartaCheckBox = QCheckBox(self.SearchPreferensiTransportasiContainer)
        self.TransjakartaCheckBox.setObjectName(u"TransjakartaCheckBox")

        self.verticalLayout_41.addWidget(self.TransjakartaCheckBox)


        self.verticalLayout_38.addWidget(self.SearchPreferensiTransportasiContainer)

        self.SearchPreferensiSimpanContainer = QWidget(self.SearchPreferences)
        self.SearchPreferensiSimpanContainer.setObjectName(u"SearchPreferensiSimpanContainer")
        self.verticalLayout_43 = QVBoxLayout(self.SearchPreferensiSimpanContainer)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.SearchPreferensiSimpanButton = QPushButton(self.SearchPreferensiSimpanContainer)
        self.SearchPreferensiSimpanButton.setObjectName(u"SearchPreferensiSimpanButton")

        self.verticalLayout_43.addWidget(self.SearchPreferensiSimpanButton)


        self.verticalLayout_38.addWidget(self.SearchPreferensiSimpanContainer)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_8)

        self.NotificatioFrame.addWidget(self.SearchPreferences)

        self.horizontalLayout_11.addWidget(self.NotificatioFrame)


        self.verticalLayout.addWidget(self.ContentWindow)


        self.gridLayout_7.addWidget(self.SubProgramWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.Central)

        self.retranslateUi(MainWindow)

        self.ContentFrame.setCurrentIndex(0)
        self.TipeTipeBunga.setCurrentIndex(1)
        self.NotificatioFrame.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LogoLabel.setText("")
        self.Minimize.setText("")
        self.Resize.setText("")
        self.CloseButton.setText("")
        self.Rumah.setText("")
        self.Kredit.setText("")
        self.Beli.setText("")
        self.Bantuan.setText("")
        self.Preferences.setText("")
        self.Notifcation.setText("")
        self.User.setText("")
        self.Pengaturan.setText("")
        self.Desc_4.setText(QCoreApplication.translate("MainWindow", u"Text Goes Here", None))
        self.Price_4.setText(QCoreApplication.translate("MainWindow", u"Price and Check", None))
        self.Desc_3.setText(QCoreApplication.translate("MainWindow", u"Text Goes Here", None))
        self.Price_3.setText(QCoreApplication.translate("MainWindow", u"Price and Check", None))
        self.Desc_2.setText(QCoreApplication.translate("MainWindow", u"Text Goes Here", None))
        self.Price_2.setText(QCoreApplication.translate("MainWindow", u"Price and Check", None))
        self.Desc_1.setText(QCoreApplication.translate("MainWindow", u"Text Goes Here", None))
        self.Price_1.setText(QCoreApplication.translate("MainWindow", u"Price and Check", None))
        self.PreviousButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.KClusterButton.setText(QCoreApplication.translate("MainWindow", u"Lihat Clustering Harga Rumah", None))
        self.NextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.LoginText.setText(QCoreApplication.translate("MainWindow", u"LOGIN PAGE", None))
        self.LoginLabelStatus.setText(QCoreApplication.translate("MainWindow", u"StatusFlagHere", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.GoResetPasswordButton.setText(QCoreApplication.translate("MainWindow", u"Reset Password", None))
        self.PasswordLabel.setText(QCoreApplication.translate("MainWindow", u"PASSWORD :", None))
        self.UsernameLabel.setText(QCoreApplication.translate("MainWindow", u"USERNAME :", None))
        self.ResetEmailLabel.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.ResetFlagStatus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ProcessResetPassword.setText(QCoreApplication.translate("MainWindow", u"Reset Password", None))
        self.BuatAkunLabel.setText(QCoreApplication.translate("MainWindow", u"Buat Akun", None))
        self.BuatUsernameLabel.setText(QCoreApplication.translate("MainWindow", u"USERNAME :", None))
        self.BuatPasswordLabel.setText(QCoreApplication.translate("MainWindow", u"PASSWORD :", None))
        self.RePassLabel.setText(QCoreApplication.translate("MainWindow", u"RETYPE PASSWORD :", None))
        self.RegisterFlag.setText(QCoreApplication.translate("MainWindow", u"RegisterFlagHere", None))
        self.BuatAkunButton.setText(QCoreApplication.translate("MainWindow", u"Buat Akun", None))
        self.IsiDataLabel.setText(QCoreApplication.translate("MainWindow", u"Isi Data", None))
        self.NamaLabel.setText(QCoreApplication.translate("MainWindow", u"Nama Lengkap :", None))
        self.PekerjaanLabel.setText(QCoreApplication.translate("MainWindow", u"Pekerjaan :", None))
        self.AlamatEmailLabel.setText(QCoreApplication.translate("MainWindow", u"Alamat Email :", None))
        self.GajiLabel.setText(QCoreApplication.translate("MainWindow", u"Range Gaji  :", None))
        self.TempatKerjaLabel.setText(QCoreApplication.translate("MainWindow", u"Tempat Kerja :", None))
        self.TanggunganLabel.setText(QCoreApplication.translate("MainWindow", u"Tanggungan :", None))
        self.CicilanLabel.setText(QCoreApplication.translate("MainWindow", u"Beban Cicilan :", None))
        self.TabunganLabel.setText(QCoreApplication.translate("MainWindow", u"Tabungan :", None))
        self.SavedFlag.setText(QCoreApplication.translate("MainWindow", u"SavedFlagHere", None))
        self.SimpanDataButton.setText(QCoreApplication.translate("MainWindow", u"Simpan Data", None))
        self.OutputPerhitunganPageDetailPembayaranLabel.setText(QCoreApplication.translate("MainWindow", u"Detail Pembayaran :", None))
        self.EstimasiHargaBungaLabel.setText(QCoreApplication.translate("MainWindow", u"Estimasi Harga Pembayaran Bunga :", None))
        self.HargaJangkaTahunSetelahLabel.setText(QCoreApplication.translate("MainWindow", u"Harga Jangka Setelah", None))
        self.HargaJangkaTahunPertamaLabel.setText(QCoreApplication.translate("MainWindow", u"Harga Jangka Tahun Pertama", None))
        self.PenulisanHargaJangkaTahunSetelahLabel.setText(QCoreApplication.translate("MainWindow", u"$MONEY$", None))
        self.PenulisanHargaJangkaTahunPertamaLabel.setText(QCoreApplication.translate("MainWindow", u"$MONEY$", None))
        self.EstimasiPembayaranLabel.setText(QCoreApplication.translate("MainWindow", u"Estimasi Pembayaran Pertama :", None))
        self.EstimasiPembayaranLainnyaLabel.setText(QCoreApplication.translate("MainWindow", u"Estimasi Pembayaran Lainnya :", None))
        self.AngsuranPertamaLabel.setText(QCoreApplication.translate("MainWindow", u"Angsuran Pertama :", None))
        self.UangMukaLabel.setText(QCoreApplication.translate("MainWindow", u"Uang Muka :", None))
        self.PenulisanHargaUangMukaLabel.setText(QCoreApplication.translate("MainWindow", u"$MONEY$", None))
        self.PenulisanHargaAngsuranPertamaLabel.setText(QCoreApplication.translate("MainWindow", u"$MONEY$", None))
        self.PenulisanHargaEstimasiPembayaranLabel.setText(QCoreApplication.translate("MainWindow", u"$MONEY$", None))
        self.PenulisanHargaEstimasiJumlahBayarLabel.setText(QCoreApplication.translate("MainWindow", u"$MONEY$", None))
        self.PinjamanPokokLabel.setText(QCoreApplication.translate("MainWindow", u"Pinjaman Pokok :", None))
        self.PenulisanHargaDetailPinjamanLabel.setText(QCoreApplication.translate("MainWindow", u"$MONEY$", None))
        self.DetailPinjamanLabel.setText(QCoreApplication.translate("MainWindow", u"Detail Pinjaman :", None))
        self.EstimasiBungaPinjamanLabel.setText(QCoreApplication.translate("MainWindow", u"Estimasi Bunga Pinjaman :", None))
        self.PenulisanHargaPinjamanPokokLabel.setText(QCoreApplication.translate("MainWindow", u"$MONEY$", None))
        self.PenulisanHargaEstimasiBungaPinjamanLabel.setText(QCoreApplication.translate("MainWindow", u"$MONEY$", None))
        self.PerhitunganKPRLabel.setText(QCoreApplication.translate("MainWindow", u"Perhitungan KPR", None))
        self.PerhitunganKPRHargaPropertiLabel.setText(QCoreApplication.translate("MainWindow", u"Harga Properti :", None))
        self.PerhitunganKPRUangMukaLabel.setText(QCoreApplication.translate("MainWindow", u"Jumlah Uang Muka yang Diberikan :", None))
        self.BungaTetapcheckBox.setText(QCoreApplication.translate("MainWindow", u"Bunga Tetap", None))
        self.BungaBerjenjangcheckBox.setText(QCoreApplication.translate("MainWindow", u"Bunga Berjenjang", None))
        self.PerhitunganKPRPersentaseSukuBungaLabel.setText(QCoreApplication.translate("MainWindow", u"Suka Bunga (Dalam Persen) :", None))
        self.PerhitunganKPRMasaKreditLabel.setText(QCoreApplication.translate("MainWindow", u"Masa Kredit :", None))
        self.PerhitunganKPRJangkaWaktuKreditLabel.setText(QCoreApplication.translate("MainWindow", u"Jangka Waktu Kredit :", None))
        self.PerhitunganKPRPersentaseLamaKreditBerjenjangLabel.setText(QCoreApplication.translate("MainWindow", u"Masa Kredit Berjenjang", None))
        self.PerhitunganKPRBungaPerTahunKreditBerjenjangLabel.setText(QCoreApplication.translate("MainWindow", u"Bunga Awal", None))
        self.BungaEskalasiLabel.setText(QCoreApplication.translate("MainWindow", u"Eskalasi Bunga", None))
        self.PerhitunganKPRJangkaWaktuKreditBerjenjangLabel.setText(QCoreApplication.translate("MainWindow", u"Masa KPR", None))
        self.PerhitunganKPRCalculateButton.setText(QCoreApplication.translate("MainWindow", u"Hitung", None))
        self.DetailPembayaranPageLabel.setText(QCoreApplication.translate("MainWindow", u"Detail Pembayaran Bulan Ini :", None))
        self.GambarRumahImage.setText(QCoreApplication.translate("MainWindow", u"Gambar Rumah :", None))
        self.DeskripsiPembayaranLabel.setText(QCoreApplication.translate("MainWindow", u"Deskripsi", None))
        self.JumlahDibayarLabel.setText(QCoreApplication.translate("MainWindow", u"Jumlah Dibayar Bulan Ini :", None))
        self.PenulisanHargaJumlahDibayarLabel.setText(QCoreApplication.translate("MainWindow", u"$MONEY$", None))
        self.ContactPageLabel.setText(QCoreApplication.translate("MainWindow", u"Hubungi Kami :", None))
        self.EmailLabel.setText(QCoreApplication.translate("MainWindow", u"Email :", None))
        self.MarketingLabel.setText(QCoreApplication.translate("MainWindow", u"Marketing :", None))
        self.ContactPersonLabel.setText(QCoreApplication.translate("MainWindow", u"Contact Person :", None))
        self.CustomerServiceLabel.setText(QCoreApplication.translate("MainWindow", u"Customer Service :", None))
        self.MarketingNumberLabel.setText(QCoreApplication.translate("MainWindow", u"#NUMBERS#", None))
        self.CustomerServiceNumberLabel.setText(QCoreApplication.translate("MainWindow", u"#NUMBERS#", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"#Email#", None))
        self.SettingsPageLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.DarkModeLabel.setText(QCoreApplication.translate("MainWindow", u"Enable Dark Mode :", None))
        self.DarkModeCheckBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.AlamatRumah.setText(QCoreApplication.translate("MainWindow", u"AlamatRumah", None))
        self.KontakPengurus.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.MatplotlibSketch.setText(QCoreApplication.translate("MainWindow", u"Lihat Tren Grafik Rumah Ini!", None))
        self.GoBackToHomeButton.setText(QCoreApplication.translate("MainWindow", u"Go Back", None))
        self.DeskripsiRumah.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.IsiRumah.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.JudulRumah.setText(QCoreApplication.translate("MainWindow", u"Judul Rumah", None))
        self.ProfilePageExitButton.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Profile Page", None))
        self.ProfileRegisterButton.setText(QCoreApplication.translate("MainWindow", u"Buat Akun", None))
        self.ProfileLoginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.ProfilePagePhoto.setText(QCoreApplication.translate("MainWindow", u"Profile Photo", None))
        self.EditDataButton.setText(QCoreApplication.translate("MainWindow", u"Edit Data", None))
        self.DashboardTransaksiButton.setText(QCoreApplication.translate("MainWindow", u"Lihat Transaksi", None))
        self.DashboardEditDataButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.NotificationsCloseContainerButton.setText("")
        self.NotificationsLabel.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.NotificationsDefaultText.setText(QCoreApplication.translate("MainWindow", u"No Notifications", None))
        self.NotificationsContentOneCloseButton.setText("")
        self.JudulContentOne.setText(QCoreApplication.translate("MainWindow", u"Judul Notifikasi", None))
        self.IsiContentOne.setText(QCoreApplication.translate("MainWindow", u"Isi Notifikasi", None))
        self.NotificationsContentTwoCloseButton.setText("")
        self.JudulContentTwo.setText(QCoreApplication.translate("MainWindow", u"Judul Notifikasi", None))
        self.IsiContentTwo.setText(QCoreApplication.translate("MainWindow", u"Isi Notifikasi", None))
        self.SearchPreferencesCloseButton.setText("")
        self.SearchPreferencesLabel.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.SearchPreferencesRuangKamarLabel.setText(QCoreApplication.translate("MainWindow", u"Jumlah Kamar :", None))
        self.SearchPreferencesRuangKamarContainerCheckBox.setText(QCoreApplication.translate("MainWindow", u"1 Kamar Tidur", None))
        self.SearchPreferencesRuangKamarContainerCheckBox_2.setText(QCoreApplication.translate("MainWindow", u"2 Kamar Tidur", None))
        self.SearchPreferencesRuangKamarContainerCheckBox_3.setText(QCoreApplication.translate("MainWindow", u"3 Kamar Tidur", None))
        self.SearchPreferencesRentangHargaLabel.setText(QCoreApplication.translate("MainWindow", u"Rentang Harga :", None))
        self.SearchPreferencesRentangHargaBawahLabel.setText(QCoreApplication.translate("MainWindow", u"Rentang Harga Bawah :", None))
        self.SearchPreferencesRentangHargaAtasLabel.setText(QCoreApplication.translate("MainWindow", u"Rentang Harga Atas :", None))
        self.SearchPreferensiTransportasiLabel.setText(QCoreApplication.translate("MainWindow", u"Akses Transportasi Umum", None))
        self.KRLCommuterCheckBox.setText(QCoreApplication.translate("MainWindow", u"KRL Kommuter", None))
        self.TransjakartaCheckBox.setText(QCoreApplication.translate("MainWindow", u"Transjakarta", None))
        self.SearchPreferensiSimpanButton.setText(QCoreApplication.translate("MainWindow", u"Simpan Preferensi", None))
    # retranslateUi

