'''
Created on Oct 15, 2018

@author: kassen qian
'''

'''
def encrypt(w):
'''
    #this function turns string w into the pig latin version of the string.


'''
    if w[0] == "a" or w[0] == "e" or w[0] == "i" or w[0] == "o" or w[0] == "u":
        return w + "-way"
    
    elif w[0] == "A" or w[0] == "E" or w[0] == "I" or w[0] == "O" or w[0] == "U":
        return w + "-way"
    
    elif w[0] == "q" and w[1]=="u":
        return w[2:]+"-"+w[0:2]+"ay" 
    
    elif w[0]=="Q" and w[1]=="U":
        return w[2:].upper()+"-"+w[0:2].upper()+"ay".upper()
    
    elif w[0]=="q" and w[1]=="U":
        return w[2:].upper()+"-"+w[0:2].upper()+"ay".upper()
    
    elif w[0]=="Q" and w[1]=="u":
        return w[2:].upper()+"-"+w[0:2].upper()+"ay".upper()
    
    elif w[0] == "y":
        return w[1:]+"-"+"yay"
    
    elif w[0] == "Y":
        return w[1:].upper()+"-"+"yay".upper()
    
    else: 
        vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
        for ch in w:
            if ch in vowels:
                vowelIndex = w.find(ch)
                return w[vowelIndex:]+"-"+w[0:vowelIndex]+"ay"  

    return w + "-ay"  
'''
    
    #    else:
    # if 'a' and 'e' and 'i' and 'o' and 'u' and 'y' not in w:

def encrypt(w):
    """
    this function turns string w into the pig latin version of the string.
    """
    statement = w.startswith('a') or w.startswith('e') or w.startswith('i') or w.startswith('o') or w.startswith('u') or w.startswith('A') or w.startswith('E') or w.startswith('I') or w.startswith('O') or w.startswith('U') or w.startswith('y') or w.startswith('Y')
    if statement == True:
        return w + "-way"
    else:
        if w.startswith('q'):
            return w[2:] + "-quay"
        else:
            a = w.find('a')
            e = w.find('e')
            i = w.find('i')
            o = w.find('o')
            u = w.find('u')
            y = w.find('y')
            A = w.find('A')
            E = w.find('E')
            I = w.find('I')
            O = w.find('O')
            U = w.find('U')
            Y = w.find('Y') 
            lst = [a, e, i, o, u, y, A, E, I, O, U, Y]
            newlst = []
            other = []
            for i in lst:
                if i != -1:
                    newlst.append(i)
                if i == -1:
                    other.append(i)
                    if lst == other:
                        return w + "-way"
            place = int(min(newlst))
            return w[place:] + '-' + w[:place] + 'ay'
        

def decrypt(w):
    '''
    this function takes string w, which is already technically in pig latin version, and returns it as best as it can to the original string
    '''
    if w.endswith("-way"):
        p = w.rfind("-")
        return w[:p]
    elif w.endswith("-quay"):
        p = w.rfind("-")
        return "qu" + w[:p]
    elif w.endswith("-yay"):
        p = w.rfind("-")
        return "y"+w[:p]
    else:
        p = w.rfind("-")
        return w[p+1:-2] + w[:p]
    
if __name__ == '__main__':
    print(encrypt("automobile"))
    print(encrypt("qUEEN"))
    print(encrypt("yesterday"))
    print(encrypt("Yesterday"))
    
    print(decrypt("apple-way"))
    print(decrypt("een-quay"))
    print(decrypt("esterday-yay"))
    print(decrypt("aight-stray"))