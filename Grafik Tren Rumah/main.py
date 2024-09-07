import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTabWidget, QHBoxLayout
import sys

class ElbowCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots(figsize=(8, 4), dpi=100)
        super().__init__(fig)
        self.setParent(parent)
        self.plot_elbow()
    
    def plot_elbow(self):
        dataFrame = pd.read_csv("jabodetabek_house_price.csv")

        # Data Cleaning and Drop Column
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
        
        clusters = []
        for i in range(1,11):
            kmeans = KMeans(n_clusters=i)
            kmeans.fit(X_filled)
            clusters.append(kmeans.inertia_)

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.lineplot(x=list(range(1, 11)), y=clusters, ax=ax)
        ax.set_title('Elbow Method')
        ax.set_xlabel('Clusters')
        ax.set_ylabel('Inertia')
        
        km5 = KMeans(n_clusters=5)
        km5.fit(X_filled)

        X_filled["cluster"] = km5.labels_
        
        plt.figure(figsize=(8, 3))
        sns.scatterplot(x=X_filled["price_in_rp"], y=X_filled["land_size_m2"], hue=X_filled["cluster"], palette="deep")
        plt.title("Cluster Plot")
        plt.show()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("House Price Clustering")
        self.resize(900, 800)
        self.layout = QVBoxLayout()
        
        
        self.tabs = QTabWidget()
        self.elbow_tab = QWidget()
        self.cluster_tab = QWidget()
        
        self.tabs.addTab(self.elbow_tab, "Elbow Method")
        self.tabs.addTab(self.cluster_tab, "Cluster Plot")
        
        
        self.elbow_layout = QVBoxLayout()
        self.elbow_canvas = ElbowCanvas(self)
        self.elbow_layout.addWidget(self.elbow_canvas)
        self.elbow_tab.setLayout(self.elbow_layout)
        
        
        self.cluster_layout = QVBoxLayout()
        self.cluster_canvas = ElbowCanvas(self)
        self.cluster_layout.addWidget(self.cluster_canvas)
        self.cluster_tab.setLayout(self.cluster_layout)
        
        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())









