# models/country.py
class Country:
    def __init__(self, name):
        self.name = name
        self.towns = []
        self.resources = 1000
        self.policies = {}

    def add_town(self, town):
        self.towns.append(town)

    def set_policy(self, policy_name, effect):
        self.policies[policy_name] = effect

    # 其他方法...
