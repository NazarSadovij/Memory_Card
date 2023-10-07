from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QHBoxLayout, QVBoxLayout, QSpinBox, QPushButton

card_width, card_height = 600, 500
win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle("Memory Card")

menu_btn = QPushButton("Меню")
rest_btn = QPushButton("Відпочити")
time_box = QSpinBox()
time_box.setValue(50)
time_lb = QLabel("хвилин")

line1 = QHBoxLayout()
line1.addWidget(menu_btn)
line1.addStretch(1)
line1.addWidget(rest_btn)
line1.addWidget(time_box)
line1.addWidget(time_lb)



main_line  =QVBoxLayout()
main_line.addLayout(line1)
win_card.setLayout(main_line)