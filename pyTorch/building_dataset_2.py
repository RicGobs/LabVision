import numpy as np
import pandas as pd

data_bbox1 = np.load('/home/riccardo/Desktop/finale/annotations/data_bbox1.npy')
data_bbox2 = np.load('/home/riccardo/Desktop/finale/annotations/data_bbox2.npy')
data_bbox3 = np.load('/home/riccardo/Desktop/finale/annotations/data_bbox3.npy')
data_bbox4 = np.load('/home/riccardo/Desktop/finale/annotations/data_bbox4.npy')
data_bbox5 = np.load('/home/riccardo/Desktop/finale/annotations/data_bbox5.npy')
data_bbox6 = np.load('/home/riccardo/Desktop/finale/annotations/data_bbox6.npy')
data_bbox7 = np.load('/home/riccardo/Desktop/finale/annotations/data_bbox7.npy')
data_bbox8 = np.load('/home/riccardo/Desktop/finale/annotations/data_bbox8.npy')
data_bbox10 = np.load('/home/riccardo/Desktop/finale/annotations/data_bbox10.npy')
data_bbox11 = np.load('/home/riccardo/Desktop/finale/annotations/data_bbox11.npy')

data_names1 = np.load('/home/riccardo/Desktop/finale/annotations/data_names1.npy')
data_names2 = np.load('/home/riccardo/Desktop/finale/annotations/data_names2.npy')
data_names3 = np.load('/home/riccardo/Desktop/finale/annotations/data_names3.npy')
data_names4 = np.load('/home/riccardo/Desktop/finale/annotations/data_names4.npy')
data_names5 = np.load('/home/riccardo/Desktop/finale/annotations/data_names5.npy')
data_names6 = np.load('/home/riccardo/Desktop/finale/annotations/data_names6.npy')
data_names7 = np.load('/home/riccardo/Desktop/finale/annotations/data_names7.npy')
data_names8 = np.load('/home/riccardo/Desktop/finale/annotations/data_names8.npy')
data_names10 = np.load('/home/riccardo/Desktop/finale/annotations/data_names10.npy')
data_names11 = np.load('/home/riccardo/Desktop/finale/annotations/data_names11.npy')

print(data_names1.size)
print(data_names2.size)
print(data_names3.size)
print(data_names5.size)
print(data_names4.size)
print(data_names6.size)
print(data_names7.size)
print(data_names8.size)
print(data_names10.size)
print(data_names11.size)

data_attenction1 = np.load('/home/riccardo/Desktop/finale/annotations/data_attenction1.npy')
data_attenction2 = np.load('/home/riccardo/Desktop/finale/annotations/data_attenction2.npy')
data_attenction3 = np.load('/home/riccardo/Desktop/finale/annotations/data_attenction3.npy')
data_attenction4 = np.load('/home/riccardo/Desktop/finale/annotations/data_attenction4.npy')
data_attenction5 = np.load('/home/riccardo/Desktop/finale/annotations/data_attenction5.npy')
data_attenction6 = np.load('/home/riccardo/Desktop/finale/annotations/data_attenction6.npy')
data_attenction7 = np.load('/home/riccardo/Desktop/finale/annotations/data_attenction7.npy')
data_attenction8 = np.load('/home/riccardo/Desktop/finale/annotations/data_attenction8.npy')
data_attenction10 = np.load('/home/riccardo/Desktop/finale/annotations/data_attenction10.npy')
data_attenction11 = np.load('/home/riccardo/Desktop/finale/annotations/data_attenction11.npy')


data_bbox=np.concatenate((data_bbox1, data_bbox2), axis=0)
data_bbox=np.concatenate((data_bbox, data_bbox7), axis=0)
data_bbox=np.concatenate((data_bbox, data_bbox3), axis=0)
data_bbox=np.concatenate((data_bbox, data_bbox4), axis=0)
data_bbox=np.concatenate((data_bbox, data_bbox5), axis=0)
data_bbox=np.concatenate((data_bbox, data_bbox6), axis=0)
data_bbox=np.concatenate((data_bbox, data_bbox8), axis=0)
data_bbox=np.concatenate((data_bbox, data_bbox10), axis=0)
data_bbox=np.concatenate((data_bbox, data_bbox11), axis=0)

data_names=np.concatenate((data_names1, data_names2), axis=0)
data_names=np.concatenate((data_names, data_names7), axis=0)
data_names=np.concatenate((data_names, data_names3), axis=0)
data_names=np.concatenate((data_names, data_names4), axis=0)
data_names=np.concatenate((data_names, data_names5), axis=0)
data_names=np.concatenate((data_names, data_names6), axis=0)
data_names=np.concatenate((data_names, data_names8), axis=0)
data_names=np.concatenate((data_names, data_names10), axis=0)
data_names=np.concatenate((data_names, data_names11), axis=0)

data_attenction=np.concatenate((data_attenction1, data_attenction2), axis=0)
data_attenction=np.concatenate((data_attenction, data_attenction7), axis=0)
data_attenction=np.concatenate((data_attenction, data_attenction3), axis=0)
data_attenction=np.concatenate((data_attenction, data_attenction4), axis=0)
data_attenction=np.concatenate((data_attenction, data_attenction5), axis=0)
data_attenction=np.concatenate((data_attenction, data_attenction6), axis=0)
data_attenction=np.concatenate((data_attenction, data_attenction8), axis=0)
data_attenction=np.concatenate((data_attenction, data_attenction10), axis=0)
data_attenction=np.concatenate((data_attenction, data_attenction11), axis=0)


np.save("/home/riccardo/Desktop/finale/data_names",data_names)
np.save("/home/riccardo/Desktop/finale/data_bbox",data_bbox)
np.save("/home/riccardo/Desktop/finale/data_attenction",data_attenction)
