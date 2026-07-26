class TimeMap:

    def __init__(self):

        self.key_dict = {} # key: [timestamp, value]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_dict:
            self.key_dict[key] = [[timestamp, value]]
        else:
            self.key_dict[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_dict:
            return ""
        target_lst = self.key_dict[key]
        i = 0
        j = len(target_lst)-1
        while i<=j:
            mid = (i+j)//2
            if target_lst[mid][0]==timestamp:
                return target_lst[mid][1]
            elif target_lst[mid][0]<timestamp:
                i = mid+1
            else:
                j = mid-1
        
        if j<0 or j>=len(target_lst):
            return ""
        else:
            return target_lst[j][1]
        
        
