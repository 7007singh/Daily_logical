import pandas as pd


df = pd.DataFrame({
    'employee':['A','B','C','D'],
    'salary':[50000,60000,45000,70000]
})

x = df['salary'].nlargest(2)
print(x)
