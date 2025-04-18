print("project started")

def greet_user():
    name = input("enter your name:")
    print("hello, " + name + "welcome to the project.")
greet_user()

from PIL import Image  # Import the image library

def open_and_show_image(image_path):
    try:
        img = Image.open(image_path)  # Open the image
        img.show()  # Show the image
    except Exception as e:
        print("Error opening image:", e)

def save_image_copy(image_path, new_name):
    try:
        img = Image.open(image_path)  # Open the image
        img.save(new_name)  # Save as a new file
        print("Image saved as:", new_name)
    except Exception as e:
        print("Error saving image:", e)

# Example usage:
image_file = r"C:\Users\ASUS\OneDrive\Desktop\project\example.jpg.jpg"  # Change this to your image file name
open_and_show_image(image_file)
save_image_copy(image_file, "copy_example.jpg")
