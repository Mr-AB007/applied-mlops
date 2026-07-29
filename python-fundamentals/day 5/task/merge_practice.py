import pandas as pd

batch1 = pd.DataFrame({
    "name":["Alice","Bob","Charlie","Ram"],
    "id":[1,2,3,4]
})

batch2 = pd.DataFrame({
    "score":[10,20,30,40],
    "id":[1,3,4,5]
})

#Inner join merge

result = pd.merge(batch1,batch2,on="id",how="inner")

#Left join

result_left = pd.merge(batch1,batch2,on="id",how="left")
result_right = pd.merge(batch1,batch2,on="id",how="right")

#Inner join only give matching rows from both batcges
#while left join return all values from left and Nan for right table for missing.