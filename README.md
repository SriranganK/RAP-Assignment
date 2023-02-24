# Handwritten Digit Classifier - RAP ASSIGNMENT
Trained the model using CNN by MNIST toy dataset in the Tensorflow framework, the model was trained. The dataset was normalised to range from 0.0 to 1.0. To classify the digit, a model with three convolutional layers, 64 filters, and a 3,3 kernal size was created. The layer was then flattened and given to the full connected layer. The L2 Regularization, Drop Outing layers, and Batch normailzation procedures were used to combat overfitting that occurred during the training phase of the model. S  saved in H5 format, Flask Web server was built, and a user interface was provided for uploading images that would be saved as temporary image files. The image was then preprocessed using OpenCV and resized to be 28x28 pixels, and passed to the trained then the output from model showed in frontend. Hosted in AWS EC2 

Accuracy of model: 98%
Validation Accuaracy : 97.2%.
## Hosted Link:
## [Click here to view application](#)
## Model Architecture
![model](https://i.postimg.cc/6QpX2PMC/image.png)
## Pages:
Home page:![1](https://i.postimg.cc/YSJYVyss/78eb3e1e-fba8-4178-a9b5-2d0a750a91d7.jpg)
Image Selection Area: ![2](https://i.postimg.cc/v8vxLBbj/51c9c7de-1b81-4c95-9718-7061fc74ea9e.jpg)
Image Preview: ![2](https://i.postimg.cc/nVdchQHH/0990896c-cd76-4a4f-8a63-3bc988185acf.jpg)
Predicated Result Page: ![2](https://i.postimg.cc/GhYNSZgZ/3ea2bce0-6015-40ff-bfea-42642149c67d.jpg)
About Page:![2](https://i.postimg.cc/RZ4PpqHH/0b865ac7-090d-4f1c-a121-92ba1e42c73d.jpg)
About Us Page![2](https://i.postimg.cc/vmDtCnHc/adef91e9-a98a-4093-a39f-86f1f406e477.jpg)


## Installation Requirements
* Python3
* flask 
* tensorflow 
* numpy
* opencv-python
* Pillow

## Contributors

1. [VENKAT P R](https://www.linkedin.com/in/venkat-p-r/)
2. [SRIRANGAN K](https://www.linkedin.com/in/srirangank)

