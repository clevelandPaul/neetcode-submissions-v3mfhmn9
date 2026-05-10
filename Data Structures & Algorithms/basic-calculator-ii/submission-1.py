from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        s_lst = []
        for c in s:
            if c!=' ':
                s_lst.append(c)
        
        opr_lst = ['+', '-', '*', '/']
        lst = []
        i = 0
        while i<len(s_lst):
            if s_lst[i] in opr_lst:
                lst.append(s_lst[i])
                i+=1
            else:
                j = i+1
                while j<len(s_lst):
                    if s_lst[j] not in opr_lst:
                        j+=1
                    else:
                        break
                lst.append(int("".join(s_lst[i:j])))
                i = j
        
        i = 0
        while i<len(lst):
            if lst[i]=='*':
                new_res = lst[i-1]*lst[i+1]
                lst[i-1] = new_res
                lst.pop(i)
                lst.pop(i)
            elif lst[i]=='/':
                new_res = lst[i-1]//lst[i+1]
                lst[i-1] = new_res
                lst.pop(i)
                lst.pop(i)
            else:
                i+=1

        i = 0
        while i<len(lst):
            if lst[i]=='+':
                new_res = lst[i-1]+lst[i+1]
                lst[i-1] = new_res
                lst.pop(i)
                lst.pop(i)
            elif lst[i]=='-':
                new_res = lst[i-1]-lst[i+1]
                lst[i-1] = new_res
                lst.pop(i)
                lst.pop(i)
            else:
                i+=1
        return lst[0]