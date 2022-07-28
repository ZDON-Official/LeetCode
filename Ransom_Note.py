class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote.lower()
        magazine.lower()

        if len(ransomNote) == len(magazine) == 1 and ransomNote != magazine:
            return False
        elif len(ransomNote) > len(magazine):
            return False
        elif ransomNote in magazine:
            return True
        else:
            ans = 0
            for i in ransomNote:
                if (i not in magazine):
                    return False
                if len(magazine) == 0:
                    break

                for j in magazine:
                    if i == j:
                        ans += 1 
                        magazine = magazine.replace(j, '', 1)
                        break
            return True

        return False

sol = Solution()


a = "aa"
b = "ab"


print(sol.canConstruct(a,b)) # false
print("")
print(sol.canConstruct("aab","baa")) # true
print("")
print(sol.canConstruct("aa","aba")) # true
