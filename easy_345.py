class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        # vowels_s = [vowel for vowel in s if vowel in vowels]
        # print(vowels_s)

        s = list(s)

        left = 0
        right = len(s) - 1
        tmp = 'a'
        
        

        while left < right:
            # v_right, v_left = 'x', 'x'
            # if s[left] not in vowels:
            #     left += 1
            # else:
            #     v_left = s[left]
            # if s[right] not in vowels:
            #     right -= 1
            # else:
            #     v_right = s[right]
            while left<right and s[left] not in vowels:
                left+=1
                # v_left = s[left]
            while left<right and s[right] not in vowels:
                right-=1
                # v_right = s[right]

            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1

            # if v_left != 'x' and v_right != 'x':
            #     print(f"swapping {v_left} with {v_right}")
            #     tmp = v_left
            #     s[left] = v_right
            #     s[right] = tmp
            #     left += 1
            #     right -= 1

        return "".join(s)

            
            