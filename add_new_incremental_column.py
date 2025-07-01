df = spark.createDataFrame([
("Alice", 1),
("Bob", 2),
("Charlie", 3),
], ["Name", "Value"])

df.show()

from pyspark.sql.functions import monotonically_increasing_id

df1 = df.withColumn("index",monotonically_increasing_id())
display(df1)
