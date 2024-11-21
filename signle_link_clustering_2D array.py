# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:54:08 2024

@author: User
"""

import numpy as np

def signle_link_clustering(data):
    clusters=[]
    for x in data:
        clusters.append([x])
        
    #create the dist matrix
    n=len(clusters)
    dist=np.zeros((n,n))
    
    
    #fill the matrix with initial dist between all pairs of elements
    for i in range(n):
        for j in range(i+1, n):
            dist[i,j]=abs(data[j]-data[i])
            dist[j,i]=dist[i,j]
            
    steps=[]
    while len(clusters)>1:
        #find the closest clusters(min dist)
        min_dist=float('inf')
        closest_a, closest_b=0,1
        
        #search through the dist matrix to find the min dist
        for a in range(len(clusters)):
            for b in range(a+1, len(clusters)):
                if dist[a,b]< min_dist:
                    min_dist=dist[a,b]
                    closest_a, closest_b=a,b
        
        # Merge the closest clusters
        clusters[closest_a].extend(clusters[closest_b])  # Merge clusters
        del clusters[closest_b]  # Remove the merged cluster from the list

        # Update the distance matrix by calculating the distance between the merged cluster and others
        for i in range(len(clusters)):
            if i != closest_a:
                # Update the distance between the merged cluster and the remaining clusters
                new_dist = min(dist[i, closest_a], dist[i, closest_b])
                dist[i, closest_a] = new_dist
                dist[closest_a, i] = new_dist
        
        # Remove the row and column for the merged cluster
        dist = np.delete(dist, closest_b, axis=0)
        dist = np.delete(dist, closest_b, axis=1)

        # Record the current state of the clusters and the minimum distance between the merged clusters
        steps.append((clusters.copy(), min_dist))
    
    return steps

data = [0, 4, 5, 20, 25, 39, 43, 44]

signle_link_clustering(data)