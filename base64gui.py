from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QWidget, QLabel, QTextEdit, QTextBrowser, QMessageBox, QApplication, QFileDialog, QDialog
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import Qt, QIcon
from PIL import Image
from io import BytesIO
import sys
import base64
import getpass

user_name = getpass.getuser()

#0 메인 페이지
class FirstWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        btnRun1 = QPushButton(self)	
        btnRun1.setStyleSheet('image:url(./img/1_img_kr.png);border:0px;')
        btnRun1.setGeometry(50, 50, 400, 400) 
        btnRun1.clicked.connect(self.change_stack1)

        btnRun2 = QPushButton(self)	
        btnRun2.setStyleSheet('image:url(./img/2_img_kr.png);border:0px;')
        btnRun2.setGeometry(500, 50, 400, 400) 
        btnRun2.clicked.connect(self.change_stack2)
     
        exit_button = QPushButton(self)	
        exit_button.setStyleSheet('image:url(./img/PNG_exit_2.png);border:0px;')
        exit_button.setGeometry(900, 0, 50, 50) 
        exit_button.clicked.connect(QCoreApplication.instance().quit)

    def change_stack1(self):
        self.parent().stack.setCurrentIndex(1)

    def change_stack2(self):
        self.parent().stack.setCurrentIndex(4)


#1 인코딩 페이지
class SecondWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # layout = QtWidgets.QVBoxLayout(self)
        # label1 = QLabel('1페이지', self)
        # label1.setAlignment(Qt.AlignVCenter)
        # label1.move(150, 40)

        self.butt1 = QPushButton(self)
        self.butt1.setStyleSheet('image:url(./img/text_img.png);border:0px;')	
        self.butt1.setGeometry(50, 50, 400, 400) 
        self.butt1.clicked.connect(self.change_stack1)

        self.butt2 = QPushButton(self)	
        self.butt2.setStyleSheet('image:url(./img/image_img.png);border:0px;')	
        self.butt2.setGeometry(500, 50, 400, 400) 
        self.butt2.clicked.connect(self.change_stack2)

        self.back = QPushButton(self)	
        self.back.setStyleSheet('image:url(./img/back_img.png);border:0px;')	
        self.back.setGeometry(0, 0, 50, 50) 
        self.back.clicked.connect(self.change_stack3)

    #2 텍스트 인코딩 페이지 
    def change_stack1(self):
        self.parent().stack.setCurrentIndex(2)

    # 3 이미지 
    def change_stack2(self):
        self.parent().stack.setCurrentIndex(3)


    # 뒤로 가기 
    def change_stack3(self):
        self.parent().stack.setCurrentIndex(0)


#2 텍스트 인코딩 페이지 
class SecondWidget1(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        layout = QtWidgets.QVBoxLayout(self)
        label1 = QLabel('입력', self)
        label1.setAlignment(Qt.AlignVCenter)
        label1.move(200, 30)

        label2 = QLabel('결과', self)
        label2.setAlignment(Qt.AlignVCenter)
        label2.move(710, 30)

        # self.text_box1 = QTextBrowser(self)
        # self.text_box1.append("None")
        # self.text_box1.setGeometry(50, 60, 350, 350) 

        self.text_box1 = QTextEdit(self)
        self.text_box1.resize(350, 350)
        self.text_box1.move(50, 60)

        self.text_box2 = QTextBrowser(self)
        self.text_box2.append('')
        self.text_box2.setGeometry(550, 60, 350, 350) 

        self.ok_base64 = QPushButton("OK", self)	
        self.ok_base64.setGeometry(50, 420, 850, 45) 
        self.ok_base64.clicked.connect(self.base64_conversion)

        self.back = QPushButton(self)
        self.back.setStyleSheet('image:url(./img/back_img.png);border:0px;')		
        self.back.setGeometry(0, 0, 50, 50) 
        self.back.clicked.connect(self.change_stack1)

    def base64_conversion(self):
        '''
        QTextEdit 사용 경우 .toPlainText() 사용 바람
        https://doc.qt.io/qt-5/qplaintextedit.html#plainText-prop 참조
        '''
        # print(self.text_box1.toPlainText())

        # Base64 변환 과정
        inpututf = self.text_box1.toPlainText().encode('utf-8') # ascii 사용시 오류발생 utf-8으로 사용하세요
        finalvalue = base64.b64encode(inpututf)
        print(finalvalue)

        '''
        내용 수정또는 추가시 내용 초기화
        https://study-code.gitbook.io/python-basic/qtpy/pyqt-widget/application-make/widget-2#undefined-1 참조
        '''
        self.text_box2.clear()
        self.text_box2.repaint()

        '''
        "b"와 따옴표없이 출력 .decode("utf-8")
        https://stackoverflow.com/a/45151048 참조
        '''
        self.text_box2.append(str(finalvalue.decode("utf-8")))

        
    def change_stack(self):
        self.parent().stack.setCurrentIndex(0)

    def change_stack1(self):
        self.parent().stack.setCurrentIndex(1)

# 3 이미지 디코딩 페이지
class SecondWidget2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.back = QPushButton(self)
        self.back.setStyleSheet('image:url(./img/back_img.png);border:0px;')	
        self.back.setGeometry(0, 0, 50, 50) 
        self.back.clicked.connect(self.change_stack1)

        label1 = QLabel(' 중요한 이미지는 변환하지마세요 BASE64는 보안으로 매우 약합니다 간단한 텍스트 용도으로 사용하기 때문에 이미지 \n 변환은 권장하지 않습니다', self)
        label1.move(125, 180)

        self.files = QPushButton("파일 선택", self)	
        self.files.setGeometry(50, 100, 850, 50) 
        self.files.clicked.connect(self.pushButtonClicked)

        self.files_encoding = QPushButton("OK", self)	
        self.files_encoding.setGeometry(800, 450, 100, 30) 
        self.files_encoding.clicked.connect(self.base64_files_encoding)

    def pushButtonClicked(self):
        # self.FileOpen = QFileDialog.getOpenFileName(self, '열기', './')
        '''
        특정 확장자 검색
        https://doc.qt.io/qt-5/qfiledialog.html 참조
        '''
        # self.FileOpen = QFileDialog.getOpenFileName(self, '열기', '','Images (*.png *.jpg *.bmp);; All File(*)')
        self.FileOpen = QFileDialog.getOpenFileName(self, '열기', '','Images (*.png *.jpg *.bmp)')
        # self.files.setText(self.FileOpen[0])
        print(self.FileOpen[0])
    
    def base64_files_encoding(self):
        
        with open(self.FileOpen[0], 'rb') as imagefile:
            byteform = base64.b64encode(imagefile.read())

        f = open('C:/Users/'+user_name+'/Desktop/base64encoding.bin', 'wb')
        f.write(byteform)
        f.close()

        guidance = QMessageBox.information(self, 'base64(개발중)', '바탕화면에 base64encoding.bin 파일이 생성했습니다', QMessageBox.Ok)
        print('완료')


    def change_stack1(self):
        self.parent().stack.setCurrentIndex(1)

# 4 디코딩 페이지
class SecondWidget3(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.butt1 = QPushButton(self)
        self.butt1.setStyleSheet('image:url(./img/text_img.png);border:0px;')		
        self.butt1.setGeometry(50, 50, 400, 400) 
        self.butt1.clicked.connect(self.change_stack1)

        self.butt2 = QPushButton(self)
        self.butt2.setStyleSheet('image:url(./img/image_img.png);border:0px;')		
        self.butt2.setGeometry(500, 50, 400, 400) 
        self.butt2.clicked.connect(self.change_stack2)

        self.back = QPushButton(self)
        self.back.setStyleSheet('image:url(./img/back_img.png);border:0px;')	
        self.back.setGeometry(0, 0, 50, 50) 
        self.back.clicked.connect(self.change_stack3)

    def change_stack1(self):
        self.parent().stack.setCurrentIndex(5)

    def change_stack2(self):
        self.parent().stack.setCurrentIndex(6)

    def change_stack3(self):
        self.parent().stack.setCurrentIndex(0)

# 5 텍스트 디코딩 페이지
class SecondWidget4(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        layout = QtWidgets.QVBoxLayout(self)
        label1 = QLabel('입력', self)
        label1.setAlignment(Qt.AlignVCenter)
        label1.move(200, 30)

        label2 = QLabel('결과', self)
        label2.setAlignment(Qt.AlignVCenter)
        label2.move(710, 30)

        self.text_dox1 = QTextEdit(self)
        self.text_dox1.resize(350, 350)
        self.text_dox1.move(50, 60)

        self.text_dox2 = QTextBrowser(self)
        self.text_dox2.append('')
        self.text_dox2.setGeometry(550, 60, 350, 350) 

        self.dk_base64 = QPushButton("OK", self)	
        self.dk_base64.setGeometry(50, 420, 850, 45) 
        self.dk_base64.clicked.connect(self.base64_conversion)


        self.back = QPushButton(self)
        self.back.setStyleSheet('image:url(./img/back_img.png);border:0px;')	
        self.back.setGeometry(0, 0, 50, 50) 
        self.back.clicked.connect(self.change_stack1)

    
    def change_stack1(self):
        self.parent().stack.setCurrentIndex(4)

    def base64_conversion(self):
        # print(self.text_dox1.toPlainText())
        sitename_bytes = base64.b64decode(self.text_dox1.toPlainText())
        sitename = sitename_bytes.decode('utf-8')
        print(sitename)

        # 내용 초기화
        self.text_dox2.clear()
        self.text_dox2.repaint()

        self.text_dox2.append(str(sitename))


# 6 이미지 디코딩 페이지
class SecondWidget5(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.files = QPushButton("파일 선택", self)	
        self.files.setGeometry(50, 100, 850, 50) 
        self.files.clicked.connect(self.pushButtonClicked)

        self.files_encoding = QPushButton("OK", self)	
        self.files_encoding.setGeometry(800, 450, 100, 30) 
        self.files_encoding.clicked.connect(self.base64_files_encoding)

        self.back = QPushButton(self)
        self.back.setStyleSheet('image:url(./img/back_img.png);border:0px;')		
        self.back.setGeometry(0, 0, 50, 50) 
        self.back.clicked.connect(self.change_stack1)

    def change_stack1(self):
        self.parent().stack.setCurrentIndex(4)

    def pushButtonClicked(self):
        # self.FileOpen = QFileDialog.getOpenFileName(self, '열기', './')

        self.FileOpen = QFileDialog.getOpenFileName(self, 'Open File', '','Images (*.bin)')
        # self.files.setText(self.FileOpen[0])
        print(self.FileOpen[0])
    
    def base64_files_encoding(self):
        print(self.FileOpen[0])
        file = open(self.FileOpen[0], 'r')
        decoding = file.read()

        im = Image.open(BytesIO(base64.b64decode(decoding)))
        im.save('C:/Users/'+user_name+'/Desktop/b64decode_images.png', 'PNG')
        guidance = QMessageBox.information(self, 'base64(개발중)', '바탕화면에 b64decode_images.png 이 생성했습니다', QMessageBox.Ok)
        print("완료")

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('./img/handshake_2.ico'))
        self.setWindowTitle('base64변환기GUI')
        self.setGeometry(500, 300, 950, 500)

        self.stack = QtWidgets.QStackedLayout(self)
        self.stack1 = FirstWidget(self)
        self.stack2 = SecondWidget(self)
        self.stack3 = SecondWidget1(self)
        self.stack4 = SecondWidget2(self)
        self.stack5 = SecondWidget3(self)
        self.stack6 = SecondWidget4(self)
        self.stack7 = SecondWidget5(self)
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        self.stack.addWidget(self.stack4)
        self.stack.addWidget(self.stack5)
        self.stack.addWidget(self.stack6)
        self.stack.addWidget(self.stack7)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '종료', '창을 닫으시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
