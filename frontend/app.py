import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox)
from PySide6.QtCore import Qt

class FitTrackLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # הגדרות חלון ה-Login
        self.setWindowTitle("FitTrack AI - Login")
        self.resize(350, 250)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setSpacing(15) # רווח נעים בין השדות
        
        # כותרת המסך
        self.title_label = QLabel("FitTrack AI Login")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #2C3E50;")
        layout.addWidget(self.title_label)
        
        # שדה שם משתמש
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setStyleSheet("padding: 8px; font-size: 14px;")
        layout.addWidget(self.username_input)
        
        # שדה סיסמה
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password) # הופך את הסיסמה לכוכביות
        self.password_input.setStyleSheet("padding: 8px; font-size: 14px;")
        layout.addWidget(self.password_input)
        
        # כפתור התחברות
        self.login_btn = QPushButton("Login")
        self.login_btn.setStyleSheet("padding: 10px; background-color: #3498DB; color: white; font-weight: bold; font-size: 14px; border-radius: 4px;")
        self.login_btn.clicked.connect(self.handle_login) # חיבור לפעולת לחיצה
        layout.addWidget(self.login_btn)
        
        central_widget.setLayout(layout)

    def handle_login(self):
        # פונקציה פשוטה שבודקת מה המשתמש הקליד
        username = self.username_input.text()
        password = self.password_input.text()
        
        # בדיקה זמנית (בשלב הבא נחבר את זה ל-Backend האמיתי!)
        if username == "Moriah" and password == "1234":
            QMessageBox.information(self, "Success", "Login Successful! Welcome to FitTrack AI.")
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FitTrackLogin()
    window.show()
    sys.exit(app.exec())