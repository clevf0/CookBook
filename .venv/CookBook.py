import os

def file_exists(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    return os.path.exists(file_path)

#Interface
class CookBook:
    #Declaring folder_path through out the class
    def __init__(self):
        document_path = os.path.join(os.path.expanduser('~'), 'Documents')
        self.dir_path = os.path.join(document_path, "cookbook")
        self.folder_path = dir_path

    def clear(self):
        self.folder_path = self.dir_path

    #function for creating folder
    def createFolder(self, x):
        folder_name = x  # Folder's name
        documents_path = os.path.join(os.path.expanduser('~'), 'Documents')# Document folder
        data_path = os.path.join(documents_path, "cookbook") #File data path on document folder
        self.folder_path = os.path.join(data_path, folder_name)
        try:
            if not os.path.exists(data_path):

                print("File data not found, permission to create file data at ", documents_path," ? (y/n)")
                t = input(">>").lower()
                if t == "y" or t == "yes":
                    os.makedirs(data_path)
                else:
                    print()

            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path)
                print(f"folder {x} is created")
                print()

        except Exception as e:
            print(e)

    #function to create recipe
    def createRecipe(self):
        file_name = input("Enter the name of the recipe: ")
        file_path = os.path.join(self.folder_path, f"{file_name}.txt")
        with open(file_path, 'w') as f:
            print("ENTER 'done' IF FINISH INPUTTING RECIPE")
            while True:
                ingredient = input("Enter the ingredient: ")
                f.write("**INGREDIENT**")
                if ingredient.lower() == "done":
                    break
                else:
                    f.write(ingredient + '\n')

            procedure = input("Do you want to enter procedures(y/n)?")

            if procedure.lower() == "y" or procedure.lower() == "yes":
                f.write("\n\n\n**Procedures** \n\n")
                i = 1
                print("ENTER 'done' IF FINISH INPUTTING PROCEDURES")
                while True:
                    inpp = input(f"{i}. ")
                    if inpp.lower() != "done":
                        f.write(f"{i}. {inpp}\n")
                    else:
                        break
                    i += 1

    #function to view recipie
    def viewRecipe(self, name):
        recipe_name = name + ".txt"
        recipe_path = os.path.join(self.folder_path, recipe_name)
        if file_exists(self.folder_path, recipe_name):
            with open(recipe_path, 'r') as f:
                print(f.read())
                return False
        else:
            print(f"Recipe '{name}' not found in the selected folder.")
            return True

    #function to delete recipe(to be coded)
    def deleteFolder(self, folder_name):
        document_path = os.path.join(os.path.expanduser('~'), 'Documents')
        dir_path = os.path.join(document_path, "cookbook")
        folder_path = os.path.join(dir_path, folder_name)
        if os.path.exists(folder_path):
            os.rmdir(folder_path)
            print(f"Recipe '{folder_name}' deleted successfully!")
            self.folder_path = dir_path
            return False
        else:
            print(f"Recipe '{folder_name}' not found.")
            return True

    def deleteRecipe(self, name):
        recipe_path = os.path.join(self.folder_path, f"{name}.txt")  # Create the full path to the recipe file

        if os.path.exists(recipe_path):
            os.remove(recipe_path)  # Delete the file
            print(f"Recipe '{name}.txt' deleted successfully!")
            return False
        else:
            print(f"Recipe '{name}' not found.")  # Use the correct variable name
            return True

    #function to list recipe created on the folder
    def listFile(self):
        document_path = os.path.join(os.path.expanduser('~'), 'Documents')
        dir_path = os.path.join(document_path, "cookbook")
        files_and_dirs = os.listdir(dir_path)
        i=0
        for i, item in enumerate(files_and_dirs, start= 1):
            i = i+1
            print(f"- {item}")
        if i == 0:
            print("No recipe folder founded, please try creating new folder")
            return True

    def findFolder(self, x):
        document_path = os.path.join(os.path.expanduser('~'), 'Documents')
        try:
            data_path = os.path.join(document_path, "cookbook")
            x = os.path.join(data_path,x)
        except Exception as e:
            print(e)

    def listSelected(self):
        path = self.folder_path
        files_and_dirs = [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]
        i=0
        for item in files_and_dirs:
            if item.endswith('.txt'):
                print("-",item[:-4])
                i += 1
            return True
        if i == 0:
            print("No recipe founded, please try creating new recipe")
            return False




if __name__ == "__main__":
    document_path = os.path.join(os.path.expanduser('~'), 'Documents')
    dir_path = os.path.join(document_path, "cookbook")
    app = CookBook()
    while True:

        while app.folder_path == dir_path:
            print("\n\n\n\nBookCook(Folder Management)")
            print("""
        What would you like to do?
        1.  Make new Folder
        2.  Select Folder
        3.  List Folder
        4.  Delete Folder
        5.  Quit
            """)

            try:
                x = int(input("(1/2/3/4)>>"))
                if x == 1:
                    i = input("Enter file name: ")
                    app.createFolder(i)
                    input("'Enter' to continue")

                elif x == 2:
                    if not app.listFile():
                        i = input("Enter file name to select (case-sensitive) >> ")
                        app.findFolder(i)
                        break
                    else:
                        input("'Enter' to continue")
                        continue
                elif x == 3:
                    app.listFile()
                    input("'Enter' to continue")
                elif x == 4:
                    app.listFile()
                    y = input("Enter file name to delete (case-sensitive) >>")
                    app.deleteFolder(y)
                    input("'Enter' to continue")
                elif x ==5:
                    quit()
                else:
                    print("Enter a choice")
                    input("'Enter' to continue")
            except Exception as e:
                continue

        while True:
            print("\n\n\n\nBookCook(App)")
            print("""
        What would you like to do?
        1.  Make new Recipe
        2.  View Recipe
        3.  Delete Recipe
        4.  Back to folder selection
            """)

            get = int(input("(1/2/3/4)>>"))

            if get == 1:
                app.createRecipe()
                input("'Enter' to continue")

            elif get == 2:
                while True:
                    if not app.listSelected():
                        input("'Enter' to continue")
                        break
                    else:
                        t = input("Enter recipe name to view >>")
                        if t == "back":
                            input("'Enter' to continue")
                            break
                        if not app.viewRecipe(t):
                            input("'Enter' to continue")
                            break

            elif get == 3:
                while True:
                    if not app.listSelected():
                        input("'Enter' to continue")
                        break
                    else:
                        go = input("Enter a file to be deleted >>")
                        if go == "back":
                            input("'Enter' to continue")
                            break
                        if not app.deleteRecipe(go):
                            input("'Enter' to continue")
                            break

            elif get == 4:
                app.clear()
                break




