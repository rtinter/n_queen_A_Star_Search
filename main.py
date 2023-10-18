class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.g = 0 if parent is None else parent.g + 1
        self.h = self.calculate_heuristic()
        self.f = self.g + self.h

    def calculate_heuristic(self):
        count = 0
        for i in range(len(self.state)):
            for j in range(i + 1, len(self.state)):
                if self.state[i] == self.state[j] or \
                        self.state[i] - i == self.state[j] - j or \
                        self.state[i] + i == self.state[j] + j:
                    count += 1
        return count

    def generate_children(self):
        children = []
        for i in range(len(self.state)):
            new_state = list(self.state)
            new_state[i] = (new_state[i] + 1) % len(self.state)
            children.append(Node(new_state, self))
        return children


def a_star_search(n):
    start = Node([0] * n)
    open_list = [start]
    closed_list = []

    while open_list:
        current = min(open_list, key=lambda x: x.f)

        # Printing the current node
        print("Exploring Node with f = {} (g = {}, h = {})".format(current.f, current.g, current.h))
        print_solution(current)

        if current.h == 0:
            return current

        open_list.remove(current)
        closed_list.append(current)

        for child in current.generate_children():
            if any(x.state == child.state for x in closed_list):
                continue

            if not any(x.state == child.state for x in open_list):
                open_list.append(child)
            else:
                existing = next(x for x in open_list if x.state == child.state)
                if child.g < existing.g:
                    open_list.remove(existing)
                    open_list.append(child)

    return None


def print_solution(node):
    board = [['-' for _ in range(len(node.state))] for _ in range(len(node.state))]
    for i, val in enumerate(node.state):
        board[val][i] = 'Q'
    for row in board:
        print(' '.join(row))
    print("\n" + "=" * 30 + "\n")


if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    result = a_star_search(n)
    if result:
        print("Final Solution:")
        print_solution(result)
    else:
        print("No solution found")

