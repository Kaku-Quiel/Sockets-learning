class Validate():
    @staticmethod
    def isValid(operationSTR):
        operation = operationSTR.split()

        valid_operators = ['+', '-', '*', '/', '**']

        try:
            num1 = float(operation[0])
            operator = operation[1]
            num2 = float(operation[2])

        except Exception as e:
            return {
                "codigo": False,
                "message": f"Error front: error en conversion {e}"
            }

        if len(operation) != 3:
            return {
                "codigo": False,
                "message": "Error front: operacion no valida" 
            }

        if type(num1) != float or type(num2) != float:
            return {
                "codigo": False,
                "message": "Error front: dato no valido en la primera posicion"
            }

        if operator not in valid_operators:
            return {
                "codigo": False,
                "message": "Error front: operador no valido"
            }
        
        return {
            "codigo": True,
            "message": "success"
        }