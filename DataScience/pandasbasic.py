# Online Python Playground
# Use the online IDE to write, edit & run your Python code
import pandas as pd
import numpy as np

friends_dict = {"Name":["Audrey", "Vivian", "Eva", "Kenny"],"Age":[22,22,21, np.nan]}
friends_df = pd.DataFrame(friends_dict)
friends_df.insert(2, "BdayMonth", ["August","September", "November", np.nan])
print("Before Replacement")
print(friends_df)
for idx,row in friends_df.iterrows():
    for col in friends_df.columns:
        if pd.isnull(row[col]):
            if col == "BdayMonth":
                friends_df.loc[idx, col] = "May"
            elif col == "Age":
                friends_df.loc[idx, col] = 23

    # if row["BdayMonth"].isnull():
    #     row["BdayMonth"] = "May"
    # if row["Age"].isnull():
    #     row["Age"] = 23
print("After Replacement")
print(friends_df)
