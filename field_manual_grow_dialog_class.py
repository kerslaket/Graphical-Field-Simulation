from PyQt4.QtGui import *

class ManualGrowDialog(QDialog):
    """ this class creates a dialog to provide light,water,and food values"""

    def __init__(self):
        super().__init__()

        #create widgets
        self.water_spin_box = QSpinBox()
        self.light_spin_box = QSpinBox()
        self.food_spin_box = QSpinBox()

        self.submit_button = QPushButton("Manually Grow fild")

        #set up spin
        self.water_spin_box.setRange(0,10)
        self.light_spin_box.setRange(0,10)
        self.food_spin_box.setRange(0,100)

        self.water_spin_box.setSuffix("Water")
        self.light_spin_box.setSuffix("Light")
        self.food_spin_box.setSuffix("Food")

        self.water_spin_box.setValue(1)
        self.light_spin_box.setValue(1)
        self.food_spin_box.setValue(1)

        #create layout
        self.layout = QVBoxLayout()

        #add widgets to the layout
        self.layout.addWidget(self.light_spin_box)
        self.layout.addWidget(self.water_spin_box)
        self.layout.addWidget(self.food_spin_box)
        self.layout.addWidget(self.submit_button)

        #set the window layout
        self.setLayout(self.layout)

        #connections
        self.submit_button.clicked.connect(self.close)

    def get_values(self):
        return self.light_spin_box.value(), self.water_spin_box.value(), self.food_spin_box.value()
        
