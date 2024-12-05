import tensorflow as tf
from tensorflow import keras

img_height = 128
img_width = 128
batch_size = 32
epochs = 10
import tensorflow as tf
from tensorflow import keras

img_height = 128
img_width = 128
batch_size = 32
epochs = 10

def create_model(img_height=128, img_width=128):
  model = keras.Sequential([
  keras.layers.Input(input_shape=(img_height, img_width, 3)),
  keras.layers.Rescaling(1./255),

  keras.layers.RandomFlip('horizontal'),
  keras.layers.RandomRotation(0.2),
  keras.layers.RandomZoom(0.2),

  keras.layers.Conv2D(32, (3, 3), activation='relu'),
  keras.layers.MaxPooling2D(),

  keras.layers.Conv2D(64, (3, 3), activation='relu'),
  keras.layers.MaxPooling2D(),

  keras.layers.Conv2D(128, (3, 3), activation='relu'),
  keras.layers.MaxPooling2D(),

  keras.layers.Flatten(),
  keras.layers.Dense(128, activation='relu'),
  keras.layers.Dense(1, activation='sigmoid'),
])
  
  model.compile(
  optimizer='adam',
  loss='binary_crossentropy',
  metrics=['accuracy']
)
  
  model.summary()