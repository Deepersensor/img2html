# extract_text.py

from paddleocr import PaddleOCR

def main():
    # Initialize PaddleOCR with English language support
    ocr = PaddleOCR(use_angle_cls=True, lang='en')

    # Path to your image file
    img_path = 'image.jpeg'  # Replace with your image path

    # Perform OCR on the image
    result = ocr.ocr(img_path, cls=True)

    # Print the result for debugging
    print("OCR Result:")
    for line in result:
        print(line)

    # Check if any text was found
    if not result:
        print("No text found in the image.")
        return

    # Open the output file
    with open('out.txt', 'w', encoding='utf-8') as f:
        # Iterate over each detected text line
        for line in result:
            # Depending on the structure, you may need to adjust how you extract 'text'
            # Let's try to extract 'text' properly
            # Print line[1] to see its content
            print("line[1]:", line[1])

            # Extract the recognized text
            if isinstance(line[1], tuple) or isinstance(line[1], list):
                # For cases where line[1] is a tuple like ('recognized text', confidence)
                text = line[1][0]
            elif isinstance(line[1], str):
                # For cases where line[1] is already the text
                text = line[1]
            else:
                # Handle unexpected structures
                text = ''.join(line[1])

            # Ensure 'text' is a string
            if isinstance(text, list):
                text = ' '.join(text)

            f.write(text + '\n')

    print("Text extracted and saved to out.txt")

if __name__ == "__main__":
    main()