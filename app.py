from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import cv2 as cv
from PIL import Image
import base64
import pymongo
from io import BytesIO

app = Flask(__name__)

connection_string = "mongodb+srv://rap:rap@cluster0.3iayb.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)

# Access a database and collection
db = client.RapAssignment
collection = db.image
# Load your machine learning model here
model = tf.keras.models.load_model('./handwritten10-epoch.model')

# Define a route for the upload form
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    image_file = request.files['rapidvs']
    if image_file:
       
        image_data = image_file.read()
        image_doc = {"image": base64.b64encode(image_data).decode()}
 
        image_id = collection.insert_one(image_doc).inserted_id
     
        image_loc = collection.find_one({"_id":image_id})
        if image_loc is not None and "image" in image_loc:
        
            nparr = np.frombuffer(base64.b64decode(image_loc["image"]), np.uint8)
            img = cv.imdecode(nparr, cv.IMREAD_COLOR)
            resized = cv.resize(cv.cvtColor(img,cv.COLOR_BGR2GRAY),(28,28),interpolation = cv.INTER_AREA)
            newimg = np.array(tf.keras.utils.normalize(resized,axis= 1)).reshape(-1,28,28,1)
            predictions = model.predict(newimg)
            # Make a prediction using the model
            pred = np.argmax(predictions)
          
            return render_template('success.html', prediction=pred)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/aboutus')
def about_us():
    return render_template('about_us.html')

if __name__ == '__main__':
    app.run(debug=True)
