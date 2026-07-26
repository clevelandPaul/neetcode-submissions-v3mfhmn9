class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        # 在能跳到的位置中，跳到i+j+nums[i+j]最大的地方
        count = 0
        i = 0
        while i<len(nums)-1:
            max_num = -float('Inf')
            next_pos = -1
            for j in range(1, nums[i]+1): # 可行的，所以不会跳到0
                if i+j>=len(nums)-1:
                    return count+1
                if i+j+nums[i+j]>=max_num:
                    max_num = i+j+nums[i+j]
                    next_pos = i+j
            count += 1
            i = next_pos
        return count
        '''
        






























        cur_pos = 0
        steps = 0
        while cur_pos<len(nums)-1:
            if cur_pos+nums[cur_pos]>=len(nums)-1:
                return steps+1
            new_stop = cur_pos
            max_dist = cur_pos+nums[cur_pos]
            for j in range(nums[cur_pos]+1):
                if cur_pos+j+nums[cur_pos+j]>max_dist:
                    new_stop = cur_pos+j
                    max_dist = cur_pos+j+nums[cur_pos+j]
            steps+=1
            cur_pos = new_stop
        return steps
