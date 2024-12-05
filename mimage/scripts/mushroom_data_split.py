import os
import shutil
from sklearn.model_selection import train_test_split

source_mushroom = './data/mushroom'
source_not_mushroom = './data/not_mushroom'

base_dirs = ['./data/train', './data/validate', './data/test']
categories = ['mushroom', 'not_mushroom']

for base_dir in base_dirs:
    for category in categories:
        os.makedirs(os.path.join(base_dir, category), exist_ok=True)

def split_and_move_images(source_dir, category):
    all_images = []
    for root, _, files in os.walk(source_dir):
        for file_name in files:
            if file_name.lower().endswith(('.jpg', '.png', '.jpeg')):
                all_images.append(os.path.join(root, file_name))
    train_val, test = train_test_split(all_images, test_size=0.2, random_state=42)
    train, val = train_test_split(train_val, test_size=0.125, random_state=42)
    move_images(train, './data/train', category)
    move_images(val, './data/validate', category)
    move_images(test, './data/test', category)

def move_images(image_list, target_base_dir, category):
    for img_path in image_list:
        target_dir = os.path.join(target_base_dir, category)
        shutil.copy(img_path, os.path.join(target_dir, os.path.basename(img_path)))

split_and_move_images(source_mushroom, 'mushroom')
split_and_move_images(source_not_mushroom, 'not_mushroom')

print("Images has been split.")