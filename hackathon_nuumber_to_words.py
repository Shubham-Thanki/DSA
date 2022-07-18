
num = input()
unitdict = {"1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR",
            "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE"}
numberdict = {"10": "TEN", "11": "ELEVEN", "12": "TWELVE", "13": "THIRTEEN", "14": "FOURTEEN", "15": "FIFTEEN", "16": "SIXTEEN", "17": "SEVENTEEN",
              "18": "EIGHTEEN", "19": "NINETEEN", "2": "TWENTY", "3": "THIRTY", "4": "FORTY", "5": "FIFTY", "6": "SIXTY", "7": "SEVENTY", "8": "EIGHTY", "9": "NINETY"}
ans = ""
flag = True
numlist = []
numlist[:0] = num
if numlist[0] != '0':
    ans = ans+unitdict[numlist[0]]+" HUNDRED "


if numlist[1] != '0' and numlist[1] != '1':
    ans = ans+numberdict[numlist[1]]+" "
elif numlist[1] == '0':
    pass
elif numlist[1] == '1':
    ans = ans+numberdict[numlist[1]+numlist[2]]
    flag = False

if flag:
    ans = ans+unitdict[numlist[2]]
print(ans)
