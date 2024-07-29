# import pymysql
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QPlainTextEdit, QStackedLayout
from PyQt5.QtGui import QPixmap
###주석 추가
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button_box()
        self.resize(420, 560)
        self.show()

    def button_box(self):
        # 배경 이미지 설정
        self.background_label = QLabel(self)
        background_pixmap = QPixmap("H:/PythonProject/MySQL_control/vaperwave.gif")  # 이미지 경로를 설정하세요
        self.background_label.setPixmap(background_pixmap)
        self.background_label.setScaledContents(True)
        
        # 메인 레이아웃 설정
        self.main_layout = QVBoxLayout(self)
        
        # 스택 레이아웃 설정
        self.stacked_layout = QStackedLayout()
        
        # 백그라운드 레이아웃 설정
        self.background_layout = QVBoxLayout()
        self.background_layout.addWidget(self.background_label)
        
        # 메인 레이아웃에 백그라운드 레이아웃 추가
        self.stacked_layout.addLayout(self.background_layout)
        
        # 위젯 레이아웃 설정
        self.widget_layout = QVBoxLayout()
        
        # 텍스트 필드와 버튼 추가
        self.line_edit = QLineEdit()
        self.line_edit.setFixedSize(400, 20)
        self.text_edit = QPlainTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setFixedSize(400, 450)

        Btn1 = QPushButton('전체조회')
        Btn2 = QPushButton('제품검색')
        Btn3 = QPushButton('제품추가')
        Btn4 = QPushButton('제품수정')
        Btn5 = QPushButton('제품삭제')
        box_in = [Btn1, Btn2, Btn3, Btn4, Btn5]

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.line_edit)
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.text_edit)
        
        hbox4 = QHBoxLayout()
        hbox4.addWidget(QLabel(" Input ▼"))
        
        for i in box_in:
            hbox2.addWidget(i)
        hbox2.addStretch(1)

        self.widget_layout.addLayout(hbox3)
        self.widget_layout.addLayout(hbox4)
        self.widget_layout.addLayout(hbox1)
        self.widget_layout.addLayout(hbox2)
        self.widget_layout.addStretch(1)
        
        # 메인 레이아웃에 위젯 레이아웃 추가
        self.stacked_layout.addLayout(self.widget_layout)
        
        # 최종 레이아웃 설정
        self.main_layout.addLayout(self.stacked_layout)

        Btn1.clicked.connect(self.on_alloutput)
        Btn2.clicked.connect(self.on_search)
        Btn3.clicked.connect(self.on_add)
        Btn4.clicked.connect(self.on_modify)
        Btn5.clicked.connect(self.on_delete)


    def on_alloutput(self):     
        self.text_edit.clear()   
        input_text = self.line_edit.text()
        self.line_edit.clear()
        result=str(background.alloutput())
        self.text_edit.appendPlainText(result)
    


    def on_search(self):    
        self.text_edit.clear()    
        input_text = self.line_edit.text()        
        self.line_edit.clear()
        result=str(background.search(input_text))
        self.text_edit.appendPlainText(result)

    def on_add(self):
        self.text_edit.clear()
        input_text = self.line_edit.text()
        background.add(input_text)
        self.line_edit.clear()
        self.text_edit.appendPlainText("Trying Add")

    def on_modify(self):
        self.text_edit.clear()
        input_text = self.line_edit.text()
        background.modify(input_text,input_text)
        self.line_edit.clear()
        self.text_edit.appendPlainText("Trying Modify")

    def on_delete(self):
        self.text_edit.clear()
        input_text = self.line_edit.text()
        background.delete(input_text)
        self.line_edit.clear()
        self.text_edit.appendPlainText("Trying DELETE")

    #self.line_edit.text() -> 입력    self.text_edit.appendPlainText->출력


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   sys.exit(app.exec_())
