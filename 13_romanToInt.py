class Solution:
    def romanToInt(self, s: str) -> int:
        romanList = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = 0
        flg=0
        for i,roman in enumerate(s):
            if flg==1:
                flg = 0
                continue
            if i<len(s)-1 and romanList[s[i]]<romanList[s[i+1]]:
                result += romanList[s[i+1]]-romanList[s[i]]
                flg=1
            else:
                result += romanList[s[i]]
        return result
