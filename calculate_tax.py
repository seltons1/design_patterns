from tax import calculate_iss,calculate_icms

class calculate_tax(object):

    def calculate(self, budget, tax):

        if tax =='ISS':
            tax = calculate_iss(budget)
            print(tax)
        if tax == 'ICMS':
            tax = calculate_icms(budget)
            print(tax)
    
if __name__ == '__main__':

    from budget import budget
    

    calc = calculate_tax()

    budget = budget(500)
    
    calc.calculate(budget,'ISS')
    calc.calculate(budget,'ICMS')