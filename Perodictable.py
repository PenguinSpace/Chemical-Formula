import pandas as pd
import regex as re


# %% codecell
# file path of csv and reads in csv into dataframe
file_path = '/Users/nelsonyeung/Documents/Penguin Files/Programs/Python Projects/Chem_Formula/MIM_Elements.csv'
mass_elements = pd.read_csv(file_path)

# %% codecell
# what I want to do now is to find the most abundent elements and their monoisotopic mass
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
    
    # makes the dictionary with keys being Symbol and values being Mass
    element_mass = mass_elements.iloc[mass_index]['Mass']
    ptable[mass_elements.iloc[mass_index]['Symbol']] = round(element_mass, 4)

# makes list of elements for new DataFrame
element_series = list(mass_elements['Name'].unique())
data = {'Name': element_series, 'Isotope_Symbol': list(ptable.keys()), 'Monoisotopic_Mass': list(ptable.values())}
# print(data)

# puts all the relevant information into a new DataFrame and saves to a csv file
PerodicTable = pd.DataFrame(data)
# print(PerodicTable)
PerodicTable.to_csv('New_Ptable.csv')


# %% codecell
# I want to reformat the symbols column to use brackets instead of ()
Isotope = PerodicTable['Isotope_Symbol'].str.extract(r'(\w{2})', expand=False)
Isotope_number = PerodicTable['Isotope_Symbol'].str.extract(r'(\d+)', expand=False)
Isotope_number = '[' + Isotope_number + ']'

Isotope = Isotope_number + Isotope
#print(Isotope)

PerodicTable['Isotopes'] = Isotope
# print(PerodicTable)

# going to add a column for just the element symbol
PerodicTable['Symbol'] = PerodicTable['Isotope_Symbol'].str.extract(r'(\w+)', expand=False)
#print(PerodicTable['Symbol'])



# %% codecell
# Need to allow user to input a chemical formula and output the monoisotopic mass
# of the molecule





# %% codecell














