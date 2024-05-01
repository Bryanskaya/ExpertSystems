from typing import List

from items import Edge, Node
from stack import Stack


class GraphDFS:
    def __init__(self, edgeLst: List[Edge]):
        self.edgeLst = edgeLst
        self.opened = Stack()
        self.closed = list()
        self.goal = None
        self.isSolutionNotFound = 1
        self.childCounter = 1

    def DFS(self, start: int, goal: int):
        self.opened.push(Node(start))
        self.goal = goal

        while self.childCounter and self.isSolutionNotFound:
            print("Current stack: ", end="")
            self.opened.print()

            self.sample_search()
            if self.isSolutionNotFound == 0:
                break
            if self.childCounter == 0 and self.opened.length() > 1:
                currentNode = self.opened.pop()
                self.closed.append(currentNode.number)
                self.childCounter = 1
        if self.isSolutionNotFound == 1:
            return None
        return self.opened

# Поиск по образцу (метод, находящий потомка для текущей подцели)
    def sample_search(self):
        self.childCounter = 0

        for edge in self.edgeLst:
            currentNode = self.opened.peek()

            if edge.startNode.number != currentNode.number:
                continue
            if edge.used:
                continue
            if self.opened.isExist(edge.endNode.number) or edge.endNode.number in self.closed:
                continue

            edge.used = True
            self.opened.push(edge.endNode)
            self.childCounter = 1

            if edge.endNode.number == self.goal:
                self.isSolutionNotFound = 0
            return