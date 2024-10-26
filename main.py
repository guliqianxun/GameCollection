# main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from models.country import Country
from models.town import Town
from views.main_window import MainWindow
from controllers.main_controller import MainController

def main():
    app = QApplication(sys.argv)

    # 初始化模型
    country = Country('我的国家')
    town_a = Town('城镇A', (0, 0))
    town_b = Town('城镇B', (100, 0))
    country.add_town(town_a)
    country.add_town(town_b)

    # 初始化视图
    main_window = MainWindow()
    main_window.show()

    # 初始化控制器
    main_controller = MainController(country, main_window)

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
