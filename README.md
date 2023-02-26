# Handwritten Digit Classifier - RAP ASSIGNMENT
The model is trained using CNN by MNIST toy dataset in the Tensorflow framework,The dataset was normalised from (0-255) to (0.0-1.0).To classify the digit, a model with three convolutional layers, 64 filters, and a 3,3 kernal size was created.The layer was then flattened and given to the fully connected layer. The L2 Regularization, Drop Outing layers, and Batch normailzation are used to combat overfitting that occurred during the training phase of the model. In the end of the training saved as H5 format,Then Flask Web server was built with user-interface for uploading images will saved in  MongoDB collection. Then Image from MongoDb is retrived and preprocessed using OpenCV and resized.Then image is passed to the trained model, Finally the output from model showed in frontend. Hosted in AWS EC2 (link is provided below).

Accuracy of model: 98%
Validation Accuaracy : 97.2%.
## Hosted Link:
## [Click here to view application](https://bit.ly/vs-rap)

## Model Architecture
![model](https://i.postimg.cc/6QpX2PMC/image.png)
## Pages:
Home page:![1](https://i.postimg.cc/YSJYVyss/78eb3e1e-fba8-4178-a9b5-2d0a750a91d7.jpg)
Image Selection Area: ![2](https://i.postimg.cc/v8vxLBbj/51c9c7de-1b81-4c95-9718-7061fc74ea9e.jpg)
Image Preview: ![2](https://i.postimg.cc/nVdchQHH/0990896c-cd76-4a4f-8a63-3bc988185acf.jpg)
Predicated Result Page: ![2](https://i.postimg.cc/GhYNSZgZ/3ea2bce0-6015-40ff-bfea-42642149c67d.jpg)
About Page:![2](https://i.postimg.cc/RZ4PpqHH/0b865ac7-090d-4f1c-a121-92ba1e42c73d.jpg)
About Us Page![2](https://i.postimg.cc/vmDtCnHc/adef91e9-a98a-4093-a39f-86f1f406e477.jpg)
MongoDB Cluster:![1](https://i.postimg.cc/JhY6m8Dd/b47c3e9e-982e-49fd-bca1-2e9109098849.jpg)
AWS EC2 instance:![1](https://i.postimg.cc/9QZCrxtp/image.png)
## Technologies & Framework Used:
* Python ( Flask, Tensorflow, OpenCV, Pymongo, Numpy )
* MongoDb 
* AWS EC2

## Contributors

1. [VENKAT P R](https://www.linkedin.com/in/venkat-p-r/)
2. [SRIRANGAN K](https://www.linkedin.com/in/srirangank)

