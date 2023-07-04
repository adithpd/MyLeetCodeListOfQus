class Solution(object):
    #Sliding Window Approach
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        lsum, rsum = 0, sum(cardPoints[-k:])
        summ = rsum
        for i in range(k):
            lsum += cardPoints[i]
            rsum -= cardPoints[-k+i]
            summ = max(summ, lsum + rsum)
            print(lsum, rsum)
        return summ


class Solution(object):
    #Sliding Window Approach
    #More Efficient
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, len(cardPoints) - k
        total = sum(cardPoints[r:])
        res = total

        while r < len(cardPoints):
            total+=(-cardPoints[r]+cardPoints[l])
            res = max(res,total)
            l+=1
            r+=1
        return res
