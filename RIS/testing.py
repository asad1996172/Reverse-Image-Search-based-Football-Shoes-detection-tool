from scipy import spatial
from pymongo import MongoClient
from PIL import Image

client = MongoClient()
client = MongoClient('mongodb://localhost:27017')
db = client.RIS
collection = db.ShoesFeatures

cursor = collection.find({})
image_to_test = cursor[10]
im = Image.open("../Data Collection/" + image_to_test["image_name"])

list_of_tuples = []
for document in cursor:
    features = [float(i) for i in document["image_features"]]
    gold = [float(i) for i in image_to_test["image_features"]]

    result = 1 - spatial.distance.cosine(gold, features)
    list_of_tuples.append((document["image_name"], result))

list_of_tuples.sort(key=lambda tup: tup[1])  # sorts in place

most_sim1, similarity1 = list_of_tuples[-2]
most_sim2, similarity2 = list_of_tuples[-3]
most_sim3, similarity3 = list_of_tuples[-4]
most_sim4, similarity4 = list_of_tuples[-5]

im1 = Image.open("../Data Collection/" + most_sim1)
im2 = Image.open("../Data Collection/" + most_sim2)
im3 = Image.open("../Data Collection/" + most_sim3)
im4 = Image.open("../Data Collection/" + most_sim4)

im.show(title="Query Image")
im1.show()
im2.show()
im3.show()
im4.show()
