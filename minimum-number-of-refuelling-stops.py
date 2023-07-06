class Solution(object):
    #Priority Queue Approach
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        count = 0
        max_reach = startFuel
        index = 0
        pqueue = []

        while (max_reach<target):
            while(index < len(stations) and stations[index][0]<=max_reach):
                pqueue.append(stations[index][1])
                pqueue.sort()
                index+=1
            
            if pqueue == []:
                return -1
            
            max_reach+=pqueue.pop()
            count+=1


        return count