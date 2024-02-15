import math

def AddFunc(num):
    if num >= 10:
        num = AddFunc(math.floor(num/10) + (num % 10))

    return num

def InitialInput():
    try:
        firstNum =  int(input("Please input the first number: "))
        secondNum = int(input("Please input the second number: "))

        totalNum = firstNum + secondNum

        return totalNum
    except:
        print("Entered value was not an integer.")
        return InitialInput()

if __name__ == '__main__':
    totalNum = InitialInput()

    print(f"Final digit: {AddFunc(totalNum)}")