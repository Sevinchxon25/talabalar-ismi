# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nZ0vznLRWz4Pz0OGImiUinGntvobmCVS
"""

import pandas as pd

import pandas as pd

# 1. DataFrame yaratish
data={
    'Ism':['Sevinch','Jumagul','Maftuna','Durdona','Zuhra','Odina','Mubina','Feruzaxon','Qurvonoy','Behruz','Sherbek'],
    'Yoshi':[18,19,32,20,17,20,21,15,25,26,35],
    'Shahar':['Beshariq','Qoqon','Fargona','Buvayda','Xorazm','Beshariq','Quva','Fargona','Xorazm','Navoiy','Samarqand']
}
df=pd.DataFrame(data)
# 2.Ma'lumotni ko'rish
print(df)
# 3.Filtrash
young_people=df[df['Yoshi']<32]
print("32 yoshdan kichiklar:\n",young_people)

#4
df['Yoshi']+=1
print("Yangilangan DataFrame:\n",df)

df.to_excel('df.xlsx')