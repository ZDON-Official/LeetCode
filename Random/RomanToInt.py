class Solution:

    def romanToInt(self, s: str) -> int:
        Symbols = {"I": 1, "II": 2, "III": 3, "V": 5,"X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0

        s = s.upper()
       
        for i in range(0,len(s)):
            if i < len(s)-1:

                if(s[i+1] == 'V' and s[i] == 'I'):
                    ans -= 1
                    continue
                elif(s[i+1] == 'X' and s[i] == 'I'):
                    ans -= 1
                    continue

                if(s[i+1] == 'L' and s[i] == 'X'):
                    ans -= 10
                    continue
                elif(s[i+1] == 'C' and s[i] == 'X'):
                    ans -= 10
                    continue

                if(s[i+1] == 'D' and s[i] == 'C'):
                    ans -= 100
                    continue
                elif(s[i+1] == 'M' and s[i] == 'C'):
                    ans -= 100
                    continue

            ans += (Symbols.get(s[i]))

        return ans

a = Solution()

#print(a.romanToInt('III'))
#print(a.romanToInt('IV'))
#print(a.romanToInt('LVIII'))
print(a.romanToInt('MCMXCIV'))
