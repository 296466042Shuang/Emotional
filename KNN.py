# Author: Zhi Kai
# Time:  10:11
# Author: Zhi Kai
# Time:  9:47

import pandas as pd
import glob
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Get a list of all csv files in the target directory
csv_files = glob.glob('F:\\PythonProject\\EmotionalAnalysis\\filter\\P*\*.csv')

# Initialize an empty list to hold the dataframes
dataframes = []

# Loop through the list of csv files
for csv in csv_files:
    # Load the csv file and append it to the list
    dataframes.append(pd.read_csv(csv))

# Concatenate all dataframes in the list into one dataframe
data = pd.concat(dataframes)
data.columns = data.columns.str.strip()
# Create a label encoder for your labels
le = preprocessing.LabelEncoder()
le.fit(["excited", "elated", "happy", "relaxed", "calm", "exhausted", "tired", "sad", "angry", "tense"])

# Convert your labels to integers
data['label'] = le.transform(data['label'])

# Split into features (X) and target (y)
X = data[['HR', 'GSR']]
y = data['label']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = KNeighborsClassifier(n_neighbors=3)

# Fit the model
model.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = model.predict(X_test)

# Compute the accuracy of the model
print('Test Accuracy: %.3f' % accuracy_score(y_test, y_pred))
