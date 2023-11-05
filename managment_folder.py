import os
import shutil
import schedule
import glob
import filetype

#declare your path
#path = r'F:\FullStackDev\New folder'


def clean_path(enter_path =False):
    if enter_path:
        clean_path = input('Enter Full Path')
        os.chdir(path =clean_path)

    else :
        os.chdir(path)
    for file in os.listdir('.') :
        kind =filetype.guess(file)
        if('image' in kind.mime):
            os.makedirs("Images", exist_ok=True)
            shutil.move(file ,"Images")
        elif ('video' in kind.mime):
            os.makedirs("Videos", exist_ok=True)
            shutil.move(file, "Videos")
        elif ('audio' in kind.mime):
            os.makedirs("Audio", exist_ok=True)
            shutil.move(file, "Audio")
        elif ('application' in kind.mime):
            #application mean compressed file like .rar ,.zip
            #check the link if you have multible type of files
            #https://pypi.org/project/filetype/
            os.makedirs("application", exist_ok=True)
            shutil.move(file, "application")

clean_path(enter_path=True)
schedule.every(10).seconds.do(clean_path())