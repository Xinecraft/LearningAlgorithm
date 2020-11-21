class QuickUnion:
    def __init__(self, size):
        self.nodes = list(range(size))

    def root(self, i):
        while i != self.nodes[i]:
            i = self.nodes[i]
        return i

    def connected(self, first, second):
        return self.root(first) == self.root(second)

    def union(self, first, second):
        first_root_id = self.root(first)
        second_root_id = self.root(second)
        if first_root_id == second_root_id:
            return
        self.nodes[first_root_id] = second_root_id

    def print(self):
        print("[", end="")
        for i in range(len(self.nodes)):
            print("%s, " % i, end="")
        print("]")
        print(self.nodes)


# # Test
# test = QuickUnion(10)
# test.union(0, 1)
# test.union(1, 9)
# test.union(5, 6)
# test.union(5, 1)
# test.print()
#
# print(test.connected(5, 9))
