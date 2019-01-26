from keras.applications.vgg19 import VGG19
from keras.preprocessing import image
from keras.applications.vgg19 import preprocess_input
from keras.models import Model
import numpy as np
from scipy import spatial
import pandas as pd
from pymongo import MongoClient


client = MongoClient()
client = MongoClient('mongodb://localhost:27017')

def get_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    flatten = model.predict(x)
    return list(flatten[0])

base_model = VGG19(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('flatten').output)

risdb = client["RIS"]
shoesdata = risdb["ShoesFeatures"]

raw_data = pd.read_csv('../Data Collection/raw_data.csv')


for index, row in raw_data.iterrows():
    print(index)
    name = row["Name"]
    image_url = row["Image URL"]
    image_name = row["Image Name"]

    image_features = get_features('../Data Collection/' + image_name)
    image_features = ['{:.5f}'.format(x) for x in image_features]
    mydict = { "name": name, "image_url": image_url,
               "image_name": image_name, "image_features":image_features }

    shoesdata.insert(mydict)
