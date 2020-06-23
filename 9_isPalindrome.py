class Solution:
    def isPalindrome(self, x: int) -> bool:
        flg = 0
        if x>=0:
            str_x = str(x)
            str_x_=str_x[::-1]
            flg = 1 if str_x==str_x_ else 0
        return True if flg==1 else False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        flg = 1
        if x>=0:
            x_str = str(x)
            for i in range(len(x_str)//2):
                if x_str[i]!=x_str[len(x_str)-i-1]:
                    flg = 0
                    break
                else:
                    continue
        else:
            flg = 0
        return True if flg==1 else False
