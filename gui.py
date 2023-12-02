import sys
import os  # LH:
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from encrypty import encrypt_file, decrypt_file, key
from PyQt5.QtGui import QIcon  # LH: Import QIcon
from PyQt5.QtCore import QSize  # LH: Import QSize
from PyQt5.QtWidgets import QLabel  # LH:
from PyQt5.QtGui import QFont  # LH:
from PyQt5.QtCore import Qt  # LH:


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # LH: Construct icon file path
        icon_path = os.path.join('Icons', 'Lock_icon.png')
        select_file_icon_path = os.path.join('Icons', 'select_file_icon.png')
        encrypt_icon_path = os.path.join('Icons', 'encrypt_icon.png')
        decrypt_icon_path = os.path.join('Icons', 'decrypt_icon.png')

        self.setWindowTitle("Encrypty")
        self.setWindowIcon(QIcon(icon_path))  # LH: Set the window icon
        self.setGeometry(100, 100, 500, 500)

        icon_size = QSize(60, 60)  # LH: Define the icon size (width, height in pixels)

        # GUI components
        select_file_button = QPushButton("Select File")
        select_file_button.setIcon(QIcon(select_file_icon_path))
        select_file_button.setIconSize(icon_size)  # LH: Set the icon size for select file button

        encrypt_button = QPushButton("Encrypt")
        encrypt_button.setIcon(QIcon(encrypt_icon_path))
        encrypt_button.setIconSize(icon_size)  # LH: Set the icon size for encrypt button

        decrypt_button = QPushButton("Decrypt")
        decrypt_button.setIcon(QIcon(decrypt_icon_path))
        decrypt_button.setIconSize(icon_size)  # LH: Set the icon size for decrypt button

        message_label = QLabel("Select a file and choose an action:")

        # Set font style and size
        font = QFont("Roboto", 12, QFont.Bold)  # Example: Arial, 12pt, bold
        message_label.setFont(font)

        # Adjust text color and alignment using style sheets
        message_label.setStyleSheet("color: #333333;")  # Example: blue text color
        message_label.setAlignment(Qt.AlignCenter)  # Center align the text

        # LH: Add margins
        message_label.setContentsMargins(10, 10, 10, 10)  # LH: Margins around the text

        # Store selected file path
        selected_file_path = None

        # Event handlers
        def select_file():
            nonlocal selected_file_path
            # Open file dialog
            selected_file_path, _ = QFileDialog.getOpenFileName(None, "Select a file", "", "All Files (*)")
            message_label.setText(f"Selected File: {selected_file_path}")

        def encrypt_clicked():
            # Pass the file path and encryption key to the encrypt_file function
            encrypt_file(selected_file_path, key)

        def decrypt_clicked():
            # Pass the file path and encryption key to the decrypt_file function
            decrypt_file(selected_file_path, key)

        # Connect event handlers
        select_file_button.clicked.connect(select_file)
        encrypt_button.clicked.connect(encrypt_clicked)
        decrypt_button.clicked.connect(decrypt_clicked)

        # Position GUI components and define layout
        layout = QVBoxLayout()
        layout.addWidget(select_file_button)
        layout.addWidget(message_label)
        layout.addWidget(encrypt_button)
        layout.addWidget(decrypt_button)

        # Set layout to the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
