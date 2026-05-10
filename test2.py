class Student:
    def __init__(self, name):
        self.name = name
        self.money = 50
        self.progress = 0

    def live(self):
        for day in range(1, 366):
            if self.money < 20:
                self.money += 50  # Працює
            elif self.progress < 10:
                self.progress += 5  # Вчиться
                self.money -= 5
            else:
                self.money -= 10  # Відпочиває

            if self.money < 0: break  # Перевірка на банкрутство


s = Student("Олег")
s.live()
