# Author: Zhi Kai
# Time:  9:55
# Author: Zhi Kai
# Time:  9:47

import pandas as pd
import glob
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

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

# Convert labels to categorical one-hot encoding
y_train_one_hot = to_categorical(y_train, num_classes=10)
y_test_one_hot = to_categorical(y_test, num_classes=10)

# Define the model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(2,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))  # 10 is the number of your classes

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X_train, y_train_one_hot, epochs=10)

# Evaluate the model
loss, acc = model.evaluate(X_test, y_test_one_hot, verbose=0)
print('Test Accuracy: %.3f' % acc)
