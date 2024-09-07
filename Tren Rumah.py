import pandas as pd
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget

class Canvas(FigureCanvas):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        
        dataFrame = pd.read_csv("jabodetabek_house_price.csv")

        X = dataFrame.drop(["url", "address", "district", "title", "building_orientation", "furnishing",
                    "property_condition", "facilities", "property_type", "city", "ads_id",
                    "certificate", "electricity"], axis=1)
        X_filled = X.fillna({
            "bedrooms": 0,
            "bathrooms": 0,
            "land_size_m2": 0,
            "building_size_m2": 0,
            "floors": 0,
            "building_age": 0,
            "year_built": 0
        })

        x = X_filled["price_in_rp"]
        y = X_filled["building_size_m2"]

        graph = pd.DataFrame({"price": x, "land_size_m2": y})
        graph.plot(kind="line", grid=True, figsize=(15, 8), title="House Tren", xlabel="Price", ylabel="Land Size (M^2)")
        plt.show()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 800)
        
        chart = Canvas(self)

app = QApplication(sys.argv)
demo = App()
demo.show()
sys.exit(app.exec())

