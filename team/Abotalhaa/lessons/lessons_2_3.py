class Solution(object):
    def longestCommonPrefix(self, strs):

        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        current = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            if len(current) == 0:
                break
            for j in range(len(strs[i])):
                if j < len(current) and current[j] == strs[i][j]:
                    temp += current[j]
                else:
                    break
            current = temp
        return current


input_list = ['flower', 'flower', 'flower']
ob1 = Solution()
print(ob1.longestCommonPrefix(input_list))
