#simple scripts to add logo to images using pillwo and typer
from PIL import Image,ImageOps
import os
import typer

app =typer.Typer()


@app.command()
def add_logo_to_img(data_folder,logo_name,save_location):
    #read logo 
    logo = Image.open(logo_name)
    logo_w ,logo_h = logo.size

    #creat newlocation to save image on it 
    os.makedirs(save_location,exist_ok=True)

    #Loop over all the .jpeg,.jpg and .png files
    for file in os.listdir(data_folder):
        if not file.endswith(('.jpeg','.jpg','.png')):
            continue
        #open image to know width and height
        im_path =os.path.join(data_folder,file)
        image = Image.open(im_path )
        
        #as image is rotate i make it normal
        image = ImageOps.exif_transpose(image)
        image_w,image_h = image.size

        #put logo on image 
        image.paste(logo,(image_w - logo_w, image_h - logo_h) ,logo)

        #save new image with logo on new location
        image.save(os.path.join(save_location,file))

if __name__ == "__main__":
    app()