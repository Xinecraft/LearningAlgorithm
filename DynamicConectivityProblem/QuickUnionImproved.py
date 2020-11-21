class QuickUnionImproved:
    def __init__(self, size):
        self.nodes = list(range(size))
        self.weight = [1] * size

    def root(self, i):
        while i != self.nodes[i]:
            self.nodes[i] = self.nodes[self.nodes[i]]       # Path Compression
            i = self.nodes[i]
        return i

    def connected(self, first, second):
        return self.root(first) == self.root(second)

    def union(self, first, second):
        first_root_id = self.root(first)
        second_root_id = self.root(second)
        if first_root_id == second_root_id:
            return
        if self.weight[first] < self.weight[second]:
            self.nodes[first] = second
            self.weight[second] += self.weight[first]
        else:
            self.nodes[second] = first
            self.weight[first] += self.weight[second]

    def print(self):
        print("[", end="")
        for i in range(len(self.nodes)):
            print("%s, " % i, end="")
        print("]")
        print(self.nodes)


# # Test
# test = QuickUnionImproved(10)
# test.union(0, 1)
# test.union(1, 9)
# test.union(5, 6)
# test.union(5, 1)
# test.print()
#
# print(test.connected(5, 9))
