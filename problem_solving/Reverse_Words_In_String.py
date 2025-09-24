class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = ''
        li = []
        for i in s:
            if i != ' ':
                st += i
            else:
                if st != '':
                    li.append(st)
                    st = ''
        if st != '':
            li.append(st)
        li.reverse()
        return ' '.join(li)

s = 'a good   example'
s1 = Solution()
print(s1.reverseWords(s))
        