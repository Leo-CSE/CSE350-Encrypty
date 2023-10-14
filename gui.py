import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from encrypty import encrypt_file, decrypt_file

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Encrypty")
        self.setGeometry(100, 100, 400, 200)

        # GUI components
        encrypt_button = QPushButton("Encrypt")
        decrypt_button = QPushButton("Decrypt")
        message_label = QLabel("Select a file and choose an action:")

        # Position GUI components and define layout
        layout = QVBoxLayout()
        layout.addWidget(message_label)
        layout.addWidget(encrypt_button)
        layout.addWidget(decrypt_button)

        # Set layout to the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Event handlers
        def encrypt_clicked():
            # Pass the file path and encryption key to the encrypt_file function
            encrypt_file("file_path", "encryption_key")

        def decrypt_clicked():
            # Pass the file path and encryption key to the decrypt_file function
            decrypt_file("file_path", "encryption_key")

        encrypt_button.clicked.connect(encrypt_clicked)
        decrypt_button.clicked.connect(decrypt_clicked)
