#importing helpful libraries
import os
import os.path
import shutil

#defining useful functions
def get_all_txt_files(path = "."):
    """This function walks through the subdirectories of the given path and returns a list of all
    the text file directories nested in this path as well as text files within the initial directory"""
    AllFiles = list(os.walk(path)) #getting all files into a data structure
    all_txt_files = []
    file_list = []

    for dir_tuple in AllFiles:
        file_list = dir_tuple[2]
        for file_name in file_list:
            if file_name[-3:] == 'txt':
                all_txt_files.append(dir_tuple[0]+'/'+file_name)
    return all_txt_files

def sweet_or_savory(path = '.'):
    """
    Input:
    path - this is the directory the function will sift through

    Outputs:
    sweet_list - this is a list of paths for sweet pie recipes
    savory_list - this is a list of paths for savory pie recipes
    mystery_list - this is a list of paths for recipes that could be sweet or savory

    This function iterates through all of the recipes in the given directory and
    nested subdirectories. It organizes the recipes accordingly"""
    all_txt_files = get_all_txt_files(path)
    sweet_words = ['sweet']
    savory_words = ['savory']

    sweet_list = []
    savory_list = []
    mystery_list = []

    for recipe in all_txt_files:
        f = open(recipe,'r',encoding = 'latin1')
        contents = f.read()
        lower_key_words = contents.lower()
        key_words_list = lower_key_words.split()
        if any(x in sweet_words for x in key_words_list):
            sweet_list.append(recipe)
        elif any(x in savory_words for x in key_words_list):
            savory_list.append(recipe)
        else:
            mystery_list.append(recipe)

    return sweet_list, savory_list, mystery_list

def organize_sweet_savory(sweet_list,savory_list,path='.'):
    """
    Inputs:
    sweet_list - list of directories for sweet pie recipes
    savory_list - list of directories for savory pie recipes
    path - directory to organize

    Outputs:
    None

    This function goes organizes all of the sweet and savory pie recipes into
    respective subdirectories sweet_pie_recipes and savory_pie_recipes
    """
    if os.path.exists('./sweet_pie_recipes') == False:
        os.mkdir('./sweet_pie_recipes')
    if os.path.exists('./savory_pie_recipes') == False:
        os.mkdir('./savory_pie_recipes')

    for recipe in sweet_list:
        shutil.copyfile(recipe,'./sweet_pie_recipes'+"/"+recipe.split("/")[-1])
    for recipe in savory_list:
        shutil.copyfile(recipe,'./savory_pie_recipes'+"/"+recipe.split("/")[-1])

def main():
    """This is the main function that runs all relevant code to organize all
    of the pies by sweet or savory to their respective folders."""
    list_tuple = sweet_or_savory()
    organize_sweet_savory(list_tuple[0],list_tuple[1])

if __name__ == "__main__":
    main()
