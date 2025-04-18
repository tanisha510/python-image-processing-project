from PIL import Image, ImageDraw

print("Project started")

def greet_user():
    name = input("Enter your name: ")
    print("Hello, " + name + ", welcome to the project.")

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

def render_image_in_circle_and_square(image_path):
    try:
        original_image = Image.open(image_path).convert("RGBA")
        
        # Create a square image (just a copy of the original)
        square_image = Image.new("RGBA", original_image.size)
        square_image.paste(original_image, (0, 0))
        
        # Create a circular mask
        circle_mask = Image.new("L", original_image.size, 0)
        draw = ImageDraw.Draw(circle_mask)
        width, height = original_image.size
        draw.ellipse((0, 0, width, height), fill=255)
        
        # Apply the circular mask to the original image
        circle_image = Image.new("RGBA", original_image.size)
        circle_image.paste(original_image, (0, 0), mask=circle_mask)
        
        # Save the images
        circle_image.save("circle_image.png")
        square_image.save("square_image.png")
        print("Images saved as 'circle_image.png' and 'square_image.png'")
        
    except Exception as e:
        print("Error processing image:", e)

# Main execution
greet_user()
image_file = r"C:\Users\ASUS\OneDrive\Desktop\project\example.jpg.jpg"

open_and_show_image(image_file)
save_image_copy(image_file, "copy_example.jpg")
render_image_in_circle_and_square(image_file)
