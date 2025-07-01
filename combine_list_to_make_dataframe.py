list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3, 4]

# for r in list(zip(list1,list2)):
#     print(r)

df = spark.createDataFrame(list(zip(list1,list2)),["name","value"])
display(df)
