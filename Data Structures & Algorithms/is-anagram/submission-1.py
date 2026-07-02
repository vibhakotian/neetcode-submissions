class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapi=dict()

        for word in s:
            if word not in mapi:
                mapi[word]=0
            mapi[word]+=1

        for word in t:
            if word not in mapi:
                mapi[word]=0
            
            mapi[word]-=1
        
        ans= all(value==0 for value in mapi.values())
       

        return ans