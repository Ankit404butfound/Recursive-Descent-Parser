class Parser:
    def __init__(self, expression):
        self.expression = expression
        self.chrPointer = 0
        self.currentChar = self.expression[self.chrPointer]
        self.result = self.parseSum()
    

    def incrementPointer(self):
        if self.chrPointer < len(self.expression)-1:
            self.chrPointer += 1
            self.currentChar = self.expression[self.chrPointer]
            return True
        else:
            return False


    def parseNumber(self):
        num = 0
        while self.currentChar >= '0' and self.currentChar <= '9':
            currentChr = ord(self.currentChar) - 48
            num = num*10 + currentChr
            if not self.incrementPointer():
                break
        return num

    
    def parseFactor(self):
        if self.currentChar >= '0' and self.currentChar <= '9':
            return self.parseNumber()
            # currentChr = self.currentChar
            # self.incrementPointer()
            # return ord(currentChr) - 48
        
        
        if self.currentChar == '(':
            self.incrementPointer()
            result = self.parseSum()
            if self.currentChar == ')':
                self.incrementPointer()
                return result
            else:
                print("Error: Expected a closing parenthesis")
                exit()
        # else:
        #     print("Error: Expected a valid expression")
        #     exit()

    
    def parseProduct(self):
        factor1 = self.parseFactor()
        while self.currentChar == '*':
            self.incrementPointer()
            factor2 = self.parseFactor()
            factor1 *= factor2
        return factor1

    
    def parseSum(self):
        factor1 = self.parseProduct()
        while self.currentChar == '+':
            self.incrementPointer()
            factor2 = self.parseProduct()
            factor1 += factor2
        return factor1
            


rdp = Parser(input("Enter an expression: "))
print(rdp.result)