# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:27:47 2024

@author: User
"""

import skimage.io
import matplotlib.pyplot as plt
import numpy as np
img = skimage.io.imread(r"C:\Users\User\OneDrive\Desktop\Fordham\Data Mining (CISC-5790-L02)\image.png")
skimage.io.imshow(img)
plt.show()

normalized_img=img/255
pixels=normalized_img.reshape(-1,3) #-> shape(28312, 3)

initial_centroids = {
    2: [(0, 0, 0), (0.1, 0.1, 0.1)],
    3: [(0, 0, 0), (0.1, 0.1, 0.1), (0.2, 0.2, 0.2)],
    6: [(0, 0, 0), (0.1, 0.1, 0.1), (0.2, 0.2, 0.2), (0.3, 0.3, 0.3), (0.4, 0.4, 0.4), (0.5, 0.5, 0.5)],
    10: [(0, 0, 0), (0.1, 0.1, 0.1), (0.2, 0.2, 0.2), (0.3, 0.3, 0.3), (0.4, 0.4, 0.4), 
         (0.5, 0.5, 0.5), (0.6, 0.6, 0.6), (0.7, 0.7, 0.7), (0.8, 0.8, 0.8), (0.9, 0.9, 0.9)],
}

cluster_color = np.array([
    (60, 179, 113),  # SpringGreen
    (0, 191, 255),   # DeepSkyBlue
    (255, 255, 0),   # Yellow
    (255, 0, 0),     # Red
    (0, 0, 0),       # Black
    (169, 169, 169), # DarkGray
    (255, 140, 0),   # DarkOrange
    (128, 0, 128),   # Purple
    (255, 192, 203), # Pink
    (255, 255, 255), # White
])/255


def k_means(pixels, centroids, k):
    labels = np.zeros(pixels.shape[0], dtype=int)  # Initialize labels

    for iteration in range(50):  # Maximum 50 iterations
    
        # Step 1: Assign pixels to the nearest centroid
        distances_2D = np.zeros((pixels.shape[0], k))
        for i in range(pixels.shape[0]):
            for j in range(k):
                distances_2D[i, j] = np.sqrt(np.sum((pixels[i] - centroids[j]) ** 2))
        new_labels = np.argmin(distances_2D, axis=1)  # Assign labels based on nearest centroid

        # Step 2: Update centroids
        for j in range(k):
            assigned_pixels = pixels[new_labels == j]  # Pixels belonging to cluster j
            if len(assigned_pixels) > 0:
                centroids[j] = assigned_pixels.mean(axis=0)

        # Step 3: Check for convergence
        if np.all(labels == new_labels):
            break
        labels = new_labels  # Update centroids for the next iteration
        
    sse=np.sum((pixels-centroids[labels])**2)
        
    return labels, centroids, sse

def color_img():
    for k, initial_centroid in initial_centroids.items():
        centroids=np.array(initial_centroid)
        labels, update_centroids, sse = k_means(pixels, centroids, k)
        print(f'Final SSE for k={k}: {sse}')
        
        colored_pixels=np.zeros((pixels.shape[0],3))
        for i in range(len(labels)): #index i
            colored_pixels[i]=cluster_color[labels[i]] #-> labels[i] is actual label
        
        # Reshape directly to the original image dimensions
        colored_img = colored_pixels.reshape(img.shape)
    
        # Display the clustered image
        plt.imshow(colored_img)
        plt.title(f'Clustered Image with k={k}')
        plt.axis('off')
        plt.show()
color_img()
            
#The image is originally a 2D array (height x width x 3), where each pixel is represented by an RGB value
#Flattening the image into a 2D array (pixels.reshape(-1, 3)), image = a list of pixels, we lose the original structure (height and width)
# -> to display the final image, we need original height and width => reshape back to original shape
        
    
           
                
                
    