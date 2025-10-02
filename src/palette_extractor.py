import cv2
import numpy as np
from sklearn.cluster import KMeans

def extract_palette(image_path, num_colors=5):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((-1, 3))

    kmeans = KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(image)

    colors = kmeans.cluster_centers_.astype(int)
    return colors
