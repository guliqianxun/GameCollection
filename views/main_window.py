# views/main_window.py
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from views.map_view import MapView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("国家模拟器")
        self.setGeometry(100, 100, 800, 600)

        # 创建中央部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建并添加地图视图
        self.map_view = MapView()
        layout.addWidget(self.map_view)

        # 这里可以添加其他UI元素，如工具栏、状态栏等