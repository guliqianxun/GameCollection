# views/map_view.py
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PySide6.QtGui import QPen, QColor
from PySide6.QtCore import Qt

class MapView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.town_items = {}  # {town: QGraphicsEllipseItem}

    def draw_map(self, towns):
        self.scene.clear()
        self.town_items.clear()

        for town in towns:
            x, y = town.position
            size = 10 + town.level * 2
            color = QColor(200, 200, 100)
            item = self.scene.addEllipse(x - size/2, y - size/2, size, size,
                                         QPen(Qt.black), color)
            self.town_items[town] = item

            # 连接信号槽
            town.data_changed.connect(self.update_town)

            # 添加点击事件
            item.setAcceptedMouseButtons(Qt.LeftButton)
            item.mousePressEvent = lambda event, t=town: self.on_town_clicked(event, t)

        # 绘制连接（边）...

    def update_town(self):
        # 更新城镇的显示，如大小、颜色等
        pass

    def on_town_clicked(self, event, town):
        # 发射信号或调用控制器的方法
        pass
        