class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        c = 0
        li = []
        for i in range(len(chars)):
            if chars[i] == chars[i-1]:
                continue
            for j in range(i , len(chars)):
                if chars[i] == chars[j] and j != len(chars)-1:
                    c += 1
                else:
                    if j == len(chars)-1:
                        c += 1
                    if c > 1:
                        li.append(chars[i])
                        if c > 9:
                            for k in str(c):
                                li.append(k)
                        else:
                            li.append(str(c))
                    else:
                        li.append((chars[i]))
                    c = 0
                    break
        return li
