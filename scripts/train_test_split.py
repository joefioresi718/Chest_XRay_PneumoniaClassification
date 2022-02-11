import os
import pandas as pd
import random
import shutil


img_list = os.listdir('../images/data/')
anno_list = pd.read_csv('../files/Cell_Defect_Labels.csv')

shutil.rmtree('../images/data/train/')
shutil.rmtree('../images/data/test/')
os.mkdir('../images/data/train/')
os.mkdir('../images/data/test/')

df_train = pd.DataFrame(columns=['images', 'label'])
df_test = pd.DataFrame(columns=['images', 'label'])

for i in img_list:
    if os.path.isdir('../images/data/' + i):
        continue
    temp_row = anno_list.loc[anno_list['images'] == i]
    if random.random() < 0.8:
        shutil.copy('../images/data/' + i, '../images/data/train/')
        df_train = df_train.append(temp_row, ignore_index=True)
    else:
        shutil.copy('../images/data/' + i, '../images/data/test/')
        df_test = df_test.append(temp_row, ignore_index=True)

df_train.to_csv('../files/train_labels.csv', index=False)
df_test.to_csv('../files/test_labels.csv', index=False)
