#simple function to rename images(.jpg,.png.) from 0 to the number of images-1.
# using typer library to run code from command line.

import os
import typer

app = typer.Typer()


@app.command()
def rename_images(directory):
    for path ,dirs ,files in os.walk(directory):
        for index ,filename in enumerate(files):

            if filename.endswith(".jpg") or filename.endswith(".png"):
                file_extention = filename.split('.')[-1]
                # Modify the filename as desired 
                new_filename = f"{index}.{file_extention}"
                old_path = os.path.join(directory, filename)
                  
                new_path = os.path.join(directory, new_filename)
                os.rename(old_path, new_path)
    print("all file renamed")

if __name__=="__main__":
    app()

