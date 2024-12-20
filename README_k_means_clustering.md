
# K-Means Image Clustering

## Overview
This Python program applies the K-Means clustering algorithm to an image for color quantization. 
It reads an input image, normalizes its pixel values, and clusters the pixels into a predefined number of clusters (k). 
The output is a visualized version of the image with clustered colors.

---

## Requirements

- **Python Version:** 3.7 or later
- **Required Libraries:**
  - `numpy`
  - `matplotlib`
  - `scikit-image`

### Install Dependencies
To install the required libraries, run:
```bash
pip install numpy matplotlib scikit-image
```

---

## How to Run the Program

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the Directory**  
   Move into the directory where the repository was cloned:
   ```bash
   cd <repository_folder>
   ```

3. **Set the Image Path**  
   Place your image file in the desired directory and update the path in the code:
   ```python
   img = skimage.io.imread(r"your_image_path")
   ```

4. **Run the Program**  
   Execute the script using Python:
   ```bash
   python k_means_image_clustering.py
   ```

---

## Example Output
1. **Clustered Images:**  
   The program outputs images clustered with different values of k (e.g., 2, 3, 6, 10).  
   Each clustered image will display the visual changes resulting from reducing the image colors into the specified number of clusters.

2. **Final SSE Values:**  
   The program calculates the Sum of Squared Errors (SSE) for each k value and prints it:
   ```
   Final SSE for k=2: 123.45
   Final SSE for k=3: 98.76
   ...
   ```

---

## Customizing the Number of Clusters
You can adjust the `initial_centroids` dictionary in the code to add or modify the number of clusters (k) and their initial centroids.

---

## Notes
- The image path must point to a valid image file. Ensure the file exists at the specified path.
- For larger images, processing time may increase due to the iterative clustering process.

---

## Contact
For any issues or questions, feel free to open an issue in this repository.
