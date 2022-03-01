# Chest_XRay_PneumoniaClassification
CAP 5516 Assignment #1, binary classification of pneumonia cases in chest x-rays, Kaggle competition


This code utilizes Pytorch and multiple other packages that need to be installed.

To run the code, the user simply needs to run the train.py python file*.
  - In the command line, navigate to the appropriate directory, then type "python train.py". Or, run from a programming environment like PyCharm.
  - Starting at line #397, the command line argument parser is found in train.py. The user can either chose to change these default values or use the appropriate commands while running.
  - Example: to change the batch size from default 32 to 16, type "python train.py -b 16"


*NOTE: the dataset is not included in this GitHub repository. It needs to be installed from: https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia. The --data-path command line argument needs to point to your personal install location.
