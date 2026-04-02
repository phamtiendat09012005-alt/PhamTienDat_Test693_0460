import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# Đổi tên import sao cho khớp với file UI Railfence của bạn (giả sử là ui.Railfence)
from ui.Railfence import Ui_MainWindow 
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Chỉ giữ lại 2 nút mã hóa và giải mã
        self.ui.btn_encypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        
        # Lấy khóa (số lượng rail) từ UI. Giả sử bạn có một ô nhập tên là txt_key
        try:
            key_value = int(self.ui.txt_key.text()) # Hoặc .toPlainText() tùy vào loại widget (QLineEdit hoặc QTextEdit)
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Vui lòng nhập Key là một số nguyên (số rails) hợp lệ!")
            msg.exec_()
            return

        payload = {
            "plain_text": self.ui.txt_plaintext.toPlainText(), 
            "key": key_value
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Key trả về từ api.py của bạn là 'encrypted_text'
                self.ui.txt_ciphertext.setText(data["encrypted_text"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Mã hóa thành công!")
                msg.exec_()
            else:
                print("Lỗi khi gọi API: ", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Lỗi: %s" % e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        
        # Lấy khóa (số lượng rail) từ UI
        try:
            key_value = int(self.ui.txt_key.text())
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Vui lòng nhập Key là một số nguyên (số rails) hợp lệ!")
            msg.exec_()
            return

        payload = {
            "cipher_text": self.ui.txt_ciphertext.toPlainText(), 
            "key": key_value
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Key trả về từ api.py của bạn là 'decrypted_text'
                self.ui.txt_plaintext.setText(data["decrypted_text"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Giải mã thành công!")
                msg.exec_()
            else:
                print("Lỗi khi gọi API: ", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Lỗi: %s" % e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())