from stack import Stack

def divideby2(decNum):
    remstack = Stack()

    while decNum > 0:
        rem = decNum % 2
        remstack.push(rem)
        decNum = decNum // 2

    binstring = ""
    while not remstack.isEmpty():
        binstring = binstring + str(remstack.pop())

    return binstring

print(divideby2(45))


def baseConverter(decNumber,base):
    """
    This function is for customed base converstion like base to 3, 16
    """
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]  # Taking corresponding index of the digit and appending.

    return newString

print(baseConverter(25,2))
print(baseConverter(25,16))