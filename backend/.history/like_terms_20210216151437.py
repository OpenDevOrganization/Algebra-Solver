# 16 - 2t = 5t + 9
class LikeTerm:
    
    def __init__(self, equation):
        self.equation = equation.replace(" ","")
        self.operators = {
            "+": " + ",
            "-": " - ",
            "*": " * ",
            "/": " / ",
            "=": " = ",
        }

    def split_equation(self):
        splitted_equation = self.equation
        for i in self.operators:
            splitted_equation.replace(i, self.operators[i]) # added spaces to the operators
        # return the equation that is separated with =
        return splitted_equation.split(" = ")


    def combine_coefficients(self):
        pass


    def combineLikeTerms(self):
        pass
    
    

    


    