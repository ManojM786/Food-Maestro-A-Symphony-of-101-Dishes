# Food Maestro: A Symphony of 101 Dishes

Food Maestro is a deep learning project focused on classifying images from the Food-101 dataset into 101 food categories. The goal is to build an effective food image classifier using state-of-the-art techniques in computer vision with PyTorch. This project demonstrates the application of deep learning for real-world image classification challenges.

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This repository contains code for training, validating, and evaluating a Convolutional Neural Network (CNN) that classifies food images. The project leverages PyTorch for model development and uses various Python libraries for data handling, visualization, and performance tracking. It is designed to be modular so that you can experiment with different architectures and training strategies.

## Repository Structure

Below is an overview of the key files and directories in the repository:


Food-Maestro-A-Symphony-of-101-Dishes/ │ ├── data/
│ └── [Optional scripts or instructions for dataset handling] │ ├── models/
│ └── model.py # Contains the CNN architecture definition │ ├── notebooks/
│ └── EDA.ipynb # Jupyter Notebook for exploratory data analysis and visualization │ ├── scripts/
│ ├── train.py # Script to train the food image classifier │ └── evaluate.py # Script to evaluate the trained model and generate metrics │ ├── results/
│ └── [Output files such as accuracy plots, confusion matrices, etc.] │ ├── requirements.txt # Python dependencies ├── LICENSE # License file (if provided) └── README.md # This file

*Note:* If any folders or files have different names or if additional scripts are present, update this section accordingly.

## Installation

### Prerequisites

- Python 3.7 or higher
- Git

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ManojM786/Food-Maestro-A-Symphony-of-101-Dishes.git
   cd Food-Maestro-A-Symphony-of-101-Dishes
2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **Dataset Setup**

Download the Food-101 dataset and follow any instructions provided in the data/ folder (if applicable). Ensure that the dataset path is correctly configured in the training and evaluation scripts.

**Usage**
**Training the Model**
To train the model, run the training script. You can adjust hyperparameters such as epochs, batch size, and learning rate as needed.

   ```bash
   python going_modular/train.py --epochs 25 --batch_size 32 --learning_rate 0.001
```


**Results**
The model has achieved competitive accuracy on the Food-101 test set. Detailed performance metrics, plots, and confusion matrices can be found in the results/ directory. (Update this section with actual performance numbers and insights after running the evaluation.)


**Dependencies**
Major libraries used in this project include:

PyTorch
Torchvision
Scikit-Learn
Other dependencies are listed in requirements.txt


**Contributing**
Contributions to improve this project are welcome. To contribute:

1.Fork the repository.
2.Create a feature branch (git checkout -b feature-branch).
3.Commit your changes (git commit -m 'Add new feature').
4.Push to the branch (git push origin feature-branch).
5.Open a pull request.


For major changes, please open an issue first to discuss what you would like to change.


**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Contact**
For any questions or feedback, please contact manojdatascientist7@gmail.com.
