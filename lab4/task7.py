class Reverse:
    def __init__(self, s):
        self.s = s
    
    def __iter__(self):
        return (self.s[i] for i in range(len(self.s)-1, -1, -1))

s = input()
print(*Reverse(s), sep='')