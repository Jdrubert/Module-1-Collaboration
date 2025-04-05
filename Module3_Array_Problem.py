class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        low = 0 
        mid = 0 
        high = len(arr) - 1 
        
        while mid <= high:
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

if __name__ == "__main__":
    solution = Solution()
    arr = [0, 1, 2, 0, 1, 2]
    solution.sort012(arr)
    print(arr)