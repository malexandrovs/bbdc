import numpy as np
import pandas as pd
import keras
import glob
import random

files = [filename for filename in glob.glob('s*.csv')]
print(files)
random.shuffle(files)
print (files)

datalist = [pd.read_csv(fn,index_col=0) for fn in files]
train = pd.concat(datalist[:-4]).drop(['Datasets', 'code.1','End time', 'End time.1', 'Datasets.1'],axis=1)
validation = pd.concat(datalist[-4:]).drop(['Datasets', 'code.1','End time', 'End time.1', 'Datasets.1'],axis=1)

train.to_csv('all_training.csv')
validation.to_csv('all_validation.csv')
#model = Sequential()
#model.add(LSTM(28, input_shape=(data.iloc[:,:-12].shape)))
#model.add(Dropout(0.1))
#model.add(Dense(50, activation='relu'))
#model.add(Dense(12,activation='softmax'))
#model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print('start fitting')
#model.fit(data.iloc[:,:-12],data.iloc[:,-12:],epochs=15, batch_size=64, verbose=0)
print('save model')
model.save('model.HDF5')
print('model saved ')
