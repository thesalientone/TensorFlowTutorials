import math
import urllib2 as url

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

urltext = "https://storage.googleapis.com/mledu-datasets/california_housing_train.csv"
response = url.urlopen(urltext)
california_housing_dataframe = pd.read_csv(response)

#print california_housing_dataframe.head()

california_housing_dataframe = california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0
print california_housing_dataframe.describe()
# Define the input feature: total_rooms
my_feature = california_housing_dataframe[["total_rooms"]]
# Configure a numeric feature column for total_rooms
feature_columns = [tf.feature_column.numeric_column("total_rooms")]


#Define the label.
targets = california_housing_dataframe["median_house_value"]

# Use gradient descent as the optimizer for training the model`
