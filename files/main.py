__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Assignment: Files

import os
import zipfile


"""1: the function clean_cache, makes a folder named "cache" in
the current directory, in case it not already existed. O
teherwise it will emty the already existing folder 'cache' """


def clean_cache():
    current_dir_path = os.path.dirname(__file__)
    folder_path = os.path.join(current_dir_path, "cache")
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    elif os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            file_name = os.path.join(folder_path, file)
            os.remove(file_name)


""" 2: the function cache_zip calls the function clean_cache to make sure
the folder cache exists and is empty. Then ZipFile will read the zip file 
and unzips all files in the cache folder """


def cache_zip(zip_file_path, cache_dir_path):
    clean_cache()
    with zipfile.ZipFile(zip_file_path) as zip_file:
        zip_file.extractall(cache_dir_path)


""" 3: cached_files returns a list of the absolute paths of all the files in
the folder 'cache'. First it determines for every file (no folders) in the
folder'cache' the absolute path and adds it to the list that is retured. """


def cached_files():
    current_dir_path = os.path.dirname(__file__)
    cache_folder_path = os.path.join(current_dir_path, "cache")
    file_list = []
    for file in os.listdir(cache_folder_path):
        file_path_absolute = os.path.join(cache_folder_path, file)
        if os.path.isfile(file_path_absolute):
            file_list.append(file_path_absolute)
    return file_list


""" 4: The function find_password return password in the cached files list.
Every file in cached_files gets read and every line in the the file gets
checked for the word 'password'. Then the line gets sliced and stripped of
every whitespace. """


def find_password(cached_files):
    for file in cached_files:
        file_content = open(file, "r")
        for line in file_content.readlines():
            if "password" in line:
                return line[line.find(" "):].strip()