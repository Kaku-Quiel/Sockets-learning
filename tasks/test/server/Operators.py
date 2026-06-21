class Operators:
    @staticmethod
    def doMath(num1, num2, operator):
        operators = ['+', '-', '*', '/', '**']

        if operator not in operators:
            return "Error back: Operacion no valida"
        
        if operator == '+':
            return num1 + num2
        
        if operator == '-':
            return num1 - num2
        
        if operator == '*':
            return num1 * num2
        
        if operator == '/':
            if num2 == 0:
                return "Error back: divicion por 0"
            
            return num1 / num2
        
        if operator == '**':
            return num1 ** num2