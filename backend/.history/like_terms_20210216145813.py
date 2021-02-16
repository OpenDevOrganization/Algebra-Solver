# 16-2t=5t+9
class LikeTerm:
    
    def __init__(self, equation):
        self.equation = equation.replace(" ","")
        self.operators = {
            "+": " + ",
            "-": " - ",
            "*": " * ",
            "/": " / ",
            "=": " = "
        }

    def _splitEquation(self):
        splitted_equation = self.equation
        for i in self.operators:
            splitted_equation.replace(i, self.operators[i])
        
        return splitted_equation
    

    

    


    