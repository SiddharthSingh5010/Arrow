import pandas as pd
import numpy as np
import multiprocessing as mp
from deep_translator import GoogleTranslator
import time

def translate_text(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text[:2000])
    return translated


if __name__=='__main__':
    df=pd.read_csv('Learning/multiprocessing/train.csv')
    df=df[:1000]

    print('Without Multiprocessing:')
    t=time.time()
    df['Translated']=df['job_description'].apply(translate_text)
    print(time.time()-t)
    print("------------")
    print('With Multiprocessing')
    p=mp.Pool(8)
    t=time.time()
    df['Translated']=p.map(translate_text,df['job_description'])
    print(time.time()-t)

    print('TADA')