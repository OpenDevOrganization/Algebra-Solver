# example: 16 - 2t = 5t + 9
class LikeTerm:
    
    def __init__(self, equation):
        self.equation = equation.replace(" ","")
        self.operators = [
            "+",
            "-",
            "*",
            "/",
            "=",
        ]
        self.variables = {}

    def split_equation(self, equation):
        for i in self.operators:
            if i in equation: 
                equation = equation.replace(i, " " + i + " ") # added spaces to the operators

        return equation.split(" = ")

    def _filter_constants(self, equation_part):
        return [i for i in equation_part if i.isdigit()]
    
    def _filter_unknowns(self, equation_part):
        return [i for i in equation_part if i.isdigit() == False]

    def _filter_variables(self, equation_part):
        return [i for i in equation_part if all(j.isalnum() for j in i)&any(j.isalpha() for j in i)]

    def split_variables(self, variables):
        pass

    def combine_constants(self):
        equation = self.split_equation(self.equation)
        first_part_of_equation = [*map(int, self._filter_constants(equation[0].split(" ")))]
        rest_part_of_equation =  [-int(i) for i in self._filter_constants("".join(equation[1:]).split(" "))]
        return sum(first_part_of_equation) + sum(rest_part_of_equation)


    def combine_like_terms(self):
        equation = self.split_equation(self.equation)
        first_part_of_equation = self._filter_variables(equation[0].split(" "))
        rest_part_of_equation = self._filter_variables("".join(equation[1:]).split(" "))
        
    def calculate_unknowns(self):
        equation = self.split_equation(self.equation)
        first_part_of_equation = [*map(str, self._filter_unknowns(equation[0].split(" ")))]
        first_part_of_equation_ = []
        place = -1
        for n in first_part_of_equation:
            place += 1
            if n == '-' or n == '+' or n == '*' or n == '/':
                holder = first_part_of_equation[place] + (first_part_of_equation[place+1])
                first_part_of_equation_.append(holder)
        first_part_of_equation_ok = 0
        for n in first_part_of_equation_:
            first_part_of_equation_ok += int(n[:-1])
        first_part_of_equation_ok = str(first_part_of_equation_ok) + first_part_of_equation_[0][-1:]
        return first_part_of_equation_ok
        

    def getResult(self):
        pass


# if __name__ == "__main__":
#    lt = LikeTerm("16 - 2t = 5t + 9")
#    print(lt.combine_constants())

'''
- split the equation
- add up all the constants 
- add up all the liketerms
- display in form: x = ?
'''
