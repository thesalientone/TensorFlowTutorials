import pandas as pd
import urllib2


print pd.__version__

x = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
y = pd.Series([852469, 1015785, 485199])

z = pd.DataFrame({'City name': x, 'Population': y})

response = urllib2.urlopen("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv")
text = response.read()
california_housing_dataframe = pd.read_csv(text, sep=",")
california_housing_dataframe.head
