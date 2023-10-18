import json
from datetime import datetime
import time
from graph import Graph


class Progress:
    def __init__(self, profile):
        f = open(profile)
        self.profile = json.load(f)
        f.close()

        self.netWage = self.profile['wage'] * (1 - self.profile['deductions'])
        self.goals = self.profile['goals']
        self.totalGoals = sum(self.goals.values())

        self.weekStart = datetime.now()
        self.startTime = datetime.now()
        self.endTime = datetime.now()
        self.duration = 0
        self.hours = 0
        self.running = False

        self.weeklyEarnings = 0
        self.durationEarnings = 0

    def start(self):
        self.running = True
        self.startTime = datetime.now()
        self.duration = 0
        self.durationEarnings = 0

    def end(self):
        self.running = False
        self.endTime = datetime.now()
        self.duration = self.endTime - self.startTime
        self.hours = self.duration.total_seconds()/3600
        self.durationEarnings = self.hours * self.netWage
        self.weeklyEarnings += self.durationEarnings

    def update(self, duration):
        self.start()
        time.sleep(duration)
        self.end()
        print("Duration Earnings: {val:.2f}".format(val=self.durationEarnings))
        print("Weekly Earnings: {val:.2f}".format(val=self.weeklyEarnings))


if __name__ == '__main__':
    progress = Progress("profile.json")
    graph = Graph(progress.goals)
    graph.update(progress.weeklyEarnings)
    graph.plot()

    #for _ in range(10):
        #progress.update(1)


