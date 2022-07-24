class Solution:

    def __init__(self, num, numsys) -> None:
        self.num = num
        self.numsys = numsys
        self.numlist = []
        self.numlist[:0] = num
        zeroadd = 7-len(self.numlist)
        for i in range(0, zeroadd):
            self.numlist.insert(0, '0')
        self.ans = ''

    unitdict = {"1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR",
                "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE", "0": ""}

    tenzdict = {"10": "TEN", "11": "ELEVEN", "12": "TWELVE", "13": "THIRTEEN", "14": "FOURTEEN", "15": "FIFTEEN", "16": "SIXTEEN", "17": "SEVENTEEN",
                "18": "EIGHTEEN", "19": "NINETEEN", "2": "TWENTY", "3": "THIRTY", "4": "FORTY", "5": "FIFTY", "6": "SIXTY", "7": "SEVENTY", "8": "EIGHTY", "9": "NINETY"}

    suffix = ["LAKH", "THOUSAND", "HUNDRED"]
    suff = 0

    def indian(self):
