class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        res = [0 for _ in range(len(days)+1)] # 第0天是0
        res[1] = min(costs)
        for i in range(1, len(days)):
            res[i+1] = res[i]+costs[0]
            if days[i]-7>=0:
                j = 0
                while j<i:
                    if days[j]<=days[i]-7:
                        j+=1
                    else:
                        break
                res[i+1] = min(res[i+1], res[j]+costs[1])
            else:
                res[i+1] = min(res[i+1], costs[1])

            if days[i]-30>=0:
                j = 0
                while j<i:
                    if days[j]<=days[i]-30:
                        j+=1
                    else:
                        break
                res[i+1] = min(res[i+1], res[j]+costs[2])
            else:
                res[i+1] = min(res[i+1], costs[2])
        
        return res[-1]

        