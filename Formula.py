import re
from Perodictable import PerodicTable

# Do I want the user to modify the PerodicTable?
# probably not?


# going to make a class for the formula to do
# monoisotopic mass predictions
class formula:
    def __init__(self, mol_formula=None):
        mol_formula = input('Please input a chemical formula')
        
        # checks for a valid input
        if re.search(r'\w', mol_formula) == None:
            print("Please enter a valid chemical formula")
            return None
        
        
        mass = 0
        return None
    
    # finds the mass of the molecule
    def get_mass(self):
        total_mass = 0
        current_mass = 0
        


if __name__ == '__main__':
    test = formula()
    
    