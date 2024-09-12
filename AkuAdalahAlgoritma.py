import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ElbowCanvas(FigureCanvas):
    def PlottingGraph():

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

    def KCluster():
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

