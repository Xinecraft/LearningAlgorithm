import ThreeSumBruteForce
import ThreeSumWithSortSearch
import random

# This only work for Distinct array right now. ThreeSumWithSortSearch dont work on distinct.
k = random.sample(range(-1200, 1200), 1000)

print("ThreeSumBruteForce O(N^3): %s sets" % ThreeSumBruteForce.threeSumCount(k))
print("ThreeSumWithSortSearch O(N^2LogN): %s sets" % ThreeSumWithSortSearch.threeSumCount(k))
