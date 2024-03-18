# final code without resize
import cv2
import math
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def normalize(rgb):
    maxval = max(rgb)
    return [rgb[0]/maxval,rgb[1]/maxval,rgb[2]/maxval]
def mapColors(input):
    colors = [[255,255,255],[0,128,0],[255,195,11],[128,0,128],[51, 36, 33]]
    ratios = [[1,1,1],[0.89,1,0.316],[1,0.806,0.186],[1,0.436,0.196],[1,0.77,0.688]]
    for i in range(0,len(input)):
        center = normalize(input[i])
        rgb = [255,255,255]
        minDistance = 100
        for j in range(0,len(colors)):
            ratio = ratios[j]
            distance = math.sqrt((ratio[0] - center[0])**2 + (ratio[1] - center[1])**2 + (ratio[2] - center[2])**2)
            if distance<minDistance:
                rgb = colors[j]
                minDistance = distance
        input[i] = rgb
    return input
def calPercentage(img):
    green = yellow = purple = brown = 0

    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if (img[i][j] == [0,128,0]).all():
                green+=1
            elif (img[i][j] == [255,195,11]).all():
                yellow+=1
            elif (img[i][j] == [128,0,128]).all():
                purple+=1
            elif (img[i][j] == [51, 36, 33]).all():
                brown+=1
        total  = green+yellow+purple+brown
    return [yellow*100/total, purple*100/total, brown*100/total , green*100/total]
def detect_color_clusters(image_path, num_clusters):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pixels = img.reshape((-1, 3))

    # Perform k-means clustering
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(pixels)

    # Get the labels and cluster centers
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    centers = mapColors(centers)
    labels = labels.reshape(img.shape[:2])
    segmented_img = centers[labels].astype(np.uint8)
    percentages = calPercentage(segmented_img)
    #Display the original and segmented images using matplotlib
    plt.figure(figsize=(10, 5))
    #percentages=[0,0,0,0]

    plt.subplot(1, 3, 1)
    plt.title('Input Image')
    plt.imshow(img)

    plt.subplot(1, 3, 2)
    plt.title('Output Image')
    plt.imshow(segmented_img)

    plt.subplot(1, 3, 3)

    plt.text(0.1, 0.6, f'Nitrogen: {percentages[0]:.2f}%', color='black', fontsize=10, va='center')
    plt.text(0.1, 0.5, f'Phosphorous: {percentages[1]:.2f}%', color='black', fontsize=10, va='center')
    plt.text(0.1, 0.4, f'Potassium: {percentages[2]:.2f}%', color='black', fontsize=10, va='center')
    plt.text(0.1,0.3 , f'Normal: {percentages[3]:.2f}%', color='black', fontsize=10, va='center')
    plt.axis('off')

    plt.show()

# Example usage
image_path = "/content/drive/MyDrive/dataset-2/Copy of Phosphorus62.png"
detect_color_clusters(image_path, num_clusters=20)
