import cv2
import math
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def padImage(image,size):
    twidth,theight = siz
    width, height = image.size
    if (width) >= (height):
        new_width = 256
        new_height = int(height * (256 / width))
    else:
        new_height = 256
        new_width = int(width * (256 / height))
    image = image.resize((new_width, new_height))
    # Calculate the position for centering the image within the padded canvas
    x = (padding_width - new_width) // 2
    y = (padding_height - new_height) // 2

    # Create a new canvas with the specified padding color
    new_image = Image.new('RGB', (padding_width, padding_height), padding_color)

    # Paste the original image onto the padded canvas at the center
    new_image.paste(image, (x, y))
def normalize(rgb):
    maxval = max(rgb)
    return [rgb[0]/maxval,rgb[1]/maxval,rgb[2]/maxval]
def mapColors(input):
    colors = [[255,255,255],[0,100,0],[238,210,2],[128,0,128],[39,19,0]]
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
            if (img[i][j] == [0,100,0]).all():
                green+=1
            elif (img[i][j] == [238,210,2]).all():
                yellow+=1
            elif (img[i][j] == [128,0,128]).all():
                purple+=1
            elif (img[i][j] == [39,19,0]).all():
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
image_path = "/content/drive/MyDrive/Dataset/Phosphorus23.png"
detect_color_clusters(image_path, num_clusters=20)
