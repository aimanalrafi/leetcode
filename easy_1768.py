class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result_string = ""
        
        if len(word1) < len(word2):
            shorterWord = word1
            longerWord = word2
        elif(len(word1) > len(word2)):
            shorterWord = word2
            longerWord = word1
        elif(len(word1) == len(word2)):
            shorterWord = word1
        
        l = 0
        while l < len(shorterWord):
            result_string += word1[l]
            result_string += word2[l]
            l += 1

        if len(word1) != len(word2):
            result_string += longerWord[len(shorterWord)::]
        
        return result_string