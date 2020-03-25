import numpy
import pandas

loaded = pandas.read_csv('../all_training.csv', index_col=0, nrows=10000)
loaded.to_csv('small_data.csv')
