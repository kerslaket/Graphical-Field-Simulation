import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from graphic_field_scene_class import *
from graphic_wheat_item_class import *
from graphic_potato_item_class import *
from graphic_cow_item_class import *
from graphic_sheep_item_class import *

def main():
    field_simulation = QApplication(sys.argv) #create new application
    field_window = FieldWindow() #create new instance of main window
    field_window.show()#make instance visible
    field_window.raise_() #raise instance to top of window stack
    field_fsimulation.exec_() #monitor application for events
    
