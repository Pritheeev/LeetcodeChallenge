#Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        res = ""
        nstack = []
        ostack = []
        while(i<len(s)):
            if(s[i].isdigit()):
                digits = ""
                while(s[i].isdigit()):
                    digits+=s[i]
                    i+=1
                nstack.append(int(digits))
            
            elif(s[i]=="["):
                ostack.append(res)
                res = ""
                i+=1
                
            elif(s[i]=="]"):
                count = nstack.pop()
                temp = ostack.pop()
                res = temp*count
                i+=1
                
            else:
                res +=s[i]
                i+=1
        return res
