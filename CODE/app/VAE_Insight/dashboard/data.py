import numpy as np
import pandas as pd

def create_dataframe():
    df1 = pd.read_excel("VAE_Insight/dashboard/clean_input.xlsx")
    df2 = pd.read_excel("VAE_Insight/dashboard/clean_output.xlsx")
    df = pd.concat([df1, df2], axis=0, ignore_index=True)
    df = df.iloc[:, 2:]
    df.fillna(0, inplace=True)
    df = df.astype(int)
    return df