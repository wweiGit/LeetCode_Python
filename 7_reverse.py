'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
 示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
'''
class Solution:
    def reverse(self, x: int) -> int:
        flag =1
        if x>=0: 
            recv_x = int(str(x)[::-1]) 
        else:
            flag=-1
            recv_x = int((str(x)[1:])[::-1])
        return flag*recv_x if flag*recv_x>=-2**31 and flag*recv_x<=2**31-1 else 0
