#Find All Anagrams in a String

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        leng = len(p)
        output = []
        if( (len(s) == len(p)) and s==p):
            return [0]
        for i in range(0,len(s)-leng+1):
            if(self.IsAnagram(p,s[i:i+leng])):
                output.append(i)
        return output
                
        
    def IsAnagram(self,str1,str2):
        if(sorted(str1)==sorted(str2)):
            return True
        else:
            return False
