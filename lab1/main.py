from graphBFS import GraphBFS
from graphDFS import GraphDFS
from items import Edge, Node


def show(arr: list):
    for i in range(len(arr) - 1, -1, -1):
        if i != 0:
            print(f'{arr[i]} -> ', end='')
        else:
            print(f'{arr[i]}')


class Example:
    def edgeLst_1(self):
        edgeLst = [
            Edge(Node(1), Node(2), 101),
            Edge(Node(1), Node(3), 102),
            Edge(Node(1), Node(4), 103),
            Edge(Node(2), Node(5), 104),
            Edge(Node(3), Node(4), 105),
            Edge(Node(4), Node(6), 106)
        ]
        return edgeLst

    def edgeLst_2(self):
        edgeLst = [
            Edge(Node(0), Node(1), 101),
            Edge(Node(0), Node(2), 102),
            Edge(Node(0), Node(3), 103),
            Edge(Node(1), Node(4), 104),
            Edge(Node(2), Node(4), 105),
            Edge(Node(2), Node(5), 106),
            Edge(Node(3), Node(5), 107),
            Edge(Node(3), Node(6), 108),
            Edge(Node(4), Node(8), 109),
            Edge(Node(5), Node(4), 110),
            Edge(Node(5), Node(7), 112),
            Edge(Node(5), Node(9), 111),
            Edge(Node(6), Node(7), 113),
            Edge(Node(7), Node(9), 115),
            Edge(Node(9), Node(8), 114)
        ]
        return edgeLst


if __name__ == "__main__":
    print("Методы поиска в графах пространства состояния")

    print("Метод поиска в глубину")
    edgeLst1 = Example().edgeLst_2()
    res = GraphDFS(edgeLst1).DFS(0, 7)
    res.show()

    print("Метод поиска в ширину")
    edgeLst2 = Example().edgeLst_2()
    res = GraphBFS(edgeLst2).BFS(0, 7)
    show(res)
