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
            # print("in else", magazine)
            ans = 0
            for i in ransomNote:
                if (i not in magazine):
                    # print("i is ", i)
                    # print("magazine is ", magazine)
                    # print("if is ", i not in magazine)
                    return False
                if len(magazine) == 0:
                    break

                for j in magazine:
                    if i == j:
                        ans += 1 
                        #magazine = magazine.translate({ord(j):None})
                        magazine = magazine.replace(j, '', 1)
                        # print("new ", magazine)
                        break
            # if ans == len(ransomNote):
            #     return True
            return True

        return False

sol = Solution()


a = "aa"
b = "ab"


# print(sol.canConstruct(a,b)) # false
print("")
print(sol.canConstruct("aab","baa")) # true
print("")
print(sol.canConstruct("aa","aba")) # true
