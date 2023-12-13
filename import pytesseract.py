import pytesseract
import cv2

# 이미지 파일 경로 리스트
image_paths = [
    'C:/ocr/output_image_4_days.jpg',
    'C:/ocr/output_image_4_numb.jpg',
    'C:/ocr/output_image_3_days.jpg',
    'C:/ocr/output_image_3_numb.jpg',
    'C:/ocr/output_image_2_days.jpg',
    'C:/ocr/output_image_2_numb.jpg',
    'C:/ocr/output_image_1_days.jpg',
    'C:/ocr/output_image_1_numb.jpg',
]

# 각 이미지 파일에 대해 반복
for image_path in image_paths:
    output_path = image_path.replace('.jpg', '_output_text.txt')

    # 이미지를 그레이스케일로 불러옴
    image = cv2.imread(image_path, 0)

    # 이미지에 Thresholding 적용
    _, thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 이미지에서 텍스트 추출
    text = pytesseract.image_to_string(thresholded, config="--psm 13")

    # 추출된 텍스트를 파일에 저장
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text)