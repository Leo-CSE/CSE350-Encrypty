import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from encrypty import encrypt_file, decrypt_file, key

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Encrypty")
        self.setGeometry(100, 100, 400, 200)

        # GUI components
        select_file_button = QPushButton("Select File")
        encrypt_button = QPushButton("Encrypt")
        decrypt_button = QPushButton("Decrypt")
        message_label = QLabel("Select a file and choose an action:")
        
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
