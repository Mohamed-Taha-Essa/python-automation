import glob
import cv2
# import the modules
import os
from os import listdir
import typer

app =typer.Typer()


@app.command()
def add_logo_to_image(directory_of_img ,name_new_directory,logo_name):
    os.makedirs(name_new_directory ,exist_ok=True)

    #read all images from folder
    images = [cv2.imread(file) for file in glob.glob(f"{directory_of_img}/*.jpg")]
    #read logo 
    logo =cv2.imread(logo_name)
        
    # Determine the region of interest (ROI)
    rows, cols, channels = logo.shape
    for index,img in enumerate(images):
        if img.any() ==None:
            print("none")
            break
        roi = img[0:rows, 0:cols]
        # Convert the logo to grayscale
        logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
        #put logo on image 

        dst=cv2.addWeighted(logo,.5,roi,.5,0 ) 
        name =f"{index}.jpg"
        path =os.path.join(name_new_directory,name)
        print(name)
        # Replace the ROI with the combined image
        img[0:rows, 0:cols] = dst
        cv2.imwrite(path,img)

 
if __name__ =="__main__":
    app()
#put all newimages in new file

