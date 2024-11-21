
# Single Link Clustering

## Overview
This Python program implements the single-link clustering algorithm. It processes a list of numeric data points, calculates pairwise distances, and performs hierarchical clustering using the single-linkage method. The program outputs:
- A distance matrix
- Clustering steps
- Minimum distances for merging clusters

---

## Requirements
- **Python Version:** 3.7 or later
- **Required Libraries:**
  - `numpy`
  - `pandas`

### Install Dependencies
To install the required libraries, run:
```bash
pip install numpy pandas
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

3. **Run the Program**  
   Execute the script using Python:
   ```bash
   python single_link_clustering.py
   ```

---

## Example Input and Output

### **Input Data**
The program uses this dataset by default:
```python
data = [0, 4, 5, 20, 25, 39, 43, 44]
```

### **Output**

1. **Distance Matrix:**  
   A symmetric matrix showing pairwise distances between points:
   ```
       0     4     5    20    25    39    43    44
   0   0.0   4.0   5.0  20.0  25.0  39.0  43.0  44.0
   4   4.0   0.0   1.0  16.0  21.0  35.0  39.0  40.0
   5   5.0   1.0   0.0  15.0  20.0  34.0  38.0  39.0
   20 20.0  16.0  15.0   0.0   5.0  19.0  23.0  24.0
   25 25.0  21.0  20.0   5.0   0.0  14.0  18.0  19.0
   39 39.0  35.0  34.0  19.0  14.0   0.0   4.0   5.0
   43 43.0  39.0  38.0  23.0  18.0   4.0   0.0   1.0
   44 44.0  40.0  39.0  24.0  19.0   5.0   1.0   0.0
   ```

2. **Clustering Steps:**  
   The program outputs the clusters and the minimum distance used to merge them after each step:
   ```
   Clusters:
    [[0, 4, 5], [20], [25], [39], [43, 44]]
   Min Distance: 1.0

   Clusters:
    [[0, 4, 5], [20, 25], [39], [43, 44]]
   Min Distance: 5.0

   ...
   ```

---

## Customizing the Data
To process a different dataset:
1. Open the `single_link_clustering.py` file.
2. Modify the `data` variable to include your dataset:
   ```python
   data = [list of numeric values]
   ```
3. Run the program as described in the **How to Use** section.

---

## Contact
For any issues or questions, feel free to open an issue in this repository.
