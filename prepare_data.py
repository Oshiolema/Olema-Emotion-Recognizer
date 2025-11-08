import os
import random
import shutil

# Path to your dataset folder
DATASET_DIR = "fer2013"
TRAIN_DIR = os.path.join(DATASET_DIR, "train")
VALIDATION_DIR = os.path.join(DATASET_DIR, "validation")

# Create the validation folder if it doesn't exist
os.makedirs(VALIDATION_DIR, exist_ok=True)

# Set what % of training images should move to validation (e.g., 15%)
VAL_SPLIT = 0.15

for emotion_class in os.listdir(TRAIN_DIR):
    class_train_dir = os.path.join(TRAIN_DIR, emotion_class)
    class_val_dir = os.path.join(VALIDATION_DIR, emotion_class)

    # Make sure we’re only looking at folders (not stray files)
    if not os.path.isdir(class_train_dir):
        continue

    os.makedirs(class_val_dir, exist_ok=True)

    images = os.listdir(class_train_dir)
    num_val = int(len(images) * VAL_SPLIT)
    val_images = random.sample(images, num_val)

    print(f"Moving {num_val} images from {emotion_class} to validation...")

    for img_name in val_images:
        src_path = os.path.join(class_train_dir, img_name)
        dst_path = os.path.join(class_val_dir, img_name)
        shutil.move(src_path, dst_path)

print("\n✅ Validation set created successfully!")
