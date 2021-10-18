from tax import iss, icms

class calculate_tax(object):

    def calculate(self, budget, tax):

        tax = tax.calculate(budget)
        print(tax)
        
if __name__ == '__main__':

    from budget import budget
    
    calc = calculate_tax()

    budget = budget(500)
    
    calc.calculate(budget,iss)
    calc.calculate(budget,icms)