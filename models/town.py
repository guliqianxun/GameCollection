# models/town.py
from PySide6.QtCore import QObject, Signal
import math

class Town(QObject):
    # 定义信号，当属性变化时发出
    data_changed = Signal()

    def __init__(self, name, position):
        super().__init__()
        self.name = name
        self.position = position  # (x, y)
        self.population = 50
        self.military = 20
        self.culture = 30
        self.politics = 25
        self.economy = 40
        self.level = 1
        self.connections = {}  # {neighbor_town: connection_type}

    def calculate_influence(self, other_towns):
        influence = 0
        for town in other_towns:
            if town != self:
                distance = self.get_distance(town)
                influence += town.get_total_attribute() / distance
        return influence

    def get_total_attribute(self):
        return (self.population + self.military + 
                self.culture + self.politics + self.economy)

    def get_distance(self, other_town):
        x1, y1 = self.position
        x2, y2 = other_town.position
        return math.hypot(x1 - x2, y1 - y2)

    def update_level(self, surrounding_influence):
        own_influence = self.get_total_attribute()
        if own_influence > surrounding_influence:
            self.level += 1
            self.data_changed.emit()  # 发出数据变化的信号

    # 其他方法...
