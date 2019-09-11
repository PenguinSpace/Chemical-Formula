import pandas as pd

# %% codecell
# file path of csv and reads in csv into dataframe
file_path = '/Users/nelsonyeung/Documents/Penguin Files/Programs/Python Projects/Chem_Formula/MIM_Elements.csv'
mass_elements = pd.read_csv(file_path)

# %% codecell
# what I want to do know is to find the most abundent elements and their monoisotopic mass
mass_elements.columns
elements = list(mass_elements['Name'].unique())

ptable = {}

for element in elements:
    mask = mass_elements.Name == element
    # finds the index of that particular element and puts in a list
    index = mass_elements[mask].index.values

    max_abundt = 0

    # loops through the list of index to find most abundent isotope
    for i in index:
        current_abund = mass_elements.iloc[i]['Abund.']
        
        if current_abund >= max_abundt:
            max_abundt = current_abund
            mass_index = i
    
    # makes the dictionary 
    element_mass = mass_elements.iloc[mass_index]['Mass']
    ptable[mass_elements.iloc[mass_index]['Symbol']] = element_mass

# makes list of elements
element_series = list(mass_elements['Name'].unique())
data = {'Name': element_series, 'Symbol': list(ptable.keys()), 'Monoisotopic Mass': list(ptable.values())}
# print(data)

# puts all the relevant information into a new DataFrame
PerodicTable = pd.DataFrame(data)
print(PerodicTable)
        



# %% codecell






