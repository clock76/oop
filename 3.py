class Counter:
    count = 0
    def start_from(self, start = 0):
     self.count = start

    def increment(self):
        self.count += 1

    def display(self):
        print("Текущий счет равен " + str(self.count))

    def reset(self):
        self.count = 0

c1 = Counter()
c1.start_from(4)
c1.increment()
c1.display()
c1.reset()
c1.display()

