class Solution:
    def minimumSwap(self, A: str, B: str) -> int:
        
        dx = dy = 0
        for i, b in enumerate(B):
            if b != A[i]:
                if b == 'x':
                    dx += 1
                else:
                    dy += 1
        
        if dx % 2 == 0 and dy % 2 == 1 or dx % 2 == 1 and dy % 2 == 0:
            return -1
        
        return dx // 2 + dy // 2 + 2 * (dx % 2)
