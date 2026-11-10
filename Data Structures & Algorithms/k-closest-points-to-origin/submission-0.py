
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        l = []

        for coordinates in points:
            distance = coordinates[0]**2 + coordinates[1]**2

            if len(heap) < k:
                heapq.heappush(heap, (-distance, coordinates))

            elif heap[0][0] < -distance:
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance, coordinates))

        for point in heap:
            l.append(point[1])

        return l
