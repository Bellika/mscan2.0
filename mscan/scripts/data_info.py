import pandas as pd

column_names = [
    "class", "cap_shape", "cap_surface", "cap_color", "bruises", "odor",
    "gill_attachment", "gill_spacing", "gill_size", "gill_color", "stalk_shape",
    "stalk_root", "stalk_surface_above_ring", "stalk_surface_below_ring",
    "stalk_color_above_ring", "stalk_color_below_ring", "veil_type",
    "veil_color", "ring_number", "ring_type", "spore_print_color",
    "population", "habitat"
]

mushrooms = pd.read_csv('mushrooms.csv', header=None, names=column_names)

print('Size:', mushrooms.shape)
print('Datatypes', mushrooms.dtypes)


print('Missing:')
print(mushrooms.isnull().sum())

print('Unique values', mushrooms['class'].unique())

print('\nSpread of class')
print(mushrooms['class'].value_counts())

for column in mushrooms.columns:
  print(f'\nColumn {column} unique values:')
  print(mushrooms[column].value_counts())