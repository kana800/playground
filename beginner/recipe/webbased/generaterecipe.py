"""
 * This script will generate recipe.html file inside the recipes folder
 * The script will read the 'recipe.json' file and add all the information
 * to the recipe.html.
 * 'recipetemplate.html' will be used as the template. After the recipe app is
 * generated it will be linked in the index html file. 
"""
from os.path import isfile, join, exists
from os import listdir
from shutil import copyfile
import json

# location of the src recipetemplate.html
src = "recipetemplate.html"
# location of all the recipes
recipes = "recipesjson"

def readDirectory(directoryname):
    """
    return:
        list of files inside the
        directory
    args:
        directoryname -> name of the
        directory
    """
    return [f for f in listdir(directoryname) if isfile(join(directoryname,f))]

def createFile(src, filename):
    """
    return:
        Boolean
    args: 
        filename -> name of the file
        src -> location of the source file
    summary:
        copy recipetemplate.html 'recipe_filename.html' 
    """
    destinationfilename = f"{filename.split('.')[0]}.html"
    try:
        if not exists(join("recipehtml",destinationfilename)):
            copyfile(src, join("recipehtml",destinationfilename))
        return True
    except Exception as e:
        print(e)
        return False

def main(src, recipes):
    """
    return;
    args:
        src -> recipetemplate.html location
        recipes -> recipejson folder location
    summary:
        main loop of the program generates recipetemplate for
        particular recipe.
        scans the whole folder.   
    """
    recipelist = readDirectory(recipes)
    htmllist = readDirectory("recipehtml")
    # iteration through the recipelist and 
    # check against the html list
    for recipe in recipelist:
        recipenameinhtmlfolder = f"{recipe.split('.')[0]}.html"
        if recipenameinhtmlfolder not in htmllist:
            createFile(src,recipe)

if __name__ == "__main__":
    main(src, recipes)