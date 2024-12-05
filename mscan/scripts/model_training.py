from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
from scripts.visualization import plot_confusion_matrix, plot_feature_importance, plot_prediction_distribution
import matplotlib.pyplot as plt

def train_decision_tree(x, y, test_size=0.2, random_state=42):
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
  dt_model = DecisionTreeClassifier(random_state=random_state)
  dt_model.fit(x_train, y_train)
  y_pred_dt = dt_model.predict(x_test)
  accuracy = accuracy_score(y_test, y_pred_dt)
  report = classification_report(y_test, y_pred_dt)

  #plot_confusion_matrix(y_test, y_pred_dt, labels=[0, 1])
  #plot_feature_importance(dt_model, x.columns)
  #plot_prediction_distribution(y_test, y_pred_dt)

  return dt_model, accuracy, report

# shows the decisions the model is making (in this file because model based)
def visualize_decision_tree(model, feature_names):
  plt.figure(figsize=(20, 10))
  plot_tree(model, feature_names=feature_names, class_names=['Edible', 'Poisonous'], filled=True, rounded=True)
  plt.title('Decision Tree visualization')
  plt.show()


  