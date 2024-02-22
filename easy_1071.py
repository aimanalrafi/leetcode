class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        isPrime = True
        sum = len(str1) + len(str2)
        # if each one letter
        if sum == 2:
            if str2[0] == str1[0]:
                return str2[0]
            else:
                return ""

        i = 0
        for i in range(2, int(sum**0.5) + 1):
            if sum % i == 0:
                isPrime = False

        a = max(len(str1), len(str2))
        b = min(len(str1), len(str2))
        # Euclidian Algorithm
        while b:
            a, b = b, a % b
        
        # handle case: all letters are the same, if sum is prime, return letter_check. If not, then gcd
        case = 0 # all same letters
        letter_check = str1[0]
        x = 0
        for letter in str1:
            if letter != letter_check:
                case = 1
        for letter in str2:
            if letter != letter_check:
                case = 1


        if case == 0:
            if isPrime == True:
                print(f"case 0 (prime): gcd is {letter_check}")
                return letter_check
            else:
                print(f"case 0: gcd is {letter_check * a}")
                return letter_check * a
        # different letters
        elif case == 1:
            # if its different letters, and the sum is prime, return ""
            if isPrime == True:
                return ""
            else:
                gcd = str1[:a]
                print(f"case 1: gcd is {gcd}")
                print(f"len(str1): {len(str1)}, len(str2): {len(str2)}, {int(len(str1)/len(gcd))}")
                # mirror the gcd to be as long as both strings, and compare each string, if diff then return ""
                check_str1 = gcd * int(len(str1)/len(gcd))
                check_str2 = gcd * int(len(str2)/len(gcd))

                if (check_str1 == str1) and (check_str2 == str2):
                    return gcd
                else:
                    return ""



                 


