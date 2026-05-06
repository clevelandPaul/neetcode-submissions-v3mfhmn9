class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 使用差分数组+前缀和
        # 差分数组记录在某个位置，人数变化了多少
        diff = [0 for _ in range(1001)]
        for num, start, end in trips:
            diff[start] += num
            diff[end] -= num
        curr_people = 0
        for d in diff:
            curr_people += d
            if curr_people > capacity:
                return False
        return True


        '''
        # 第3个位置记录是start time: 1, 还是end time: 0
        # end time需要排到start time前面
        # arr.sort(key=lambda x: 0 if x[1] == "start" else 1)
        start_time = [[i, trips[i][1], 1] for i in range(len(trips))]
        end_time = [[i, trips[i][2], 0] for i in range(len(trips))]
        total_time = start_time + end_time
        total_time.sort(key=lambda x: x[2])
        total_time.sort(key=lambda x: x[1])

        curr_people = 0
        n = len(total_time)
        print(total_time)
        curr_time = 0
        for i in range(n):
            curr_time = total_time[i][1]
            if total_time[i][2]==1: # start time
                curr_people += trips[total_time[i][0]][0]
                if curr_people>capacity:
                    return False
            else:
                curr_people -= trips[total_time[i][0]][0]
        return True
        '''

        