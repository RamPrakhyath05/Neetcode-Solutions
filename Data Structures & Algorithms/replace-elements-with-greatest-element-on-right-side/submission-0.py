class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = arr[-1]
        for i in range(len(arr)-1,-1,-1):
            temp = maximum
            if maximum < arr[i]:
                maximum = arr[i]
            arr[i] = temp
        arr[-1] = -1
        return arr