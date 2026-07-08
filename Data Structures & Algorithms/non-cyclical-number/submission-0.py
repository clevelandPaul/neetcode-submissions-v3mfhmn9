class Solution:
    def isHappy(self, n: int) -> bool:
        s1 = set()
        curr_num = n
        while True:
            if curr_num==1:
                return True
            s1.add(curr_num)
            new_num = 0
            for s in str(curr_num):
                new_num += int(s)**2
            if new_num in s1:
                return False
            curr_num = new_num
        