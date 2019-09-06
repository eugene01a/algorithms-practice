'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 <=
 k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

# class MySolution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#          :type k: int
#         :rtype: List[int]
#         """
#         counts = {}
#         unums = set(nums)
#         for unum in unums:
#             counts[unum] = nums.count(unum)
#
#         def foo():
#             unum = max(unums, key=lambda unum: counts[unum])
#             unums.remove(unum)
#             return unum
#
#         return [foo() for i in range(k)]

class Solution(object):
    def topKFrequent(self, nums, k):
        def heapify(heap, i, n):
            l = i * 2 + 1
            r = i * 2 + 2
            maxidx = i
            if l < n and heap[l][0] > heap[i][0]:
                maxidx = l
            if r < n and heap[r][0] > heap[maxidx][0]:
                maxidx = r
            if maxidx != i:
                heap[maxidx], heap[i] = heap[i], heap[maxidx]
                heapify(heap, maxidx, n)

        counter = dict()
        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        heap = []
        for num in counter:
            heap.append((counter[num], num))
        for i in range(len(heap) // 2 - 1, -1, -1):
            heapify(heap, i, len(heap))

        res = []
        for i in range(1, k + 1):
            res.append(heap[0][1])
            heap[0] = heap[-i]
            heapify(heap, 0, len(heap) - i)
            print(heap)
        return res


for nums, k in [
    ([1,1,1,2,2,3], 2)
]:

    sol = Solution().topKFrequent(nums, k)
    print(sol)