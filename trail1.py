import pandas as pd
class Data:
    def __init__(self,file):
        self.file=file
    def data_frame(self):
        df=pd.read_csv(self.file)

        return df
    def hi(self):
        s=Data.data_frame(self)
        print(s.head())
d=Data("sales5.csv")
d.hi()

