import cv2


def extract_images(image_path, rows, cols, ignore_last_row_cols):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Cannot load the image from {image_path}")
        return []

    total_height, total_width = img.shape[:2]
    img_width = total_width // cols
    img_height = total_height // rows

    extracted_images = []

    for row in range(rows):
        for col in range(cols):
            if row == rows - 1 and col in ignore_last_row_cols:
                continue

            x = col * img_width
            y = row * img_height
            cropped_img = img[y : y + img_height, x : x + img_width]
            extracted_images.append(cropped_img)

    return extracted_images
