import os

import cv2


def save_images(images, output_folder, prefix="extracted"):
    for i, img in enumerate(images):
        filename = os.path.join(output_folder, f"{prefix}_{i}.jpg")
        cv2.imwrite(filename, img)
        print(f"Saved: {filename}")


def save_image(image, output_folder, filename="merge.jpg"):
    filepath = os.path.join(output_folder, filename)
    cv2.imwrite(filepath, image)
    print(f"Saved: {filepath}")
