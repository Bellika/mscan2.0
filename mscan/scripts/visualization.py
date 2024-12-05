from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns

# shows accuracy in form of diagram - r
def plot_confusion_matrix(y_true, y_pred, labels):
  cm = confusion_matrix(y_true, y_pred, labels=labels)
  disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
  disp.plot(cmap='Blues')
  plt.title('Confusion Matrix')
  plt.show()

# shows the importance of wich columns that has the most affect on the model
def plot_feature_importance(model, feature_names):
    importance = model.feature_importances_
    sorted_indices = np.argsort(importance)[::-1]

    plt.figure(figsize=(10, 6))
    plt.bar(range(len(importance)), importance[sorted_indices], align="center")
    plt.xticks(range(len(importance)), [feature_names[i] for i in sorted_indices], rotation=90)
    plt.title("Feature Importances")
    plt.xlabel("Feature")
    plt.ylabel("Importance")
    plt.tight_layout()
    plt.show()

# seaborn
def plot_prediction_distribution(y_true, y_pred):
    sns.histplot(y_pred, kde=True, label='Predictions', color='blue', stat='density', bins=30)
    sns.histplot(y_true, kde=True, label='True Values', color='orange', stat='density', bins=30)
    plt.legend()
    plt.title("Prediction vs True Value Distribution")
    plt.show()

