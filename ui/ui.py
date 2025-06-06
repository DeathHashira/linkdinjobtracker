import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton, QStackedLayout, QFormLayout, QLabel, QRadioButton, 
    QButtonGroup, QCheckBox, QLineEdit
    )
from pyqt6_multiselect_combobox import MultiSelectComboBox
from PyQt6.QtCore import Qt
from ui.data import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Job Tracker')
        self.stacked_layout = QStackedLayout()

        self.page1 = QWidget()
        self.page2 = QWidget()
        self.page3 = QWidget()

        self.page1_layout = QFormLayout()
        self.page2_layout = QFormLayout()
        self.page3_layout = QFormLayout()

        self.page1.setLayout(self.page1_layout)
        self.page2.setLayout(self.page2_layout)
        self.page3.setLayout(self.page3_layout)

        # page 1 setup
            # row one
        self.label1 = QLabel('Please enter your job titles and skills')
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addRow(self.label1)

            # row two
        self.skills = MultiSelectComboBox()
        self.skills.addItems(linkedin_skills)
        self.titles = MultiSelectComboBox()
        self.titles.addItems(linkedin_job_titles)
        self.row12 = QHBoxLayout()
        self.row12.addWidget(QLabel('Titles'))
        self.row12.addWidget(self.titles)
        self.row12.addWidget(QLabel('Skills'))
        self.row12.addWidget(self.skills)
        self.page1_layout.addRow(self.row12)

            # row three
        self.filter = QPushButton('Filter Jobs')
        self.filter.clicked.connect(self.go_to_filter)
        self.search = QPushButton('Search')
        self.search.clicked.connect(self.check_scope)
        self.row13 = QHBoxLayout()
        self.row13.addWidget(self.search)
        self.row13.addWidget(self.filter)
        self.page1_layout.addRow(self.row13)

            # row four
        self.check = QLabel()
        self.check.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page1_layout.addRow(self.check)

        # page 2 setup
            # row one
        self.row21 = QHBoxLayout()
        self.button21 = QButtonGroup()
        self.rece = QRadioButton('Most recent')
        self.relev = QRadioButton('Most relevant')
        self.button21.addButton(self.rece)
        self.button21.addButton(self.relev)
        self.row21.addWidget(QLabel('Sort by: '))
        self.row21.addWidget(self.rece)
        self.row21.addWidget(self.relev)
        self.country = QLineEdit()
        self.row21.addWidget(QLabel('Country: '))
        self.row21.addWidget(self.country)
        self.page2_layout.addRow(self.row21)

            # row two
        self.button22 = QButtonGroup()
        self.anyt = QRadioButton('Any time')
        self.pasm = QRadioButton('Past month')
        self.pasw = QRadioButton('Past week')
        self.pash = QRadioButton('Past 24 hours')
        self.button22.addButton(self.anyt)
        self.button22.addButton(self.pasm)
        self.button22.addButton(self.pasw)
        self.button22.addButton(self.pash)
        self.row22 = QHBoxLayout()
        self.row22.addWidget(QLabel('Date pasted: '))
        self.row22.addWidget(self.anyt)
        self.row22.addWidget(self.pasm)
        self.row22.addWidget(self.pasw)
        self.row22.addWidget(self.pash)
        self.page2_layout.addRow(self.row22)

            # row three
        self.exprience = MultiSelectComboBox()
        self.exprience.setPlaceholderText('Exprience level')
        self.exprience.addItems(exprience_level)
        self.jobtype = MultiSelectComboBox()
        self.jobtype.setPlaceholderText('Job type')
        self.jobtype.addItems(job_type)
        self.remo = MultiSelectComboBox()
        self.remo.setPlaceholderText('Remote')
        self.remo.addItems(remote)
        self.row23 = QHBoxLayout()
        self.row23.addWidget(self.exprience)
        self.row23.addWidget(self.jobtype)
        self.row23.addWidget(self.remo)
        self.page2_layout.addRow(self.row23)

            # row four
        self.row24 = QHBoxLayout()
        self.easyapply = QCheckBox('Easy apply')
        self.hasverification = QCheckBox('Has verification')
        self.under = QCheckBox('Under 10 applicants')
        self.row24.addWidget(self.easyapply)
        self.row24.addWidget(self.hasverification)
        self.row24.addWidget(self.under)
        self.page2_layout.addRow(self.row24)

            # row five
        self.newsearch = QPushButton('Search')
        self.newsearch.clicked.connect(self.go_to_search)
        self.page2_layout.addRow(self.newsearch)

        # page 3 setup
            # row one
        self.start = QLabel('The process has been started')
        self.start.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page3_layout.addRow(self.start)

            # row two
        self.showjob = QLabel()
        self.showjob.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page3_layout.addRow(self.showjob)

            # row three
        self.showpage = QLabel()
        self.showpage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page3_layout.addRow(self.showpage)

            # row four
        self.workdon = QLabel()
        self.workdon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page3_layout.addRow(self.workdon)

        self.stacked_layout.addWidget(self.page1)
        self.stacked_layout.addWidget(self.page2)
        self.stacked_layout.addWidget(self.page3)
        self.stacked_layout.setCurrentIndex(0)

        central_widget = QWidget()
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)

    def check_scope(self):
        if len(self.skills.currentData()) == 0 and len(self.titles.currentData()) == 0:
            self.check.setText('Please choose at least one skill or title')
        else:
            self.go_to_search()

    def go_to_filter(self):
        self.stacked_layout.setCurrentIndex(1)

    def go_to_search(self):
        self.stacked_layout.setCurrentIndex(2)



app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
