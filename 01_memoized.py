class Solution:
    def knapSack(self, W, wt, val, n):
        t=[[-1 for i in range(W+1)] for j in range(n+1)]   #got TLE if I use the maximum values of W and n given in constraints , so better to use n+1 and W+1 in GFG
        def memo(W,wt,val,n):
            if n == 0 or W == 0:
                return 0
            if t[n][W] != -1: #if present function's return value is already computed and stored in matrix 't'  then , return it without computing it again.
                return t[n][W]
            if wt[n - 1] <= W:
                t[n][W] = max(val[n - 1] + memo(W - wt[n - 1], wt, val, n - 1), memo(W, wt, val, n - 1))
                return t[n][W]
            if wt[n - 1] > W:
                t[n][W] = memo(W, wt, val, n - 1)
                return t[n][W]
        return memo(W,wt,val,n) 
