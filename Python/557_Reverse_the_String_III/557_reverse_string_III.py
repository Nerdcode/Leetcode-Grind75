class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        arr=[]
        for i in x :
            arr.append(i[::-1])
            arr.append(" ")
        return "".join(arr).strip()
    