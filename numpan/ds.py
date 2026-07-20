import pandas as pd
import numpy as np


# df = pd.DataFrame({
#     'employee':['A','B','C','D'],
#     'salary':[50000,60000,45000,70000]
# })

# x = df['salary'].max()

# x = df['salary'].mean()

# x = df['salary'].nlargest(2).iloc[-1]

#emp grater then avg salary
# avg_s = df['salary'].mean()
# x = df[df['salary']>avg_s]

# x = df['salary_level'] = df['salary'].apply(lambda x: 'High' if x > 60000 else 'Low')

# df['salary_level'] = np.where(
#     df['salary'] > 60000,
#     'High',
#     'Low'
# )
df = pd.DataFrame({
'dept':['IT','HR','IT','Finance','HR'],
'salary':[50000,45000,60000,55000,48000]
})

# x = df.sort_values(by='salary', ascending=False)
# x = df['salary'].nlargest(3)
x = df.groupby('dept')['salary'].mean().idxmax()
print(x )
