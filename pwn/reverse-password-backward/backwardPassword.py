def selectorOne(sliceOne:list, sliceFour:list):
    
    partOne = list()
    
    sliceOneLen = len(sliceOne)
    sliceFourLen = len(sliceFour)

    partOne.append(sliceOne[sliceFourLen-1])
    partOne.append(sliceOne[sliceOneLen-2])
    partOne.append(sliceOne[sliceFourLen-2])
    partOne.append(sliceOne[sliceOneLen-7])
    
    return partOne

def selectorTwo(sliceOne:list, sliceFour:list):

    partOne = list()
    
    sliceOneLen = len(sliceOne)
    sliceFourLen = len(sliceFour)

    partOne.append(sliceOne[sliceOneLen-3])
    partOne.append(sliceFour[sliceFourLen-5])
    partOne.append(sliceOne[sliceOneLen-6])
    partOne.append(sliceFour[sliceFourLen-9])
    
    return partOne

def main(stringOne:list, stringTwo:list):
    
    # Contains 10 elements
    sliceOne = stringOne[2:12]

    # Contains 10 elements
    sliceThree = stringOne[12:22]
    
    # Contains 10 elements
    sliceFour = stringTwo[0:10]

    passwordPartOne = selectorOne(sliceOne, sliceFour)
    passwordPartThree = selectorTwo(sliceThree, sliceFour)

    finalPassword = "".join(passwordPartThree + passwordPartOne)

    finalPassword = finalPassword[::-1]
    
if __name__ == "__main__":
    alphabet = [a.upper() for a in list(("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"))]

    special_char = list(("@","#","$","^","&","*","_","-","+","=","-","?"))

    print("alphabet     = ", alphabet[::-1])
    print("special_char = ", special_char[::-1])

    main(alphabet[::-1], special_char[::-1])