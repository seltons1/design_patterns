from tax import calculate_iss,calculate_icms

class calculate_tax(object):

    def calculate(self, budget, tax):

        tax = tax(budget)
        print(tax)
        
if __name__ == '__main__':

    from budget import budget
    
    calc = calculate_tax()

    budget = budget(500)
    
    calc.calculate(budget,calculate_iss)
    calc.calculate(budget,calculate_icms)