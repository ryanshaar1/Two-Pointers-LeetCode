class Solution(object):
    def isSubsequence(self, s, t):
        x=0
        if len(s)==0:
            return True
        for i in range(len(t)):
            if x < len(s) and s[x] == t[i]:
                x+=1
        return x==len(s)