# Author: Zhi Kai
# Time:  9:47
# Author: Zhi Kai
# Time:  21:37

import pandas as pd
import glob
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

# Get a list of all csv files in the target directory
csv_files = glob.glob('F:\PythonProject\EmotionalAnalysis\\filter\P1\*.csv')
#csv_files = glob.glob('F:\PythonProject\EmotionalAnalysis\\filter\P2\*.csv')
#csv_files = glob.glob('F:\PythonProject\EmotionalAnalysis\\filter\P3\*.csv')
#csv_files = glob.glob('F:\PythonProject\EmotionalAnalysis\\filter\P4\*.csv')
#csv_files = glob.glob('F:\PythonProject\EmotionalAnalysis\\filter\P5\*.csv')
#csv_files = glob.glob('F:\PythonProject\EmotionalAnalysis\\filter\P6\*.csv')
#csv_files = glob.glob('F:\PythonProject\EmotionalAnalysis\\filter\P7\*.csv')
#csv_files = glob.glob('F:\PythonProject\EmotionalAnalysis\\filter\P8\*.csv')
#csv_files = glob.glob('F:\PythonProject\EmotionalAnalysis\\filter\P9\*.csv')

# csv_files = glob.glob('F:\PythonProject\EmotionalAnalysis\\filter\P10\*.csv')
#
# # Initialize an empty list to hold the dataframes
# dataframes = []
#
# # Loop through the list of csv files
# for csv in csv_files:
#     # Load the csv file and append it to the list
#     dataframes.append(pd.read_csv(csv))
#
# # Concatenate all dataframes in the list into one dataframe
# data = pd.concat(dataframes)

#dirs = [f'F:\\PythonProject\\EmotionalAnalysis\\filter\\P{i}' for i in range(1, 11)]

# Initialize an empty list to hold the dataframes
dataframes = []

# # Loop through each directory
# for dir in dirs:
#     # Get a list of all csv files in the current directory
#     csv_files = glob.glob(f'{dir}\\*.csv')
#
#     # Loop through the list of csv files and append each dataframe to the list
#     for csv in csv_files:
#         dataframes.append(pd.read_csv(csv))

for csv in csv_files:
        dataframes.append(pd.read_csv(csv))

# Concatenate all dataframes in the list into one dataframe
data = pd.concat(dataframes)


# Create a label encoder for your labels
le = preprocessing.LabelEncoder()
le.fit(["excited", "elated", "happy", "relaxed", "calm", "exhausted", "tired", "sad", "angry", "tense"])

# Convert your labels to integers
data['label'] = le.transform(data['label'])

# Split into features (X) and target (y)
data.columns = data.columns.str.strip()
print(data.head())
X = data[['HR', 'GSR']]
y = data['label']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the SVM model
# Use the 'rbf' kernel for non-linear problems
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print(len(le.classes_))
# cm = confusion_matrix(y_test, y_pred)
# cmd = ConfusionMatrixDisplay(cm, display_labels=le.classes_[np.unique(y_test)])
# # cmd = ConfusionMatrixDisplay(cm, display_labels=le.classes_)
# cmd.plot(cmap=plt.cm.Blues)
# plt.show()
# Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Convert to probabilities
cm_prob = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

# Now cm_prob is a matrix of probabilities. You can display it like you did with the confusion matrix:
cmd = ConfusionMatrixDisplay(cm_prob, display_labels=le.classes_[np.unique(y_test)])
cmd.plot(cmap=plt.cm.Blues)
plt.show()

# Select one tree from the forest
estimator = model.estimators_[5]

# Visualize the tree
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=800)
tree.plot_tree(estimator,
               feature_names = ['HR', 'GSR'],
               class_names=le.classes_,
               filled = True,
               max_depth=3);
fig.savefig('rf_individualtree.png')