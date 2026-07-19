import os
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

IMG_SIZE = 224

train = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_data = train.flow_from_directory(
    "dataset/train",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=32,
    class_mode="categorical",
    subset="training",
    shuffle=True
)

val_data = train.flow_from_directory(
    "dataset/train",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=32,
    class_mode="categorical",
    subset="validation",
    shuffle=False
)

print("\nClasses:")
print(train_data.class_indices)

base = MobileNetV2(
    include_top=False,
    weights="imagenet",
    input_shape=(224,224,3)
)

base.trainable = False

model = Sequential([
    base,
    GlobalAveragePooling2D(),
    Dropout(0.3),
    Dense(train_data.num_classes, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    train_data,
    validation_data=val_data,
    epochs=5
)

os.makedirs("model", exist_ok=True)

model.save("model/plant_model.keras")

print("\nTraining Complete!")
print("Model Saved Successfully")