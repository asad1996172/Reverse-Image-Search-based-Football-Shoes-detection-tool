from keras.applications.vgg19 import VGG19
from keras.preprocessing import image
from keras.applications.vgg19 import preprocess_input
from keras.models import Model
import numpy as np
from scipy import spatial

def get_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    flatten = model.predict(x)
    return flatten

base_model = VGG19(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('flatten').output)

# img_path = '../Data Collection/Football Shoes Images/1.jpg'

sim = 1 - spatial.distance.cosine(get_features('../Data Collection/Football Shoes Images/3.jpg'),
                                  get_features('../Data Collection/Football Shoes Images/5.jpg'))
print(sim)