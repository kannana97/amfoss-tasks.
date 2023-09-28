from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap
import requests

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(850, 500)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 280, 40)
        self.textbox.setPlaceholderText("Enter Pokemon Name")

        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        self.search_button = QPushButton("Search", self)
        self.search_button.setGeometry(50, 300, 160, 43)
        self.search_button.clicked.connect(self.fetch_and_display_pokemon_data)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)

    def fetch_and_display_pokemon_data(self):
        # Get the entered Pokémon name from the QLineEdit
        pokemon_name = self.textbox.text().strip().lower()

        if pokemon_name:
            try:
                # Make an API request to the Poke API
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
                if response.status_code == 200:
                    data = response.json()
                    # Extract relevant data (e.g., name, sprite URL)
                    name = data["name"].capitalize()
                    sprite_url = data["sprites"]["front_default"]

                    # Create a QLabel to display Pokémon name
                    pokemon_name_label = QLabel(f"Pokemon: {name}", self)
                    pokemon_name_label.setGeometry(400, 50, 400, 30)

                    # Load and display the Pokémon sprite (image)
                    pixmap = QPixmap(sprite_url)
                    pokemon_sprite_label = QLabel(self)
                    pokemon_sprite_label.setGeometry(400, 100, 400, 400)
                    pokemon_sprite_label.setPixmap(pixmap)
                    pokemon_sprite_label.setScaledContents(True)
                else:
                    # Handle API request errors
                    print("Pokemon not found")
            except requests.exceptions.RequestException:
                # Handle network or request errors
                print("Error fetching data")

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
