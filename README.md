# Image Processing with Python (Milestone-Based Project)

This project is part of a milestone-based assignment that uses Python to perform basic image processing tasks such as opening, displaying, and saving image files using the PIL (Python Imaging Library).

## Overview

The project is divided into three key milestones:

### ✅ Milestone 1 
- Wrote helper functions in Python.
- Learned function-based code structure.
- Created a greeting function to interact with the user.

### ✅ Milestone 2 
- Read and displayed images using PIL.Image.
- Implemented a function to open and show an image.
- Practiced exception handling for robustness.

### ✅ Milestone 3 
- Saved new image files as copies using img.save().
- Finalized project by integrating all previous parts.
- Worked with multiple image formats (JPG, PNG).

## Example Code

```python
from PIL import Image

def greet_user():
    name = input("Enter your name: ")
    print("Hello, " + name + " welcome to the project.")

def open_and_show_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print("Error opening image:", e)

def save_image_copy(image_path, new_name):
    try:
        img = Image.open(image_path)
        img.save(new_name)
        print("Image saved as:", new_name)
    except Exception as e:
        print("Error saving image:", e)

# Example usage
image_file = r"C:\Users\ASUS\OneDrive\Desktop\project\example.jpg"
open_and_show_image(image_file)
save_image_copy(image_file, "copy_example.jpg")
---

## About the Project

This is a beginner Python image processing project using the Pillow library. It includes:

- Displaying an image
- Saving a new image copy
- Basic exception handling

### Tech Used:
- Python 3
- Pillow (PIL)

### How to Run:
1. Install Pillow: pip install Pillow
2. Run the file: python project.py

### Output:
![Output](copy_example.jpg)
