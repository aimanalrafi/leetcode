class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        i = len(s) - 1

        

        while i > -1:
            
            if s[i] != " ":
                word = []
                while s[i] != " " and i > -1:
                    # print(f"letter found: {s[i]}")
                    word.insert(0,s[i])
                    i -= 1 
                    
                
                # word.append(" ")
                # print(word)
                res.append("".join(word))
                
            else:
                # print(f"space found '{s[i]}'")
                i -= 1
            
            # if i == 0:
            #     break

            
        # print(res)
        # print(" ".join(res)[:len(s)])
        return " ".join(res)[:len(s)]


        # also possible solution. just two lines TT
        # x = s.split()
        # return " ".join(x[::-1])
                    
            
