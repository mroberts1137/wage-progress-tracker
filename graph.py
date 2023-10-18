import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self, goals):
        self.goals = goals
        self.weeklyEarnings = 0
        print(self.goals)

    def update(self, earnings):
        self.weeklyEarnings = earnings

    def plot(self):
        fig, ax = plt.subplots()

        bottom = 0
        for goal, value in self.goals.items():
            p = ax.bar(x=0, height=value, width=1, bottom=bottom)
            bottom += value

        plt.show()