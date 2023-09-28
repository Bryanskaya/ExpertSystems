from queue import Queue
from typing import List

from items import Edge, Node


class GraphBFS:
    def __init__(self, edgeLst: List[Edge]):
        self.edgeLst = edgeLst
        self.opened = Queue()
        self.closed = list()
        self.start = None
        self.goal = None
        self.isSolutionNotFound = 1
        self.parentCounter = 1
        self.resultPath = {}

    def BFS(self, start: int, goal: int):
        self.opened.put(Node(goal))
        self.start = start
        self.goal = goal

        while self.parentCounter and self.isSolutionNotFound:
            self.opened.print()

            self.sample_search()
            if self.isSolutionNotFound == 0:  # решение найдено
                break

            currentNode = self.opened.get()
            self.closed.append(currentNode.number)

            if self.opened.length() != 0:
                self.parentCounter = 1

        if self.isSolutionNotFound == 1:
            return None
        return self.getResultPath(self.goal)

# Поиск родителей
    def sample_search(self):
        self.parentCounter = 0

        for edge in self.edgeLst:
            currentNode = self.opened.top()

            if edge.endNode.number != currentNode.number:
                continue
            if edge.used:
                continue
            if self.opened.isExist(edge.startNode.number) or edge.startNode.number in self.closed:
                continue

            edge.used = True
            self.opened.put(edge.startNode)
            self.resultPath[edge.startNode.number] = edge.endNode.number
            self.parentCounter = 1

            if edge.startNode.number == self.start:
                self.isSolutionNotFound = 0
                return

    def getResultPath(self, startNode: int):
        current = self.start
        result = [current]
        while current != startNode:
            current = self.resultPath[current]
            result.append(current)
        return result

