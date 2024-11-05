# Install PaddleOCR and dependencies
# pip install paddlepaddle paddleocr

from paddleocr import PaddleOCR, draw_ocr
import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = 'path_to_your_image.jpg'
image = cv2.imread('./Capture.PNG')

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Perform OCR
result = ocr.ocr(image_path, cls=True)

# Print the OCR results
for line in result:
    print(line)

# Optional: Visualize the results
boxes = [elements[0] for elements in result[0]]
txts = [elements[1][0] for elements in result[0]]
scores = [elements[1][1] for elements in result[0]]

# Draw results on the image
im_show = draw_ocr(image, boxes, txts, scores, font_path='path_to_your_font.ttf')
im_show = cv2.cvtColor(im_show, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(im_show)
plt.axis('off')
plt.show()