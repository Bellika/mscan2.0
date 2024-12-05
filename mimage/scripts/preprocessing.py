import tensorflow as tf
tf.config.set_visible_devices([], 'GPU')
from tensorflow import keras

img_height = 128
img_width = 128
batch_size = 32

train_dataset = tf.keras.utils.image_dataset_from_directory(
  './data/train',
  image_size=(img_height, img_width),
  batch_size=batch_size,
  label_mode='binary' 
)

val_dataset = tf.keras.utils.image_dataset_from_directory(
  './data/validate',
  image_size=(img_height, img_width),
  batch_size=batch_size,
  label_mode='binary'
)

test_dataset = tf.keras.utils.image_dataset_from_directory(
  './data/test',
  image_size=(img_height, img_width),
  batch_size=batch_size,
  label_mode='binary'
)

# normalize changes the pixel value to be between 0 - 1 instead of 0 - 255
def normalize(image, label):
  image = tf.cast(image, tf.float32) / 255.0
  return image, label

train_dataset = train_dataset.map(normalize)
val_dataset = val_dataset.map(normalize)
test_dataset = test_dataset.map(normalize)

data_augmentation = keras.Sequential([
  keras.layers.RandomFlip('horizontal'),
  keras.layers.RandomRotation(0.2),
  keras.layers.RandomZoom(0.2),
  keras.layers.RandomHeight(0.2),
  keras.layers.RandomWidth(0.2),
])