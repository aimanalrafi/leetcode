class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if len(s) == 0:
        #     return True
        # elif len(s) == 1:
        #     if len(t) == 1 and s[0] == t[0]:
        #         return True
        #     elif len(t) == 1 and s[0] != t[0]:
        #         return False
        # elif len(t) == 0:
        #     return False

                
        p_s = 0
        p_t = 0
        # count = 0
        # res = []
        
        while p_s != len(s) and p_t != len(t):
            if s[p_s] == t[p_t]:
                p_s += 1
                p_t += 1
            else:
                p_t += 1


        return p_s == len(s)

        
        