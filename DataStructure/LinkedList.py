class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class SLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def insert(self, data):
        node = SNode(data)
        if not self.head:
            self.head = node
            return

        current_node = self.head
        while True:
            if not current_node.next:
                current_node.next = node
                break
            current_node = current_node.next

    def isEmpty(self):
        return self.head is None
