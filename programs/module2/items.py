from typing import List


class Node:
    def __init__(self, number: int, flag: int=0):
        self.number = number
        self.flag = flag

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


class Rule:
    def __init__(self, number: int, goalNode: Node, nodeArr: List[Node], isClosed: bool=False):
        self.number = number
        self.goalNode = goalNode
        self.nodeArr = nodeArr
        self.isClosed = isClosed

    def isNodeExist(self, node: Node):
        for inode in self.nodeArr:
            if inode.number == node.number:
                return True
        return False
