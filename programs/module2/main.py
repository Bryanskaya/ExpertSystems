from graphBFS import GraphBFS
from items import Edge, Node, Rule
from search import Search


def show(arr: list):
    if arr is None:
        print("Not found")
        return
    for i in range(len(arr) - 1, -1, -1):
        if i != 0:
            print(f'{arr[i]} <- ', end='')
        else:
            print(f'{arr[i]}')


class Example:
    def edgeLst_1(self):
        node105 = Node(105)
        node7 = Node(7)
        node9 = Node(9)
        node102 = Node(102)
        node3 = Node(3)
        node4 = Node(4)
        node14 = Node(14)


        return [
            Rule(105, node105, [node7, node9]),
            Rule(102, node102, [node3, node4])
        ]


if __name__ == "__main__":
    # edgeLst2 = Example().edgeLst_2()
    # res = GraphBFS(edgeLst2).BFS(4, 0)
    ruleArr = Example().edgeLst_1()
    res = Search(ruleArr, [Node(4)]).run(Node(14))
