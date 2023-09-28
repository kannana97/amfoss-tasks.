import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtCore import QRect
import requests

from search_window import SearchWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.w = None

    def initUI(self):
        self.setWindowTitle("Pokédex")
        self.setFixedSize(850, 500)

        self.setStyleSheet("""
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QMainWindow {
                background-color: black;
            }
            QLabel {
                font-size: 32px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)

        labelmov = QLabel(self)
        labelmov.setScaledContents(True)
        movie = QMovie("../assets/openingpokeball-pokemon.gif")
        labelmov.setGeometry(QRect(0, 0, 900, 478))
        labelmov.setMovie(movie)
        movie.start()

        poke_search_label = QLabel("POKÉSEARCH", self)
        poke_search_label.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
        poke_search_label.setGeometry(QRect(50, 5, 900, 250))

        poke_label = QLabel("ENGINE ", self)
        poke_label.setStyleSheet("color: white; font-size: 32px; font-weight: bold;")
        poke_label.setGeometry(QRect(50, 50, 900, 250))

        pushButton = QPushButton(parent=self, text='GO!')
        pushButton.setGeometry(50, 300, 160, 43)
        pushButton.clicked.connect(self.open_search_window)

        # Add a QLineEdit widget for entering Pokémon names
        self.search_line_edit = QLineEdit(self)
        self.search_line_edit.setGeometry(50, 250, 160, 30)
        self.search_line_edit.setPlaceholderText("Enter Pokémon Name")

        self.labelpic = QLabel(self)
        self.labelpic.setGeometry(QRect(400, 20, 550, 700))
        self.labelpic.setPixmap(QPixmap(""))
        self.labelpic.setScaledContents(True)

        self.show()

    def open_search_window(self, checked):
        if self.w is None:
            self.w = SearchWindow()
            # Connect the SearchWindow's search_button to fetch_and_display_pokemon_data
            self.w.search_button.clicked.connect(self.fetch_and_display_pokemon_data)
        self.w.show()

    def fetch_and_display_pokemon_data(self):
        # Get the entered Pokémon name from the QLineEdit
        pokemon_name = self.search_line_edit.text().strip().lower()

        if pokemon_name:
            try:
                # Make an API request to the Poke API
                response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")

                if response.status_code == 200:
                    data = response.json()
                    # Extract relevant data (e.g., name, sprite URL)
                    name = data["name"].capitalize()
                    sprite_url = data["sprites"]["front_default"]

                    # Update the label with the Pokémon name
                    self.labelpic.setText(f"Pokemon: {name}")

                    # Load and display the Pokémon sprite (image)
                    pixmap = QPixmap(sprite_url)
                    self.labelpic.setPixmap(pixmap)
                    self.labelpic.setScaledContents(True)

                    # Clear any previous error messages
                    self.w.error_label.setText("")
                else:
                    # Handle API request errors
                    self.labelpic.setText("Pokemon not found")
            except requests.exceptions.RequestException:
                # Handle network or request errors
                self.labelpic.setText("Error fetching data")
        else:
            # Handle the case when no Pokémon name is entered
            self.labelpic.setText("Enter a Pokémon name")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
