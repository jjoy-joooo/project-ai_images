import os

from image_concatenator import concatenate_images
from image_extractor import extract_images
from image_saver import save_image, save_images

# 설정
image_path = "result.jpg"
output_folder = "./data"
rows = 3
cols = 5
ignore_last_row_cols = [1, 2, 3, 4]

# output 폴더 확인 및 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 이미지 분리 및 추출
extracted_images = extract_images(image_path, rows, cols, ignore_last_row_cols)

# 분리된 이미지를 data 폴더에 저장
save_images(extracted_images, output_folder)

# 추출된 이미지들을 한 줄로 이어붙임
final_image = concatenate_images(extracted_images)

# 최종 병합된 이미지 저장
save_image(final_image, output_folder)
