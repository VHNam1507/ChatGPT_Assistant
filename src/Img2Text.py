import os
import io
import imghdr
import pytesseract as tess
import numpy as np
from PIL import Image
import cv2

# Function to process image using OpenCV
def process_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    edges = cv2.Canny(blur, threshold1=30, threshold2=100)
    return edges

# Function to check if image file is valid
def is_valid_image(path):
    valid_formats = ['jpeg', 'png', 'bmp', 'gif']
    if imghdr.what(path) in valid_formats:
        return True
    else:
        return False

# Function to remove temp files
def remove_temp_files(*files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)

# Main function for OCR
def image2text():
    with io.open('data/tess_Path.txt', 'r') as f_path:
        tess_path = f_path.read().strip()
    tess.pytesseract.tesseract_cmd = tess_path

    # Prompt user for input file and check validity
    while True:
        input_file = input("Enter path to input file: ")
        if os.path.exists(input_file) and is_valid_image(input_file):
            break
        else:
            print("Invalid file path or format. Please try again.")
    
    # Prompt user for output file and check validity
    while True:
        output_file = input("Enter path to output file: ")
        if os.path.exists(os.path.dirname(output_file)):
            break
        else:
            print("Invalid directory path. Please try again.")
    
    # Process image using OpenCV and save temporary file
    temp_file = 'temp.jpg'
    edges = process_image(input_file)
    cv2.imwrite(temp_file, edges)
    
    # Perform OCR on temporary file and remove temporary files
    try:
        img = Image.open(temp_file)
        text = tess.image_to_string(img)
        text = text.replace('\n', ' ')
        with io.open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write("Result: " + text)
    except Exception as e:
        print("An error occurred during OCR: ", e)
    finally:
        remove_temp_files(temp_file)

# Call main function
if __name__ == '__main__':
    image2text()
