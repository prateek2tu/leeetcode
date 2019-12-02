class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        n = len(arr)
        ans = ''
        if n == 0:
            return ans
        mini = min(arr, key=len)
        for i in range(len(mini)):
            curr = mini[i]
            if any(arr[j][i] != curr for j in range(n)):
                break
            ans += curr
        return ans
