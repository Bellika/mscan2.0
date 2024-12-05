import pandas as pd 
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
  return pd.read_csv(file_path)

def clean_data(data):
  # replacing ? with the most common value
  most_common_value = data.loc[data['stalk-root'] != '?', 'stalk-root'].mode()[0]
  return data

# tranforming string values to numerical values
def encode_labels(data):
  label_encoders = {}
  for column in data.columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le
  return data, label_encoders


