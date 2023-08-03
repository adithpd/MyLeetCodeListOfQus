class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        pq = []
        heapq.heapify(pq)
        for index in range(len(points)):
            x, y = points[index][0], points[index][1]
            distance = (x*x+y*y)**0.5
            heapq.heappush(pq,[distance, index])
        
        answer = []
        for _ in range(k):
            answer.append(points[heapq.heappop(pq)[1]])
        
        return answer