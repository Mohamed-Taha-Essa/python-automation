import os



#simple function to rename images(.jpg,.png) from 0 to the number of images-1 if the folder imgs is beside the code .
def rename_images(directory):
    for index ,filename in enumerate(os.listdir(directory)):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            file_extention=filename.split('.')[-1]
            new_filename=f"{index}.{file_extention}"
            old_path = os.path.join(directory, filename)
            # new_filename =  filename  # Modify the filename as desired
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
    print("all file renamed")

# the directory of folder cntain images you can change it 
directory ="imgs"
rename_images(directory)


