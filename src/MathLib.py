class MathLib:

    @classmethod
    def execute(cls, math_request):
        operator = math_request.get_operator()
        ope1 = math_request.get_ope1()
        ope2 = math_request.get_ope2()

        match operator:
            case 'add':
                math_request.set_res(ope1 + ope2)
            case 'sub':
                math_request.set_res(ope1 - ope2)
            case 'mul':
                math_request.set_res(ope1 * ope2)
            case 'div':
                if ope2 == 0:
                    raise MathLibException ("ope2 cannot be zero")
                else:
                    math_request.set_res(ope1 / ope2)
            case 'pow':
                math_request.set_res(ope1 ** ope2)
            case 'root':
                math_request.set_res(cls.__root(ope1, ope2))
            case _:
                raise OperatorNotSupportedException ("Operator not supported")

    @staticmethod
    def __root(ope1, ope2):
        if ope2 == 0:
            raise MathLibException ("ope2 cannot be zero")
        else:
            return round(ope1 ** (1 / ope2), 2)

class MathLibException(Exception):
    pass

class OperatorNotSupportedException(MathLibException):
    pass