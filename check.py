import os 


def walk_the_directory():
    file_list = [(x, y, z) for x, y, z in os.walk('.')]
    for idx, files in enumerate(file_list):
        if idx < 10:
            for file in files[2]:
                print(os.path.join(files[0], file))
        else:
            break 

walk_the_directory()