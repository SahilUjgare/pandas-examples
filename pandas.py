#create_dataframe.py
import pandas as pd

# Creating DataFrame from dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "Paris", "London", "Tokyo"]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
# Display basic info
print("\nInfo:")
print(df.info())
# Display statistics
print("\nStatistics:")
print(df.describe())


#filter_sort.py
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "Score": [85, 90, 78, 88, 95]
})
# Filtering
print("Students with Score > 85:")
print(df[df["Score"] > 85])
# Sorting
print("\nSorted by Age:")
print(df.sort_values("Age"))



#groupby.py
import pandas as pd

# Sample Data
data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Salary": [60000, 52000, 58000, 72000, 50000, 68000]
}
df = pd.DataFrame(data)
# Group by Department and calculate average salary
avg_salary = df.groupby("Department")["Salary"].mean()
print("Average Salary by Department:")
print(avg_salary)



#merge_concat.py
import pandas as pd

# DataFrame 1
df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
})
# DataFrame 2
df2 = pd.DataFrame({
    "ID": [1, 2, 4],
    "Score": [85, 90, 75]
})
# Merge
merged = pd.merge(df1, df2, on="ID", how="outer")
print("Merged DataFrame:")
print(merged)
# Concatenate
concat_df = pd.concat([df1, df2], axis=0, ignore_index=True)
print("\nConcatenated DataFrame:")
print(concat_df)

