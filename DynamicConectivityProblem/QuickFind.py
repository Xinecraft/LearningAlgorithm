class QuickFind:
    def __init__(self, size):
        self.nodes = list(range(size))

    def connected(self, first, second):
        return self.nodes[first] == self.nodes[second]

    def union(self, first, second):
        if self.connected(first, second):
            return
        first_id = self.nodes[first]
        second_id = self.nodes[second]
        for i in range(len(self.nodes)):
            if self.nodes[i] == first_id:
                self.nodes[i] = second_id

    def print(self):
        print("[", end="")
        for i in range(len(self.nodes)):
            print("%s, " % i, end="")
        print("]")
        print(self.nodes)


# # Test
# test = QuickFind(10)
# test.union(0, 1)
# test.union(1, 9)
# test.union(5, 6)
# test.union(5, 1)
# test.print()
#
# print(test.connected(5, 9))
