from PyQt4.QtGui import *

class FieldReportDialog(QDialog):
    """his clss creates a report for the field"""

    #constructor
    def __init__(self,report):
        super().__init__()
        self.setWindowitle("Fied Report")

        #labels for the crop stats
        self.crop_type_label = QLabel("Crop Type")
        self.crop_status_label = QLabel("Crop Status")
        self.crop_days_growing_label = QLabel("Days Growing")
        self.crop_growth_label = QLabel("Growth")

        #labls for the animal stats
        self.animal_type_label = QLabel("Animal Type")
        self.animal_status_label - QLabel("Anmal Status")
        self.animal_days_growing_label = QLabel("Days Growing")
        self.animal_weight_label = QLabel("Weight")

        #labels for other cases
        self.no_crops_label = QLabel("There are no crops in this field")
        self.no_animals_label = QLabel("There are no animals in this field")
        self.nothing_label = QLabel("This field is empty")

        self.close_button = QPushButton("Dismiss Report")

        #layouts
        self.report_layout = QGridLayout()
        self.layout = QVBoxLayout()

        row = 1

        if len(report["crops"]) == 0 and len(report["animals"]) == 0:
            self.report_layout.addWidget(self.nothing_label,0,0)
        else:
            if len(report["crops"]) > 0:
                .report_layout.addWidget(self.crop_type_label,0,0)
                
                                                   
