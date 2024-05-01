class Queue:
    def __init__(self):
        self.elements = []

    def length(self):
        return len(self.elements)
    
    def print(self):
        for i in range(self.length()):
            print(self.elements[i], end=" ")
        print()

    def put(self, element):
        self.elements.append(element)

    def get(self):
        if len(self.elements) == 0:
            return None
        return self.elements.pop(0)

    def top(self):
        if self.length() == 0:
            return None
        return self.elements[0]

    def isExist(self, item):
        for element in self.elements:
            if element.number == item:
                return True
        return False

    def __upgradeQueue(self, queue):
        while queue.length() != 0:
            self.put(queue.get())

    def show(self):
        tempQueue = Queue()
        while self.length() != 0:
            tempQueue.put(self.get())

        while tempQueue.length() != 0:
            element = tempQueue.get()
            self.put(element)
            if tempQueue.length() != 0:
                print(f'{element} -> ', end='')
            else:
                print(f'{element}')
