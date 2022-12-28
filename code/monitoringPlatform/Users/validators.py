
class CpfValidator():
    cleaned = ''
    error = ''

    def __init__(self, cpf):
        self.raw = cpf
        self.is_valid()
        

    def is_valid(self):
        
        formated = self.__clear_formatting( self.raw )
        special_character = ['-','.']
        
        err_formating_msg = "Use the format xxx.xxx.xxx-xx  or xxxxxxxxxxx"

        if not str(formated).isnumeric() or len(str(formated)) > 11:
            self.error = err_formating_msg
            return False
        
        for index, digit in enumerate(formated):
            if (digit in special_character) and (index not in [3,7,9]) or \
                (digit == '-' and index != 11) :
                self.error = err_formating_msg
                return False
        
        cpf_with_first_digit = self.__getDigit(formated[:-2])
        valid_cpf = self.__getDigit(cpf_with_first_digit)

        if valid_cpf == formated:
            self.cleaned = valid_cpf
            return True
        
        self.error = "Invalid cpf. Insert a valid cpf number"
        return False

    def __clear_formatting(self, cpf):
        special_character = ['-','.']
        cpf_new = ''

        for digit in cpf:
            if not digit in special_character:
                cpf_new += digit

        return cpf_new

    def __getDigit(self, cpf) :
        sum = 0

        for i, number in enumerate( range( len(cpf) + 1, 1, -1 ) ): 
            sum += int(cpf[i]) * number
        
        res = sum % 11

        digit = 0
        if res > 1:
            digit = 11 - res

        return cpf + str(digit)
