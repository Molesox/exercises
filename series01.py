import pandas as pd
import seaborn as sns


def main():
    rawData = pd.read_csv("NVS.txt"," ")

    print(rawData.describe())
    
    
    
if __name__ == "__main__":
    main()