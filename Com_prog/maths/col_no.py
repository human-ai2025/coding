class Solution:
    def approach1(self, columnNumber: int) -> str:
        newString = ""
        while columnNumber > 0:
            columnNumber -= 1
            newString = chr((columnNumber%26)+65) + newString
            columnNumber = columnNumber // 26  
        return newString
        

    def convertToTitle(self, columnNumber: int) -> str:
        return self.approach1(columnNumber)
    


# https://leetcode.com/problems/excel-sheet-column-title