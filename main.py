import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QTextEdit, QLineEdit, QLabel, QMessageBox, QListWidget, QInputDialog
)

class RecipeManager:
    def __init__(self, storage_file="recipes.json"):
        self.recipes = []
        self.storage_file = storage_file
        self.load_recipes()

    def save_recipes(self):
        with open(self.storage_file, "w") as file:
            json.dump([recipe.to_dict() for recipe in self.recipes], file, indent=4)

    def load_recipes(self):
        try:
            with open(self.storage_file, "r") as file:
                recipes_data = json.load(file)
                self.recipes = [Recipe.from_dict(data) for data in recipes_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.recipes = []

    def add_recipe(self, title, ingredients, instructions):
        self.recipes.append(Recipe(title, ingredients, instructions))
        self.save_recipes()

    def get_recipes(self):
        return self.recipes

    def delete_recipe(self, index):
        if 0 <= index < len(self.recipes):
            del self.recipes[index]
            self.save_recipes()

class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    def to_dict(self):
        return {"title": self.title, "ingredients": self.ingredients, "instructions": self.instructions}

    @staticmethod
    def from_dict(data):
        return Recipe(data["title"], data["ingredients"], data["instructions"])

class RecipeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.recipe_manager = RecipeManager()

        self.setWindowTitle("Recipe Manager")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.recipe_list = QListWidget()
        self.load_recipe_list()
        layout.addWidget(self.recipe_list)

        self.view_button = QPushButton("View Recipe")
        self.view_button.clicked.connect(self.view_recipe)
        layout.addWidget(self.view_button)

        self.add_button = QPushButton("Add Recipe")
        self.add_button.clicked.connect(self.add_recipe)
        layout.addWidget(self.add_button)

        #new button
        self.edit_button = QPushButton("Edit Recipe")
        self.edit_button.clicked.connect(self.edit_recipe)
        layout.addWidget(self.edit_button)


        self.delete_button = QPushButton("Delete Recipe")
        self.delete_button.clicked.connect(self.delete_recipe)
        layout.addWidget(self.delete_button)

        self.central_widget.setLayout(layout)

    def load_recipe_list(self):
        self.recipe_list.clear()
        for recipe in self.recipe_manager.get_recipes():
            self.recipe_list.addItem(recipe.title)

    def view_recipe(self):
        selected_item = self.recipe_list.currentRow()
        if selected_item == -1:
            QMessageBox.warning(self, "Warning", "Please select a recipe to view.")
            return

        recipe = self.recipe_manager.get_recipes()[selected_item]
        details = f"Title: {recipe.title}\nIngredients: {', '.join(recipe.ingredients)}\nInstructions: {recipe.instructions}"
        QMessageBox.information(self, "Recipe Details", details)

    def add_recipe(self):
        title, ok = QInputDialog.getText(self, "Add Recipe", "Enter recipe title:")
        if not ok or not title.strip():
            return

        ingredients, ok = QInputDialog.getText(self, "Add Recipe", "Enter ingredients (comma-separated):")
        if not ok:
            return

        instructions, ok = QInputDialog.getMultiLineText(self, "Add Recipe", "Enter instructions:")
        if not ok:
            return

        self.recipe_manager.add_recipe(title, ingredients.split(','), instructions)
        self.load_recipe_list()


    def edit_recipe(self):
        selected_item = self.recipe_list.currentRow()
        if selected_item == -1:
            QMessageBox.warning(self, "Warning", "Please select a recipe to edit.")
            return

        recipe = self.recipe_manager.get_recipes()[selected_item]

        new_title, ok = QInputDialog.getText(self, "Edit Recipe", "Edit title:", text=recipe.title)
        if not ok or not new_title.strip():
            return

        new_ingredients, ok = QInputDialog.getText(self, "Edit Recipe", "Edit ingredients (comma-separated):", text=", ".join(recipe.ingredients))
        if not ok:
            return

        new_instructions, ok = QInputDialog.getMultiLineText(self, "Edit Recipe", "Edit instructions:", text=recipe.instructions)
        if not ok:
            return

        # Update recipe details
        recipe.title = new_title
        recipe.ingredients = new_ingredients.split(',')
        recipe.instructions = new_instructions

        # Save and refresh list
        self.recipe_manager.save_recipes()
        self.load_recipe_list()


    def delete_recipe(self):
        selected_item = self.recipe_list.currentRow()
        if selected_item == -1:
            QMessageBox.warning(self, "Warning", "Please select a recipe to delete.")
            return

        confirm = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this recipe?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.recipe_manager.delete_recipe(selected_item)
            self.load_recipe_list()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecipeApp()
    window.show()
    sys.exit(app.exec_())
