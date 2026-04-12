class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# connect nodes
n1.next = n2
n2.next = n3

head = n1


def print_list(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next


print_list(head)
