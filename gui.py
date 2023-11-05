import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from encrypty import encrypt_file, decrypt_file, key

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set window title, size, icon image
        self.setWindowTitle("Encrypty")
        self.setGeometry(100, 100, 400, 200)
        self.setFixedSize(400,300) #stops user from resizing window, however, cuts off selected file path.
        self.setWindowIcon(QIcon('icon.png'))

        # GUI components
        select_file_button = QPushButton("Select File...", objectName="fileSelect")
        encrypt_button = QPushButton("Encrypt")
        decrypt_button = QPushButton("Decrypt")
        message_label = QLabel("Select a file to encrypt or decrpyt:")
        
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
        font = QtGui.QFont()
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
        encrypt_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        decrypt_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        select_file_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

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