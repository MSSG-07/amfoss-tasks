from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QScrollArea, QDialog, QGridLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import requests
import os

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pokémon Search")
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
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)

        # Widgets
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter Pokémon name")
        self.textbox.setGeometry(50, 55, 280, 40)

        label1 = QLabel("Enter Pokémon name:", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 100, 160, 43)
        enter_button.clicked.connect(self.search_pokemon)

        self.capture_button = QPushButton("Capture", self)
        self.capture_button.setGeometry(50, 350, 160, 43)
        self.capture_button.setEnabled(False)  # Disabled initially
        self.capture_button.clicked.connect(self.capture_image)

        self.show_button = QPushButton("Show Captured", self)
        self.show_button.setGeometry(50, 400, 160, 43)
        self.show_button.clicked.connect(self.show_captured_pokemons)

        self.pokemon_image_label = QLabel(self)
        self.pokemon_image_label.setGeometry(400, 50, 200, 200)

        self.pokemon_info_label = QLabel(self)
        self.pokemon_info_label.setGeometry(400, 250, 400, 200)

        self.captured_pokemons = []

        # QLabel to show capture message
        self.capture_message_label = QLabel(self)
        self.capture_message_label.setGeometry(50, 450, 300, 40)
        self.capture_message_label.setAlignment(Qt.AlignCenter)
        self.capture_message_label.setStyleSheet("font-size: 14px; color: green;")
        self.capture_message_label.setText("")  # Initially empty

    def search_pokemon(self):
        pokemon_name = self.textbox.text().lower()
        if pokemon_name:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                self.display_pokemon_info(data)
            else:
                self.pokemon_info_label.setText("Pokémon not found.")

    def display_pokemon_info(self, data):
        pokemon_name = data['name'].capitalize()
        abilities = ", ".join([ability['ability']['name'] for ability in data['abilities']])
        types = ", ".join([type['type']['name'] for type in data['types']])
        stats = "\n".join([f"{stat['stat']['name']}: {stat['base_stat']}" for stat in data['stats']])

        self.pokemon_info_label.setText(f"Name: {pokemon_name}\nAbilities: {abilities}\nTypes: {types}\nStats:\n{stats}")

        image_url = data['sprites']['other']['official-artwork']['front_default']
        self.display_image(image_url)

        self.capture_button.setEnabled(True)  # Enable capture button

    def display_image(self, image_url):
        response = requests.get(image_url)
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        scaled_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        self.pokemon_image_label.setPixmap(scaled_pixmap)

    def capture_image(self):
        # Save the image
        if self.pokemon_image_label.pixmap():
            pokemon_name = self.textbox.text().lower()
            os.makedirs("captured_pokemons", exist_ok=True)
            file_path = f"captured_pokemons/{pokemon_name}.png"
            self.pokemon_image_label.pixmap().save(file_path)
            self.captured_pokemons.append(file_path)

            # Update the capture message label
            self.capture_message_label.setText(f"Pokémon captured: {pokemon_name}")

    def show_captured_pokemons(self):
        # Show all captured Pokémon images in a new dialog window
        if not self.captured_pokemons:
            return
        
        captured_window = CapturedPokemonsWindow(self.captured_pokemons)
        captured_window.exec()

class CapturedPokemonsWindow(QDialog):
    def __init__(self, captured_pokemons):
        super().__init__()

        self.setWindowTitle("Captured Pokémon")
        self.setFixedSize(600, 400)

        # Layout to display images
        layout = QGridLayout(self)

        row, col = 0, 0
        for file_path in captured_pokemons:
            pixmap = QPixmap(file_path)
            pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
            label = QLabel(self)
            label.setPixmap(pixmap)
            layout.addWidget(label, row, col)

            col += 1
            if col > 4:
                col = 0
                row += 1

        self.setLayout(layout)

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
