# Recipe-Manager
Recipe Manager is a simple and intuitive desktop application for storing, viewing, editing, and organizing recipes. Users can add recipes with ingredients and instructions, edit existing entries, and delete recipes as needed. Built with PyQt5, the app provides a user-friendly interface for easy recipe management.

## Features  
- 📜 View a list of saved recipes  
- ➕ Add new recipes with title, ingredients, and instructions  
- ✏️ Edit existing recipes  
- ❌ Delete unwanted recipes  
- 💾 Data is saved in `recipes.json` for persistence

## Installation  
1. Clone the repository:  
   ```sh
   git clone https://github.com/yourusername/recipe-manager.git
   cd recipe-manager
2. Install dependencies:
   ```sh
   pip install PyQt5
3. Run the application:
    ```sh
   python recipe_manager.py

## Usage
- Click Add Recipe to create a new recipe.
- Select a recipe from the list and click View Recipe to see details.
- Click Edit Recipe to modify an existing recipe.
- Click Delete Recipe to remove a recipe permanently.  

## Structure  
      ```sh
      |-- recipe-manager
      │-- recipes.json          # Stores recipes data
      │-- recipe_manager.py     # Main application script
      │-- README.md             # Project documentation


## Credits
This project was started with the tutorial from Code Nust (https://www.youtube.com/watch?v=39GJ6XGCYlI) , which provided the foundation for building a recipe management app.


## Features Added
This project was inspired by the tutorial, but I made different changes, including:
- **🖥 GUI Added**  
   Introduced a graphical user interface for a more intuitive and enjoyable user experience.

- **✏️ Edit Existing Recipes**  
   Added the functionality to modify previously saved recipes, enabling users to edit instead of just adding or deleting.

- **📜 Enhanced Recipe Display**  
   Improved the presentation of recipes to make the output more readable and user-friendly.

- **❌ Delete Recipe Feature**  
   Users can now delete unwanted recipes directly from the interface with ease.

- **💾 Persistent Storage**  
   Previously, recipes were lost upon closing the application. Now, recipes are stored in `recipes.json` and automatically loaded at startup, ensuring persistence.

## Contributing
Feel free to submit issues or pull requests to improve the application.


