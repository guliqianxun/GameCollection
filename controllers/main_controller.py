# controllers/main_controller.py
from controllers.map_controller import MapController

class MainController:
    def __init__(self, country, main_window):
        self.country = country
        self.main_window = main_window

        # 初始化地图控制器
        self.map_controller = MapController(self.country, self.main_window.map_view)

        # 这里可以添加其他控制器的初始化，如城镇管理、资源管理等