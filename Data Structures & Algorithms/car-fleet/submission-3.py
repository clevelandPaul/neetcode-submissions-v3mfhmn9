class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[position[i], speed[i]] for i in range(len(position))]
        pair.sort(key=lambda x: x[0])
        count = 1
        curr_pos, curr_speed = pair[-1][0], pair[-1][1]
        for i in range(len(pair)-2, -1, -1):
            if pair[i][1]==curr_speed and pair[i][0]==curr_pos:
                continue
            if pair[i][1]<=curr_speed: # can't catch up
                curr_speed = pair[i][1]
                curr_pos = pair[i][0]
                count += 1
            else:
                if (target-curr_pos)/curr_speed * pair[i][1]-target+pair[i][0]>=0: # can catch up
                    # curr_speed = pair[i][1]
                    # curr_pos = pair[i][0]
                    continue
                else:
                    curr_speed = pair[i][1]
                    curr_pos = pair[i][0]
                    count += 1
        
        return count

