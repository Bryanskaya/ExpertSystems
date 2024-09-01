from queue import Queue
from typing import List

from items import Edge, Node


class GraphBFS:
    def __init__(self, edgeLst: List[Edge]):
        self.edgeLst = edgeLst
        self.opened = Queue()
        self.closed = list()
        self.goal = None
        self.isSolutionNotFound = 1
        self.childCounter = 1
        self.resultPath = {}

    def BFS(self, start: int, goal: int):
        self.opened.put(Node(start))
        self.goal = goal

        while self.childCounter and self.isSolutionNotFound:
            print("Current queue: ", end="")
            self.opened.print()
            
            self.sample_search()  # метод потомков
            if self.isSolutionNotFound == 0:  # решение найдено
                break

            currentNode = self.opened.get()
            self.closed.append(currentNode.number)

            if self.opened.length() != 0:
                self.childCounter = 1

        if self.isSolutionNotFound == 1:
            return None
        return self.getResultPath(start)

# Поиск по образцу (метод, находящий потомка для текущей подцели)
    def sample_search(self):
        self.childCounter = 0

        for edge in self.edgeLst:
            currentNode = self.opened.top()

            if edge.startNode.number != currentNode.number:
                continue
            if edge.used:
                continue
            if self.opened.isExist(edge.endNode.number) or edge.endNode.number in self.closed:
                continue

            edge.used = True
            self.opened.put(edge.endNode)
            self.resultPath[edge.endNode.number] = edge.startNode.number
            self.childCounter = 1

            if edge.endNode.number == self.goal:
                self.isSolutionNotFound = 0
                return


    def getResultPath(self, start: int):
        current = self.goal
        result = [current]
        while current != start:
            current = self.resultPath[current]
            result.append(current)
        return result

