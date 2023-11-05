import glob
import cv2
# import the modules
import os
from os import listdir



#read all images from folder



images = [cv2.imread(file) for file in glob.glob("imgs/*.jpg")]
cv2.imshow('img',images[0])
cv2.waitKey(0)
cv2.destroyAllWindows()



#read logo 
#put logo on all images 
#put all newimages in new file



def read_images_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            print(image_path)
            image = cv2.imread(image_path)
            if image is not None:
                images.append(image)
                cv2.imshow("img",image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
    return images

def write_images_to_directory(images, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    for i, image in enumerate(images):
        output_path = os.path.join(output_directory, f"image_{i}.jpg")
        cv2.imwrite(output_path, image)

# Example usage
input_directory = "imgs/"
output_directory = "/path/to/output/directory"

# Read images from input directory
images = read_images_from_directory(input_directory)

# Process the images (e.g., apply filters, perform object detection, etc.)

# Write processed images to output directory
# write_images_to_directory(images, output_directory)