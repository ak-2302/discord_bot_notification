import random


class Dice:
    def __init__(self, text):
        self.text = text
        self.output = ""
        self.do = False
        self.result = []
        self.dice = []
        self.analyze()
        if self.do:
            self.output = "result :"
            self.roll()

    def analyze(self):
        if "d" in self.text:
            self.dice = self.text.split("d")
            self.do = True
        elif "D" in self.text:
            self.dice = self.text.split("D")
            self.do = True
        else:
            return
        if self.dice[0].isdecimal() and self.dice[1].isdecimal():
            self.do = True
            return

    def roll(self):
        for i in range(int(self.dice[0])):
            self.result.append(random.randint(1, int(self.dice[1])))
        for i in self.result:
            self.output += " " + str(i)
        self.output += "\n"
        self.output += "sum:" + str(sum(self.result))
        return self.output
