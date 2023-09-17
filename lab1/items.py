class Node:
    def __init__(self, number: int):
        self.number = number

    def __str__(self):
        res = '' + f'{self.number}'
        return res

    def __repr__(self):
        res = '' + f'{self.number}'
        return res


class Edge:
    def __init__(self, startNode: Node, endNode: Node, label):
        self.startNode = startNode
        self.endNode = endNode
        self.label = label
        self.used = False
