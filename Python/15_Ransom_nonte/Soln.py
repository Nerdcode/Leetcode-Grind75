class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)
        for item,value in rc.items():
            if item in rc:
                if mc[item]<value:
                    return False
        return True
