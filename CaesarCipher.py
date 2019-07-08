'''
Created on Oct 16, 2018

@author: kassen qian
'''
# from Transform import shift
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()

def setShift(number):
    '''
    this function allows the user to pick the shift for the encryption.
    it creates global variables that create shifted alphabets based on the inputted number
    '''
    global shift
    shift = number
    
    global shifted_lower
    shifted_lower = lower_alph[number:] + lower_alph[:number]
    
    global shifted_upper
    shifted_upper = upper_alph[number:] + upper_alph[:number]
    
def encrypt(w):
    '''
    this function takes string w and for each character in w, shifts each character based on the encryption key from setShift.
    '''
    global shifted_lower, shifted_upper
    
    shiftedWord = "" 
    for ch in w:
        if ch in lower_alph:
            charIndex = lower_alph.find(ch)
            shiftedLetter = shifted_lower[charIndex]
            shiftedWord += shiftedLetter
        elif ch in upper_alph:
            charIndex = upper_alph.find(ch)
            shiftedLetter = shifted_upper[charIndex]
            shiftedWord += shiftedLetter
        else:
            shiftedWord += ch
    return shiftedWord

def findShift(string):
    '''
    this function tests all possible shifts for the words in the file and then returns the number for the shift that gives you the most words
    '''
    
    import os.path
    file = os.path.join("data","lowerwords.txt")
    f = open(file)
    
    global shifted_lower, shifted_upper
    
    fileSet = [w for w in f.read().split()]
    
    match = []
    
    for sh in range(26):
        setShift(sh)
        encryptedSet = set([encrypt(w) for w in string.split(" ")])
        intersect = encryptedSet.intersection(set(fileSet))
        length = len(intersect)
        match.append(length)
    maxMatch = max(match)
    return 26 - match.index(maxMatch)
    


if __name__ == '__main__':
    print(findShift("Bxvncrvnb rc'b njbh cx lxdwc oaxv 1-10, kdc wxc jufjhb"))
    
    setShift(3)
    print(encrypt("Hat7"))
    print(encrypt("Kass10?"))