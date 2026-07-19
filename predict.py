import os
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

model = load_model("model/plant_model.keras")

# Read folder names automatically
classes = sorted([
    folder for folder in os.listdir("dataset/train")
    if os.path.isdir(os.path.join("dataset/train", folder))
])

print(classes)

def predict(image):

    image = image.convert("RGB")

    image = image.resize((224,224))

    image = np.array(image)/255.0

    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image, verbose=0)

    index = np.argmax(prediction)

    confidence = float(prediction[0][index])

    disease = classes[index]

    return disease, confidence