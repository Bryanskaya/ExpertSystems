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
            rule = self.sample_search()
            if rule is None:
                self.noSolutionFlg = 0
                #back


    def sample_search(self):
        ruleCnt = 0

        for rule in self.ruleArr:
            currentNode = self.openNodeSt.peek()

            if rule.goalNode.number != currentNode.number:
                continue
            if rule.isClosed:
                continue

            ruleCnt += 1
            self.openRule.append(rule)
            self.openNodeSt.pushArr(rule.nodeArr)

            return rule
        return None