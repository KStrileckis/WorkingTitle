from Cipher import *
class Virtual_Network:
    def __init__(self, x):
        #hex limit is how many hex ciphers (non-normal ciphers) are allowed
        self.hex_limit = int(x * .3333)
        self.targets = []
        self.hex_chance_upper = 5
        x_2 = int(x/ 5)
        #The first several will be normal ciphers
        for i in range(0, int(x_2)):
            self.targets.append(Cipher(randint(1,7), True, i))
        for i in range(x_2, x):
            #50% chance to make hex cipher if hex limit is not yet met
            if self.hex_limit > 0 and randint(0,self.hex_chance_upper) == 0:
                self.hex_limit -= 1
                self.targets.append(Cipher(randint(1,7), False, i))
            else:
                self.targets.append(Cipher(randint(1,7), False, i))
            self.hex_chance_upper -= 1
            if self.hex_chance_upper < 1:
                self.hex_chance_upper = 1
    def reset(self, num_to_reset, on_index):
        i = on_index
        while i >= 0 and num_to_reset > 0:
            if self.targets[i].normal == True:
                self.targets[i] = Cipher(randint(1,7), True, i)
            else:
                self.targets[i] = Cipher(randint(1,7), False, i)
            i = i - 1
            num_to_reset = num_to_reset - 1
    def get_targets(self):
        return self.targets
    def print_targets_coded(self, text):
        for x in self.targets:
            print(x.encode(text))
        print("")
    def print_targets(self):
        for x in self.targets:
            x.print_keys()
            print("")
    def guess(self, target_index, guess):
        if self.targets[target_index].make_guess(guess):
            print("Correct!", end="\n\n")
            return True
        else:
            print("Incorrect!", end="\n\n")
            return False
    def print_targets_obscured(self):
        for x in self.targets:
            print("Target ["+str(x.idt)+"] is "+x.getCompro())
    def print_targets_obscured_final(self, t):
        for x in self.targets:
            print(str(t) + "Target ["+str(x.idt)+"] is "+x.getCompro())
    def all_unsafe(self):
        x = True
        for x in self.targets:
            if x.compromised == False:
                x = False
        return x

