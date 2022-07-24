

def indian(num):
    unitdict = {"1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR",
                "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE", "0": ""}
    tenzdict = {"10": "TEN", "11": "ELEVEN", "12": "TWELVE", "13": "THIRTEEN", "14": "FOURTEEN", "15": "FIFTEEN", "16": "SIXTEEN", "17": "SEVENTEEN",
                "18": "EIGHTEEN", "19": "NINETEEN", "2": "TWENTY", "3": "THIRTY", "4": "FORTY", "5": "FIFTY", "6": "SIXTY", "7": "SEVENTY", "8": "EIGHTY", "9": "NINETY"}
    suffix = ["LAKH", "THOUSAND", "HUNDRED"]
    suff = 0
    ans = ""
    numlist = []
    numlist[:0] = num
    zeroadd = 7-len(numlist)
    for i in range(0, zeroadd):
        numlist.insert(0, '0')
    # print(numlist)

    digit = ''
    for i in [0, 2]:
        if numlist[i] != '0':  # The number has a digit at this place
            if numlist[i] == '1':  # If the first digit is 1
                # Merging the 2 digits to get a suitable value from the keys available in tenzdict.
                digit = digit+numlist[i]+numlist[i+1]
                ans = ans+tenzdict[digit]+' '
            else:
                ans = ans+tenzdict[numlist[i]]+' ' + unitdict[numlist[i+1]]+' '
            ans = ans+suffix[suff]+' '

        elif numlist[i+1] != '0':
            ans = ans+unitdict[numlist[i+1]]+' '
            ans = ans+suffix[suff]+' '

        suff += 1
    flag = True
    digit = ''
    if numlist[4] != '0':
        ans = ans+unitdict[numlist[4]]+' '+suffix[suff]+' '
    if numlist[5] != '0':
        if numlist[5] == '1':
            digit = digit+numlist[5]+numlist[6]
            ans = ans+tenzdict[digit]+' '
            flag = False
        else:
            ans = ans+tenzdict[numlist[5]]+' '
    if numlist[6] != '0' and flag:
        ans = ans+unitdict[numlist[6]]

    ans = ans.split("  ")
    for i in ans:
        print(i, end=' ')


def international(num):
    unitdict = {"1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR",
                "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE", "0": ""}
    tenzdict = {"10": "TEN", "11": "ELEVEN", "12": "TWELVE", "13": "THIRTEEN", "14": "FOURTEEN", "15": "FIFTEEN", "16": "SIXTEEN", "17": "SEVENTEEN",
                "18": "EIGHTEEN", "19": "NINETEEN", "2": "TWENTY", "3": "THIRTY", "4": "FORTY", "5": "FIFTY", "6": "SIXTY", "7": "SEVENTY", "8": "EIGHTY", "9": "NINETY"}

    ans = ""
    numlist = []
    numlist[:0] = num
    zeroadd = 7-len(numlist)
    for i in range(0, zeroadd):
        numlist.insert(0, '0')
    if numlist[0] != '0':
        ans = ans+unitdict[numlist[0]]+' '+'MILLION '

    digit = ''
    flag = True
    for i in [1, 4]:
        if numlist[i] != '0':
            ans = ans+unitdict[numlist[i]]+' '+'HUNDRED '
        if numlist[i+1] != '0':
            if numlist[i+1] == '1':
                digit = digit+numlist[i+1]+numlist[i+2]
                ans = ans+tenzdict[digit]+' '
                flag = False
            else:
                ans = ans+tenzdict[numlist[i+1]]+' '

        if numlist[i+2] != '0' and flag:
            ans = ans+unitdict[numlist[i+2]]+' '

        checksum = int(numlist[i])+int(numlist[i+1])+int(numlist[i+2])

        if i == 1 and checksum > 0:
            ans = ans+'THOUSAND '

    ans = ans.split("  ")
    for i in ans:
        print(i, end=' ')


if __name__ == '__main__':
    choose = input()
    num = input()
    if choose == '1':
        indian(num)
    else:
        international(num)
