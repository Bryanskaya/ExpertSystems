from items import Rule, Node, Label
from stack import Stack


# Reverse search from goal to deep
# Methods
# 1. reverse search (main)
# 2. find children for current goal
# 3. backtracking -- form list of prohibited nodes and rules
# 4. labeling
# 5. create search tree by list of closed rules
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
        self.no_label = 1

    def run(self, goal_node: Node, in_node_arr: [Node]):
        self.goal_node = goal_node
        self.open_node_st.push(goal_node)
        self.close_node_lst = in_node_arr

        while self.solution_flg and self.no_solution_flg:
            rule_cnt = self.child_search()

            # solution was found
            if self.solution_flg == 0:
                print("Solution was found")
                return

            if rule_cnt == 0 and self.open_node_st.length() < 2:
                self.no_solution_flg = 0
                print("Solution was not found")
            elif rule_cnt == 0:
                print("Backtracking process is going to be launched")
                self.backtracking()

    def child_search(self):
        cnt_rules = 0

        for rule in self.rule_arr:
            print(f'[Rule {rule.number}] Current rule')

            current_node = self.open_node_st.peek()
            print(f'[Node {current_node.number}]  Current node')

            if rule.label != Label.OPEN:
                print(f'[Rule {rule.number}] was already processed')
                print('-' * 128 + '\n')
                continue

            if rule.out_node == current_node:
                print(f'[Rule {rule.number}] has out node that equals goal one')

                rule.label = Label.VIEWED
                self.open_rule_lst.append(rule)
                is_new_goal_added = self.add_new_goal(rule.node_arr)
                if not is_new_goal_added:
                    print("Label process is going to be launched")
                    self.label()

                cnt_rules += 1
                self.print_info(rule)
                break

            if self.is_prohibited_node_exist(rule.node_arr):
                self.prohibited_rule_lst.append(rule)
                rule.label = Label.FORBIDDEN

                self.print_info(rule)
                continue

            self.print_info(rule)

        return cnt_rules

    def label(self):
        while True:
            rule = self.open_rule_lst.pop()
            self.close_rule_lst.append(rule)

            node = self.open_node_st.pop()
            self.close_node_lst.append(node)

            print(f'[Labelling] Rule {rule.number} was added to close rules')
            print(f'[Labelling] Node {node.number} was added to close nodes')

            if node == self.goal_node:
                self.solution_flg = 0
                return

            current_node = self.open_node_st.peek()
            current_rule = self.open_rule_lst[-1]
            if current_rule.out_node != current_node:
                return

    def backtracking(self):
        current_goal = self.open_node_st.pop()
        rule = self.open_rule_lst.pop()

        current_goal.flag = Label.FORBIDDEN
        self.prohibited_node_lst.append(current_goal)

        rule.label = Label.FORBIDDEN
        self.prohibited_rule_lst.append(rule)

        print(f'[Backtrack] Rule {rule.number} was added to prohibited rules')
        print(f'[Backtrack] Node {current_goal.number} was added to prohibited nodes')

        for node in rule.node_arr:
            print(f'[Backtrack] Node {node.number} should be removed from opened nodes')
            self.open_node_st.remove_element(node)
        print()

    def add_new_goal(self, node_arr: [Node]):
        new_goal_flg = False

        for node in node_arr[::-1]:
            if node not in self.close_node_lst:
                self.open_node_st.push(node)
                new_goal_flg = True
        return new_goal_flg

    def is_prohibited_node_exist(self, node_arr: [Node]):
        for node in node_arr:
            if node in self.prohibited_node_lst:
                return True
        return False

    def print_nodes(self, node_arr: [Node]):
        for node in node_arr:
            print(node, end=' ')
        print()

    def print_rules(self, rule_arr: [Rule]):
        for rule in rule_arr:
            print(rule.number, end=' ')
        print()

    def print_info(self, rule: Rule):
        print(f'[Rule {rule.number}] list of opened nodes: ', end='    ')
        self.open_node_st.show()
        print(f'[Rule {rule.number}] list of closed nodes: ', end='    ')
        self.print_nodes(self.close_node_lst)
        print(f'[Rule {rule.number}] list of prohibited nodes: ', end='')
        self.print_nodes(self.prohibited_node_lst)
        print(f'[Rule {rule.number}] list of opened rules: ', end='    ')
        self.print_rules(self.open_rule_lst)
        print(f'[Rule {rule.number}] list of closed rules: ', end='    ')
        self.print_rules(self.close_rule_lst)
        print(f'[Rule {rule.number}] list of prohibited rules: ', end='')
        self.print_rules(self.prohibited_rule_lst)

        print('-' * 128 + '\n')
