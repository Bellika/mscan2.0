from scripts.preprocessing import load_data, clean_data, encode_labels
from scripts.model_training import train_decision_tree, visualize_decision_tree


file_path = 'data/mushrooms.csv'
data = load_data(file_path)

data = clean_data(data)
data, label_encoders = encode_labels(data)

# x = other columns / variables, y = target variable
x = data.drop('class', axis=1)
y = data['class']

model, accuracy, report = train_decision_tree(x, y)

#dt visual model
#visualize_decision_tree(model, x.columns)

print(f'Model Accuracy: {accuracy}')
print(f'Model Report:\n{report}')