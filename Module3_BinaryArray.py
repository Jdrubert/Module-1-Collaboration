class Solution:
    def binarysearch(self, arr, k):
        left = 0
        right = len(arr) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == k:
                result = mid
                right = mid - 1
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
                
        return result


if __name__ == "__main__":
    solution = Solution()
    arr1 = [1, 2, 3, 4, 5]
    print(solution.binarysearch(arr1, 3))

    arr2 = [1, 2, 2, 2, 3, 4]
    print(solution.binarysearch(arr2, 2))
    
    arr3 = [1, 2, 3, 4]
    print(solution.binarysearch(arr3, 5))