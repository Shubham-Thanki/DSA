class Solution:

    def __init__(self, num, numsys) -> None:
        self.numlist = []
        self.numlist[:0] = num
        zeroadd = 7-len(self.numlist)
        for i in range(0, zeroadd):
            self.numlist.insert(0, '0')

        if numsys == '1':
            self.indian()
        else:
            self.international()

    unitdict = {"1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR",
                "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE", "0": ""}

    tenzdict = {"10": "TEN", "11": "ELEVEN", "12": "TWELVE", "13": "THIRTEEN", "14": "FOURTEEN", "15": "FIFTEEN", "16": "SIXTEEN", "17": "SEVENTEEN",
                "18": "EIGHTEEN", "19": "NINETEEN", "2": "TWENTY", "3": "THIRTY", "4": "FORTY", "5": "FIFTY", "6": "SIXTY", "7": "SEVENTY", "8": "EIGHTY", "9": "NINETY"}

    def indian(self):
        suffix = ["LAKH", "THOUSAND"]
        suff = 0
        list1 = self.numlist[0:2]
        list2 = self.numlist[2:4]
        list3 = self.numlist[4:7]
        ans = ''

        if int(list1[0])+int(list1[1]) > 0:
            ans = ans + self.two_digits(list1)+' '+suffix[suff]+' '
        suff += 1

        if int(list2[0])+int(list2[1]) > 0:
            ans = ans + self.two_digits(list2)+' '+suffix[suff]+' '

        if int(list3[0])+int(list3[1])+int(list3[2]) > 0:
            ans = ans + self.three_digits(list3)

        print(ans)

    def international(self):
        suffix = ["MILLION", "THOUSAND"]
        suff = 0
        list1 = self.numlist[0]
        list2 = self.numlist[1:4]
        list3 = self.numlist[4:7]
        ans = ''

        if int(list1[0]) > 0:
            ans = ans+self.unitdict[list1[0]]+' '+suffix[suff]+' '
        suff += 1

        if int(list2[0])+int(list2[1])+int(list2[2]) > 0:
            ans = ans+self.three_digits(list2)+' '+suffix[suff]+' '

        if int(list3[0])+int(list3[1])+int(list3[2]) > 0:
            ans = ans+self.three_digits(list3)

        print(ans)

    def three_digits(self, three_digits):
        ans3 = ''
        digit = ''
        if three_digits[0] != '0':
            ans3 = ans3+self.unitdict[three_digits[0]]+' '+'HUNDRED'+' '
        if three_digits[1] != '0':
            if three_digits[1] == '1':
                digit = three_digits[1]+three_digits[2]
                ans3 = ans3+self.tenzdict[digit]
            else:
                ans3 = ans3+self.tenzdict[three_digits[1]] + \
                    ' '+self.unitdict[three_digits[2]]
        else:
            ans3 = ans3+self.unitdict[three_digits[2]]

        if ans3[-1] == ' ':
            # This is to handle specific cases where strings like 100, 200, 300 , 400, etc. end with 'HUNDRED '.
            # So this condition helps to eliminate the redundant space.
            ans3 = ans3[0:len(ans3)-1]
        return ans3

    def two_digits(self, two_digits):
        ans2 = ''
        digit = ''
        if two_digits[0] != '0':
            if two_digits[0] == '1':
                digit = two_digits[0]+two_digits[1]
                ans2 = ans2+self.tenzdict[digit]
            else:
                ans2 = ans2+self.tenzdict[two_digits[0]
                                          ]+' '+self.unitdict[two_digits[1]]
        else:
            ans2 = ans2+self.unitdict[two_digits[1]]

        return ans2


if __name__ == '__main__':
    choose = input()
    num = input()
    k = Solution(num, choose)
