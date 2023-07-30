import numpy as np
import pandas as pd
import tensorflow as tf
import keras
from keras.layers import Concatenate
import csv
import hashlib
import secrets
import binascii
from binascii import unhexlify, hexlify
from datetime import datetime

# load data from csv file into a pandas dataframe
df = pd.read_csv("train.csv")
id_data = df["id"].values
nonce_data = df["nonce"].values

#hash_data_0 = df["hash"].values
#for i in hash_data_0:
    #hash_data_1 = hash_data_0[i]
    #hash_data = int(hash_data_1, 16)

df["hash_int"] = df["hash"].apply(lambda x: int(x, 16))
hash_data = df["hash_int"].values
df["merkle_root_int"] = df["merkle_root"].apply(lambda x: int(x, 16))
merkle_root_data = df["merkle_root_int"].values

# Convert the string time value to a datetime object
#df["time_value"] = df["time"].datetime.datetime.strptime(time_data, '%m/%d/%y %H:%M')
# Convert the datetime object to a float value representing the number of seconds since the epoch
#time_data_float = (df["time_value"] - datetime.datetime(1970,1,1)).total_seconds()
#time_data = time_data_float.values
#print(time_data)

date_str = df["time"].values
date_str = date_str.tolist()[0]
date_format = "%m/%d/%y %H:%M"
date = datetime.strptime(date_str, date_format)
time_data = int(date.timestamp())
version_data = df["version"].values
bits_data = df["bits"].values

# normalize the input variable
# convert the input variable to a tensor
id_data_tensor = tf.constant(id_data, dtype=tf.float64)
nonce_data_tensor = tf.constant(nonce_data, dtype=tf.float64)
hash_data_tensor = tf.constant(hash_data, dtype=tf.float64)
merkle_root_data_tensor = tf.constant(merkle_root_data, dtype=tf.float64)
time_data_tensor = tf.constant(time_data, dtype=tf.float64)
version_data_tensor = tf.constant(version_data, dtype=tf.float64)
bits_data = tf.constant(bits_data, dtype=tf.float64)

#X and Y variables
#Training Data
id_x = id_data_tensor[:-1]
nonce_x = nonce_data_tensor[:-1]
hash_x = hash_data_tensor[:-1] 
merkle_root_x = merkle_root_data_tensor[:-1]
#time_x = time_data_tensor[:-1]
version_x = version_data_tensor[:-1]
bits_x = bits_data[:-1] 

#Target Data
id_y = id_data_tensor[1:]
nonce_y = nonce_data_tensor[1:]
hash_y = hash_data_tensor[1:] 
merkle_root_y = merkle_root_data_tensor[1:]
#time_y = time_data_tensor[1:]
version_y = version_data_tensor[1:]
bits_y = bits_data[1:] 

print("XXXXXXXXXXXXXXX")
# create the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(6, activation="relu", input_shape=[1]),
    tf.keras.layers.Dense(6, activation="relu", name="layer1"),
    tf.keras.layers.Dense(36, activation="relu", name="layer2"),
    tf.keras.layers.Dense(1, activation="relu", name="layer3")
])

# compile the model
#model.compile(optimizer='adam', loss='mean_squared_error', learning_rate = 0.1)
optim = keras.optimizers.Adam(learning_rate=0.01)
model.compile(optimizer='adam',loss='mse', metrics=['accuracy'])

# train the model on the data
history = model.fit(nonce_x, nonce_y, epochs=2)
#history = model.fit(x=[id_x, nonce_x, hash_x, merkle_root_x, version_x, bits_x], y = nonce_y, epochs=2)

# make predictions using the trained model
predictions = model.predict(nonce_y)
print("Next nonce: ", predictions)
integer_list = [int(val[0]) for val in predictions]
#print(integer_list)
#df_test = pd.read_csv("test.csv")
#nonce_y_resized = nonce_y[:df_test]
# Test the neural network on the resized ground truth labels
#test_acc = model.evaluate(df_test, nonce_y_resized, verbose=2)
#print('\nTest accuracy:', test_acc)

with open('list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(integer_list)


#####################################
#####################################
#####################################
#####################################
#####################################
#####################################
print("XXXXXXXXXXXXXXX")
#####################################
#####################################
#####################################
#####################################
#####################################
#####################################

# create the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(6, activation="relu", input_shape=[1]),
    tf.keras.layers.Dense(6, activation="relu", name="layer1"),
    tf.keras.layers.Dense(36, activation="relu", name="layer2"),
    tf.keras.layers.Dense(1, activation="relu", name="layer3")
])

# compile the model
#model.compile(optimizer='adam', loss='mean_squared_error', learning_rate = 0.1)
optim = keras.optimizers.Adam(learning_rate=0.01)
model.compile(optimizer='adam',loss='mse', metrics=['accuracy'])

# train the model on the data
history = model.fit(version_x, version_y, epochs=2)
# make predictions using the trained model
predictions = model.predict(version_y)
print("Next version: ", predictions)
integer_list = [int(val[0]) for val in predictions]
#print(integer_list)
#df_test = pd.read_csv("test.csv")
#nonce_y_resized = nonce_y[:df_test]
# Test the neural network on the resized ground truth labels
#test_acc = model.evaluate(df_test, nonce_y_resized, verbose=2)
#print('\nTest accuracy:', test_acc)
with open('list2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(integer_list)

#####################################
#####################################
#####################################
#####################################
#####################################
#####################################
#####################################
test_data = pd.read_csv("test.csv")

# load data from csv file into a pandas dataframe
id_data = test_data["id"].values
nonce_data = test_data["nonce"].values
test_data["hash_int"] = test_data["hash"].apply(lambda x: int(x, 16))
hash_data = test_data["hash_int"].values
test_data["merkle_root_int"] = test_data["merkle_root"].apply(lambda x: int(x, 16))
merkle_root_data = test_data["merkle_root_int"].values

# Convert the string time value to a datetime object
#df["time_value"] = df["time"].datetime.datetime.strptime(time_data, '%m/%d/%y %H:%M')
# Convert the datetime object to a float value representing the number of seconds since the epoch
#time_data_float = (df["time_value"] - datetime.datetime(1970,1,1)).total_seconds()
#time_data = time_data_float.values
#print(time_data)
date_str = test_data["time"].values
date_str = date_str.tolist()[0]
date_format = "%m/%d/%y %H:%M"
date = datetime.strptime(date_str, date_format)
time_data = int(date.timestamp())
version_data = test_data["version"].values
bits_data = test_data["bits"].values

# normalize the input variable
# convert the input variable to a tensor
id_data_tensor = tf.constant(id_data, dtype=tf.float64)
nonce_data_tensor = tf.constant(nonce_data, dtype=tf.float64)
hash_data_tensor = tf.constant(hash_data, dtype=tf.float64)
merkle_root_data_tensor = tf.constant(merkle_root_data, dtype=tf.float64)
time_data_tensor = tf.constant(time_data, dtype=tf.float64)
version_data_tensor = tf.constant(version_data, dtype=tf.float64)
bits_data = tf.constant(bits_data, dtype=tf.float64)

#X and Y variables
#Training Data
id_x = id_data_tensor[:-1]
nonce_x = nonce_data_tensor[:-1]
hash_x = hash_data_tensor[:-1] 
merkle_root_x = merkle_root_data_tensor[:-1]
#time_x = time_data_tensor[:-1]
version_x = version_data_tensor[:-1]
bits_x = bits_data[:-1] 

#Target Data
id_y = id_data_tensor[1:]
nonce_y = nonce_data_tensor[1:]
hash_y = hash_data_tensor[1:] 
merkle_root_y = merkle_root_data_tensor[1:]
#time_y = time_data_tensor[1:]
version_y = version_data_tensor[1:]
bits_y = bits_data[1:] 

############################
############################

# Evaluate the model on the test data
loss, accuracy = model.evaluate(nonce_x, nonce_y)

# Print the test loss and accuracy
print('Test Loss:', loss)
print('Test Accuracy:', accuracy)

# Make predictions on the test data
predictions = model.predict(nonce_y)

# Print the predicted labels and their corresponding probabilities
for i in range(len(nonce_y)):
    predicted_label = tf.argmax(predictions[i]).numpy()
    predicted_prob = tf.math.reduce_max(predictions[i]).numpy()
    print('Example %d: Predicted Label = %d, Probability = %.2f' % (i+1, predicted_label, predicted_prob))