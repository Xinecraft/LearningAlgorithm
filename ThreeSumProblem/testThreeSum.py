import ThreeSumBruteForce
import ThreeSumWithSortSearch
import random

k = random.sample(range(-1000, 1000), 700)

print("ThreeSumBruteForce O(N^3): %s sets" % ThreeSumBruteForce.threeSumCount(k))
print("ThreeSumWithSortSearch O(N^2LogN): %s sets" % ThreeSumWithSortSearch.threeSumCount(k))
