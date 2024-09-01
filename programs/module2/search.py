from items import Rule, Node
from stack import Stack


class Search:
    def __init__(self, ruleArr: [Rule], inNodeArr: [Node]):
        self.ruleArr = ruleArr
        self.openNodeSt = Stack()
        self.openRule = []
        self.closeNode = inNodeArr
        self.closeRule = []
        self.prohibitedNode = []

        self.goalNode = None
        self.solutionFlg = 1
        self.noSolutionFlg = 1

    def run(self, goalNode: Node):
        self.goalNode = goalNode
        self.openNodeSt.push(goalNode)

        while self.solutionFlg and self.noSolutionFlg:
            self.sample_search()

    def sample_search(self):
        ruleCnt = 0

        for rule in self.ruleArr:
            currentNode = self.openNodeSt.peek()

            if rule.goalNode.number != currentNode.number:
                continue
            if rule.isClosed:
                continue
            if not rule.isNodeExist(currentNode):
                continue

            ruleCnt += 1
            self.openRule.append(rule)
            self.openNodeSt.pushArr(rule.nodeArr)

            # edge.used = True
            # self.opened.put(edge.startNode)
            # self.resultPath[edge.startNode.number] = edge.endNode.number
            # self.parentCounter = 1
            #
            # if edge.startNode.number == self.start:
            #     self.isSolutionNotFound = 0
            #     return