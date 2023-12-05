import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog, QInputDialog
from PyQt5.QtGui import QIcon, QFont, QCursor
from PyQt5.QtCore import Qt
from encrypty import Encrypty
from keymanager import KeyManager

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Encrypty")
        self.setGeometry(100, 100, 400, 200)
        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon('icon.png'))

        # GUI components
        select_file_button = QPushButton("Select File...", objectName="fileSelect")
        encrypt_button = QPushButton("Encrypt")
        decrypt_button = QPushButton("Decrypt")
        message_label = QLabel("Select a file to encrypt or decrypt:")

        # Store selected file path
        self.selected_file_path = None

        # Key management
        self.master_password, ok = QInputDialog.getText(self, 'Master Password', 'Enter your master password:')
        if ok:
            salt = KeyManager.load_salt()
            if salt is None:
                salt = KeyManager.generate_salt()
                KeyManager.save_salt(salt)

            key = KeyManager.derive_key_from_password(self.master_password, salt)
            KeyManager.save_key(key)

            self.key = key

            # Event handlers
            def select_file():
                nonlocal self
                self.selected_file_path, _ = QFileDialog.getOpenFileName(None, "Select a file", "", "All Files (*)")
                message_label.setText(f"Selected File: {self.selected_file_path}")

            def update_progress(progress):
                print(f"Progress: {progress}%")

            def encrypt_clicked():
                if self.selected_file_path:
                    success = Encrypty.encrypt_file(self.selected_file_path, self.key)
                    if success:
                        update_progress(100)

            def decrypt_clicked():
                if self.selected_file_path:
                    success = Encrypty.decrypt_file(self.selected_file_path, self.key)
                    if success:
                        update_progress(100)

            # Connect event handlers
            select_file_button.clicked.connect(select_file)
            encrypt_button.clicked.connect(encrypt_clicked)
            decrypt_button.clicked.connect(decrypt_clicked)

            # Position GUI components and define layout
            layout = QVBoxLayout()
            layout.addWidget(message_label)
            layout.addWidget(select_file_button)
            layout.addWidget(encrypt_button)
            layout.addWidget(decrypt_button)

            # Set layout to the main window
            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            # Align label to the horizontal center
            message_label.setAlignment(Qt.AlignHCenter)

            # Setting font
            font = QFont()
            font.setFamily("System")
            font.setPointSize(24)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            message_label.setFont(font)
            encrypt_button.setFont(font)
            decrypt_button.setFont(font)
            select_file_button.setFont(font)

            # On button hover, set cursor to PointingHandCursor
            encrypt_button.setCursor(QCursor(Qt.PointingHandCursor))
            decrypt_button.setCursor(QCursor(Qt.PointingHandCursor))
            select_file_button.setCursor(QCursor(Qt.PointingHandCursor))

            # Stylesheet
            self.setStyleSheet("""
            QMainWindow {
            background-color: #495369;
            }

            QPushButton { 
                    background-color: #859ba8;
                    color: white;
                    padding: 18px 16px;
                    font: 20px;
                    border-top-left-radius: 8px;
                    margin: 8px;
                    border-top-right-radius: 8px;
                    border-bottom-left-radius: 8px; 
                    border-bottom-right-radius: 8px;
                    border: none;
             } 

             QPushButton:hover {
                border: 1px solid white;
                background-color: #708591;
             }

             QPushButton:pressed {
             background-color: #5d7380;
             border: 1px solid #c4c4c4;
             }

             QPushButton#fileSelect {
             text-decoration: underline;
             }

             QLabel {
             color: white;
             font: 20px;
             }
             """)
