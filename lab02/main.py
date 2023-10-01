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
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        node8 = Node(8)
        node9 = Node(9)

        node14 = Node(14)
        node11 = Node(11)
        node18 = Node(18)

        node31 = Node(31)



        return [
            Rule(105, node14, [node7, node9]),
            Rule(102, node7, [node3, node2, node4]),
            Rule(104, node3, [node8, node31]),
            Rule(101, node3, [node1, node2]),
            Rule(103, node4, [node5, node6]),
            Rule(106, node9, [node4, node18, node11])
        ]


if __name__ == "__main__":
    # edgeLst2 = Example().edgeLst_2()
    # res = GraphBFS(edgeLst2).BFS(4, 0)
    ruleArr = Example().edgeLst_1()
    res = Search(ruleArr, [Node(4)]).run(Node(14))

    # for i in range(10):
    #     print(i)
