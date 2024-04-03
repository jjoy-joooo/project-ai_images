import cv2


def concatenate_images(images):
    if not images:
        print("No images to concatenate.")
        return None

    max_height = max(img.shape[0] for img in images)
    resized_images = [
        cv2.resize(
            img,
            (int(img.shape[1] * max_height / img.shape[0]), max_height),
            interpolation=cv2.INTER_AREA,
        )
        for img in images
    ]
    concatenated_image = cv2.hconcat(resized_images)
    return concatenated_image
