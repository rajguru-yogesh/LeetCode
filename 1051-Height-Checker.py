'''
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

 

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3

 

Constraints:

    1 <= heights.length <= 100
    1 <= heights[i] <= 100


'''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return 0
        arr = [i for i in heights]
        res = 0
        for i in range(len(arr)-1, 0, -1):
            flag = True
            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    flag = False
            if flag:
                break
        for i in range(len(heights)):
            if heights[i] != arr[i]:
                res += 1
        return res
            