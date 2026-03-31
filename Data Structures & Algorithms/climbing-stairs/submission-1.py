class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        one, two=1,1
        sum=0
        for i in range(n-1):
            sum=one+two
            one=two
            two=sum
        return two   
        '''
        memo=[-1]*n
        def dfs(i):
            if i==n:
                return True
            if i>n:
                return False
            if memo[i]!=-1:
                return memo[i]
            memo[i]=dfs(i+1)+dfs(i+2)
            return memo[i]
        return dfs(0)                 




        