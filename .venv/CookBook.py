import os

def file_exists(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    return os.path.exists(file_path)

#Interface
class CookBook:

    def __init__(self):
        self.folder_path = 0

    def findfolder(self,x):
        folder_path = x

        if os.path.isdir(folder_path):
            print(f"You selected: {folder_path}")
            return folder_path
        else:
            print("Invalid folder path. Please try again.")
            return select_folder()

    def makeFolder(self, x):
        folder_name = x  # Folder's name
        documents_path = os.path.join(os.path.expanduser('~'), 'Documents') # Document folder
        self.folder_path = os.path.join(documents_path, folder_name)

        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
            print("Folder created successfully!")
        else:
            print("Founded")

    def makeRecipie(self):
        file_name = input("Enter the name of the recipie: ")
        file_path = os.path.join(self.folder_path, f"{file_name}.txt")
        with open(file_path, 'w') as f:
            print("ENTER 'done' IF FINISH INPUTTING RECIPIE")
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


    def view_recipe(self, name):
        recipe_name = name
        recipe_path = os.path.join(self.folder_path, f"{recipe_name}.txt")
        if os.path.exists(recipe_path):
            with open(recipe_path, 'r') as f:
                print(f.read())
        else:
            print("Recipe not found.")

    def delete_recipe(self, delete):
        recipe_name = delete
        folder = self.folder_path
        if os.path.exists(folder):
            if file_exists(folder, recipe_name):
                os.remove(recipe_path)
            print("Recipe deleted successfully!")
        else:
            print("Recipe not found.")



#UI
print("BookCook")
print("""
What would you like to do?
1.  Select/Make new account
2.  Write Recipie
3.  View Recipie
4.  Delete Recipie
""")
