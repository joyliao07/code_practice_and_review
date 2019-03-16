class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        
        if x < 0:
            neg = True
            x = x * -1
            
        new_num = []
        new_int = 0
        
        position = 10
        while x > 0:
            digit = x % position
            new_num.append(int(digit/(position/10)))
            x -= digit
            position *= 10
        new_num = new_num[::-1]
        
        position = 1
        for what in new_num:
            new_int += (what * position)
            position *= 10
        
        if neg == True:
            new_int = new_int * -1
        
        if new_int > 2147483649 or new_int < -2147483649:
            new_int = 0
        
        return new_int
