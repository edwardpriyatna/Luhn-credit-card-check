def getDigits(number):
    if number < 9:
        return number#less than 9 nothing happens
    else:
        number = 1 + number % 10  # more than 9 do this formula
        return number
def SumOfDoubleEvenPlace(number):
    even_digits = number[-2::-2]  # entering every even place number from right to left and placing them to even_digits list
    sum=0
    for number in even_digits:
        number = int(number)  # converting each element of the list to an integer
        number = number * 2
        sum=sum+getDigits(number)#summing the double even place numbers
    return sum

def SumOfOddPlace(number):
    odd_digits = number[-1::-2]#take only the digits in the odd place from right to left
    sumOdd = 0
    for elements in odd_digits:
        elements = int(elements) # converting each element of the list to an integer
        sumOdd = sumOdd + elements#summing the odd place numbers
    return sumOdd #the sum of odd digits
def isValid(number):
    if len(number) >= 13 and len(number) <= 16:#if the lenght not 13 to 16 wrong
        if int(number[0]) in [4, 5, 6] or (int(number[0]) == 3 and int(number[1])== 7):  # if not start with these numbers wrong
            sumOddEven = SumOfDoubleEvenPlace(number) + SumOfOddPlace(number)
            if sumOddEven % 10 == 0:
                print("valid")
                return True  # if Sum of number in even place+ Sum of number in odd place divisible by 10 valid
            else:
                print("invalid")
                return False
        else:
            print("must start with 4 or 5 or 6 or 37")
    else:
        print("wrong lenght")
if __name__ == '__main__':
    number = list(input("credit card number"))  # input credit card number
    isValid(number)