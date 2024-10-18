class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x<0:     #FRT
            return False
        else:    
            temp= x
            for i in range((len(x))):  # cant decide loop
            digit= temp%10
            number= digit/10
            reverse = reverse + number        # dont know how to add integer to the end of an integer
            
