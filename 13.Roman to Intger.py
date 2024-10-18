class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0

        roman = {        #first time I used dictonaries
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for a,b in zip(s,s[1:]):    # this zip function was very clever at mixing and using tuples. 

            if roman[a]>=roman[b]:

                res += roman[a]
            else:
                res-=roman[a]


        return res + roman[s[-1]]   
            
