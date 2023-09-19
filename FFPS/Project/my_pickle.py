import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle as my_pickle

# Load the dataset
data = pd.read_csv('forest_fire_data.csv')
X = data[['temperature', 'humidity', 'oxygen']]
y = data['fire_occurred']

# Train the model
model = LogisticRegression()
model.fit(X, y)

# Save the model
with open('forest_fire_model.pkl', 'wb') as model_file:
    my_pickle.dump(model, model_file)



