class Solution:
    def compress(self, chars: List[str]) -> int:
        # read: 扫描原数组，找到每一段连续相同字符
        # write: 把压缩后的结果写回chars
        read = 0
        write = 0
        n = len(chars)

        while read<n:
            curr_char = chars[read]
            count = 0

            while read<n and chars[read]==curr_char:
                read+=1
                count+=1

            chars[write] = curr_char
            write += 1
            if count>1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

        