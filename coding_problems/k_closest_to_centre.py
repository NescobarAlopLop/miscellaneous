from typing import List
import heapq


def get_distance_to_centre_squared_2d(point: List[int]) -> float:
    if len(point) == 2:
        return (0 - point[0]) ** 2 + (0 - point[1]) ** 2


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = heapq.heapify([])

        for point in points:
            heapq.heappush(res,)
            res.append([get_distance_to_centre_squared_2d(point), points])

        # sorted(res, key=dist)
        res.sort(key=lambda x: x[0])
        rv = [x[1] for x in res]

        if K > 1:
            return rv[:K + 1]
        else:
            return rv[0]


k_c = Solution()

print(k_c.kClosest([[1, 3], [-2, 2]], 1))
print(k_c.kClosest([[1, 3], [-2, 2]], 2))
