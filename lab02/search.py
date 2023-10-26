from items import Rule, Node, Label
from stack import Stack


# Breadth-first search method from data to goal
# (include parent method -- looks for closed rules)
class Search:
    def __init__(self, rule_arr: [Rule]):
        self.rule_arr = rule_arr  # база знаний
        self.open_node_st = Stack()
        self.open_rule_lst = []
        self.close_node_lst = []
        self.close_rule_lst = []
        self.prohibited_node_lst = []
        self.prohibited_rule_lst = []

        self.goal_node = None
        self.solution_flg = 1
        self.no_solution_flg = 1

    def run(self, goal_node: Node, in_node_arr: [Node]):
        self.goal_node = goal_node
        self.open_node_st.push(goal_node)
        self.close_node_lst = in_node_arr

        while self.solution_flg and self.no_solution_flg:
            rule_cnt = self.parent_search()

            # solution was found
            if self.solution_flg == 0:
                return

            if rule_cnt == 0:
                self.no_solution_flg = 0
                print("Solution was not found")

    '''
    Return value: count of rules
    0 -- no solution
    solution was found
    middle -- part of rules were proved
    '''
    def parent_search(self):
        cnt_rules = 0

        for rule in self.rule_arr:
            print(f'[Rule {rule.number}] Current rule')
            if self.solution_flg:
                if rule.label != Label.OPEN:
                    print(f'[Rule {rule.number}] was already processed')
                    print('-' * 128 + '\n')
                    continue

                # Is set of input node covered closed nodes
                if self.is_close_nodes_cover(rule.node_arr):
                    print(f'[Rule {rule.number}] has set of input nodes all in closed nodes')

                    rule.label = Label.CLOSE
                    self.close_rule_lst.append(rule)
                    self.close_node_lst.append(rule.out_node)
                    self.set_nodes_closed(rule.node_arr)

                    # rule was proved, check its out node
                    if rule.out_node == self.goal_node:
                        self.solution_flg = 0
                        print(f'[Rule {rule.number}] has output node equal to goal one')

                    cnt_rules += 1
                else:
                    print(f'[Rule {rule.number}] does not have all closed input nodes')
            else:
                print(f'[Rule {rule.number}] solution was found')
                break

            print(f'[Rule {rule.number}] list of closed rules: ', end='')
            self.print_rules(self.close_rule_lst)
            print(f'[Rule {rule.number}] list of closed nodes: ', end='')
            self.print_nodes(self.close_node_lst)
            print('-' * 128 + '\n')

        print(f'{cnt_rules} rules were proved')
        return cnt_rules

    def is_close_nodes_cover(self, in_node_arr: [Node]):
        for node in in_node_arr:
            if node not in self.close_node_lst:
                return False
        return True

    def set_nodes_closed(self, node_arr):
        for node in node_arr:
            node.flag = Label.CLOSE

    def print_rules(self, rule_arr: [Rule]):
        for rule in rule_arr:
            print(rule.number, end=' ')
        print()

    def print_nodes(self, node_arr: [Node]):
        for node in node_arr:
            print(node, end=' ')
        print()