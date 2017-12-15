from random import *
class Cipher:
    def __init__(self):
        self.key_length = 2
        self.keys = [1, 2]
        self.compromised = False
        self.idt = 0
        self.normal = True
    def __init__(self, length):
        self.key_length = length
        self.keys = []
        self.compromised = False
        self.id = 0
        self.normal = True
        for i in range(1, length+1):
            self.keys.append(i)
    def __init__(self, length, normal, idt):
        self.key_length = length
        self.keys = []
        self.compromised = False
        self.idt = idt
        self.normal = normal
        #if normal is True, then each key is a random shift
        if normal == True:
            for i in range(1, length+1):
                self.keys.append(randint(0,i*4))
        #if normal is False, then there is only one key in the cipher which is 0-F
        else:
            self.key_length = 1
            self.keys = [ hex(randint(0,15)) ]
    def getCompro(self):
        if self.compromised == False:
            return "not compromised."
        else:
            return "compromised. Good job."
    def make_guess(self, code):
        #If it's a hexadecimal encoding
        if self.normal == False:
            k = str(self.keys[0].replace("0x","").lower())
            k = k.replace("\'", "")
            #print(k)#REMOVE
            c = str(str(code).replace("[","").replace("]","").lower())
            c = c.replace("\'", "")
            #print(c)#REMOVE
            print (k + "\n\t" + c)
            if k == c:
                #compromise it and return True
                self.compromised = True
                return True
            else:
                return False
        #the below condition is easier than !=
        if len(code) < len(self.keys):
            return False
        for (x,y) in zip(code, self.keys):
            if x != y:
                return False
        #compromise it and return True
        self.compromised = True
        return True
    def get_int_of_hex_key(self, hex_c):
        #0-9
        if ord(hex_c) < 58:
            return int(int(ord(hex_c)) - 48)
        #A-F
        return int(int(ord(hex_c)) - 97 + 10)
    def encode(self, text):
        if self.compromised:
            return "\tX"
        code = "\t"+str(self.idt)+" (\""+text+"\")--->"
        y = 0
        key_array = []
        if self.normal == False:
            l = 1
            key_array = [self.get_int_of_hex_key(self.keys[0][2])]
        else:
            l = len(self.keys)
            key_array = self.keys
        for x in text:
            if x.isalpha():
                num = ord(x)
                num += key_array[y % l]
                if x.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif x.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                code += chr(num)
                y += 1
            else:
                code += x
        return code
    def print_keys(self):
        print(end="-")
        for x in self.keys:
            print(x, end="-")

