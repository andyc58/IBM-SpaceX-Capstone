import pandas as pd
spacex_df = pd.read_csv("spacex_launch_dash.csv")



def Odds(x):
    p = x.mean()
    return p/(1-p)

print(spacex_df.groupby(['Launch Site'])['class']\
            .agg(['mean' ,Odds])\
            .rename(columns={'mean':'Success Probability'})
        
)

