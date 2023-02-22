# Handwritten Digit Classifier - RAP ASSIGNMENT

Trained the model using CNN by MNIST toy dataset in Tensorflow Framwork, Normalized dataset to 0 to 255 into 0.0 to 1.0. Created the model 3 Convolutional layer 64 filters and 3,3 kernal size and flatten the layer give that to the full connected layer ,Finally 10 neuron of full connected layer with softmax activation to classify the digit.
During the training model goes to overfit ,to overcome this Performed the L2 Regularization , Dropouting th layers and Batchnormailzation. After that saved model in H5 format and Creted Flask Web server provided basic UI for uploading images that will saved as temporary file and that file path given to server as input then image preprocesssed using OPENCV. In preprocessing converting rgb to grayscale then resized the image into 28x28px then the image file given to trained model it predict the value that displayed in Frontend.
Accuracy of model: 98%
Validation Accuaracy : 97.2%
## Hosted Link:
[Click here to view application](#)
## Model Architecture
![model](https://i.postimg.cc/6QpX2PMC/image.png)
## Results:
![1](https://i.postimg.cc/W16NJgTc/Whats-App-Image-2023-02-22-at-14-16-44.jpg)
![2](https://i.postimg.cc/8PGPkZgm/Whats-App-Image-2023-02-22-at-14-20-01.jpg)
![2](https://i.postimg.cc/V6yPGNYW/Whats-App-Image-2023-02-22-at-14-17-06.jpg)


## Installation
Python3
flask 
tensorflow 
numpy
opencv-python
Pillow

## Contributing

1. [VENKAT P R](https://www.linkedin.com/in/venkat-p-r/)
2. [SRIRANGAN K](https://www.linkedin.com/in/srirangank)