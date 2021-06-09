import unittest


res = []

def subsetsUtil(A, subset, index):
    print(*subset)
    global res
    res.append(list(subset))
    for i in range(index, len(A)):
        # include the A[i] in subset.
        subset.append(A[i])

        # move onto the next element.
        subsetsUtil(A, subset, i + 1)

        # exclude the A[i] from subset and
        # triggers backtracking.
        subset.pop(-1)
    return


# below function returns the subsets of vector A.
def subsets(A):
    global res
    subset = []

    # keeps track of current element in vector A
    index = 0
    subsetsUtil(A, subset, index)

    return res


def maxSubsetSum(arr):
    result = float('-inf')
    global res

    res = []

    for subset in subsets(arr):
        result = max(result, sum(subset))

    return result


class TestSolution(unittest.TestCase):
    def test_0(self):
        self.assertEqual(
            first=13,
            second=maxSubsetSum(
                arr=[3, 7, 4, 6, 5],
            ),
        )

    def test_1(self):
        self.assertEqual(
            first=11,
            second=maxSubsetSum(
                arr=[2, 1, 5, 8, 4],
            ),
        )

    def test_2(self):
        self.assertEqual(
            first=15,
            second=maxSubsetSum(
                arr=[3, 5, -7, 8, 10],
            ),
        )


if __name__ == '__main__':
    unittest.main()
