class Solution(object):
    def canWinNim(self, n):
        """
        :type n:int
        :rtype: bool
        """
        if n <= 0:
            print("illegal iput")
        elif n <= 3:
            return True
        elif n < 5:
            return False
        else:
            if n % 4 == 0 
                return False
            else:
                return True
