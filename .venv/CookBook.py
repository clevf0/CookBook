import os

def file_exists(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    return os.path.exists(file_path)

#Interface
class CookBook:
    #Declaring folder_path through out the class
    def __init__(self):
        self.folder_path = 0

    #function to find folder
    def findFolder(self, x):
        document_path = os.path.join(os.path.expanduser('~'), 'Documents')
        try:
            data_path = os.path.join(document_path, "cookbook")
            x = os.path.join(data_path,x)
        except Exception as e:
            print(e)
        if os.path.isdir(data_path):
            print("Founded data path")
            if os.path.isdir(x):
                print(f"selected {x}")
                self.folder_path = x
                return x
            else:
                print(f"file {x} is not founded")
                return self.findFolder(input("Folder path: "))

        else:
            print("Try to make a new recipe first")



    #function for creating folder
    def createFolder(self, x):
        folder_name = x  # Folder's name
        documents_path = os.path.join(os.path.expanduser('~'), 'Documents')# Document folder
        data_path = os.path.join(documents_path, "cookbook") #File data path on document folder
        self.folder_path = os.path.join(data_path, folder_name)
        try:
            if not os.path.exists(data_path):
                os.makedirs(data_path)

            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path)
                print("Folder created successfully!")
            else:
                print("Founded")
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
        recipe_name = name
        recipe_path = os.path.join(self.folder_path, f"{recipe_name}.txt")
        if os.path.exists(recipe_path):
            with open(recipe_path, 'r') as f:
                print(f.read())
        else:
            print("Recipe not found.")
    def pathSelected(self):                                                                                              #Used for debugging
        print(self.folder_path)

    #function to delete recipe(to be coded)

    #function to list recipe created on the folder(to be coded)


#UI
print("BookCook")
print("""
What would you like to do?
1.  Make new file
2.  Select file
3.  Write Recipe
4.  View Recipe
5.  Delete Recipe
""")

app = CookBook()
app.createFolder("sigma")
app.findFolder("alpha")
app.pathSelected()