# controllers/map_controller.py
class MapController:
    def __init__(self, model, view):
        self.model = model  # Map 或 Country 模型
        self.view = view    # MapView 视图

        # 初始化视图
        self.view.draw_map(self.model.towns)

        # 连接视图的事件到控制器的方法
        self.view.on_town_clicked = self.on_town_clicked

    def on_town_clicked(self, town):
        # 处理城镇点击事件，如显示城镇信息视图
        pass
