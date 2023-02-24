from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import cv2 as cv
from PIL import Image

app = Flask(__name__)

# Load your machine learning model here
model = tf.keras.models.load_model('./handwritten10-epoch.model')

# Define a route for the upload form
@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the uploaded file from the request
        file = request.files['rapidvs']
        # Save the file to a temporary location on the server
        filename = 'temp.jpg'
        file.save(filename)
        # Load the image and preprocess it for the model
        imgpath = Image.open(filename)
        img = cv.imread(filename)
        resized = cv.resize(cv.cvtColor(img,cv.COLOR_BGR2GRAY),(28,28),interpolation = cv.INTER_AREA)
        newimg = np.array(tf.keras.utils.normalize(resized,axis= 1)).reshape(-1,28,28,1)
        predictions = model.predict(newimg)
        # Make a prediction using the model
        pred = np.argmax(predictions)
        # Render an HTML page with the prediction result
        return render_template('success.html', prediction=pred)
    # If the request method is GET, display the upload form
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/aboutus')
def about_us():
    return render_template('about_us.html')

if __name__ == '__main__':
    app.run(debug=True)