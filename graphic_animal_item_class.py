from graphic_field_item_class import *

class AnimalGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    """this class provides a pixmap item with a preset image for the animal"""

    #constructor
    def __init__(self,graphics_list):
        super().__init__(graphics_list)

        self.animal = None

    def update_status(self):
        if self.animal._status == "Baby":
            self.setPixmap(QPixmap(self.available_graphics[0]).scaledToWidth(25,1))
        elif self.animal._status == "Poor":
            self.setPixmap(QPixmap(self.available_graphics[1]).scaledToWidth(25,1))
        elif self.animal._status == "Fine":
            self.setPixmap(QPixmap(self.available_graphics[2]).scaledToWidth(25,1))
        elif self.animal._status == "Prime":
            self.setPixmap(QPixmap(self.available_graphics[3]).scaledToWidth(25,1))

    def _remove_animal(self):
        self.scene().remove_animal(self)

    def needs(self):
        return self.animal.needs()

    def grow(self,feed,water):
        self.animal.grow(feed,water)

    def contextMenuEvent(self,event):
        menu = QMenu("Animal")
        remove = menu.addAction("Remove Animal")

        #connection
        remove.triggered.connect(self._remove_animal)

        #run menu
        menu.exec_(event.screenPos())
