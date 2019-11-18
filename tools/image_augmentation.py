from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np


class ImageAugmentation:
    def __init__(self, image, output, total=10):
        self.image = image
        self.output = output
        self.total = total
        self.aug = ImageDataGenerator(
            rotation_range=30,
            zoom_range=0.15,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.15,
            horizontal_flip=True,
            fill_mode="nearest")
        print("[INFO] loading "+self.image)
        self.image = load_img(self.image)
        self.image = img_to_array(self.image)
        self.image = np.expand_dims(self.image, axis=0)

    def generate(self):
        total = 0
        # construct the actual Python generator
        print("[INFO] generating images...")
        imageGen = self.aug.flow(self.image, batch_size=1, save_to_dir=self.output,
            save_prefix="image", save_format="jpg")

        # loop over examples from our image data augmentation generator
        for self.image in imageGen:
            # increment our counter
            total += 1

            # if we have reached the specified number of examples, break
            # from the loop
            if total == self.total:
                break



ig = ImageAugmentation('anuj.png', 'generated')
ig.generate()

# USAGE
# python generate_images.py --image dog.jpg --output generated_dataset/dogs
# python generate_images.py --image cat.jpg --output generated_dataset/cats

