from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pandas as pd

S3_DATA_SOURCE_PATH = "s3://myawsbucket-ajarabani/PKL/RAW_LBR.PKL"
S3_DATA_OUTPUT_PATH = "s3://myawsbucket-ajarabani/data-output"
raw_lbr = pd.read_pickle(S3_DATA_SOURCE_PATH)


def main():
    spark = SparkSession.builder.appName("demoapp").getOrCreate()
    raw_lbr = spark.createDataFrame(raw_lbr)
    print(f"Total number of records {raw_lbr.count()}")
    raw_lbr = raw_lbr.withColumn("HRS/EA", col("HRS_WORKED") / col("OP_QTY"))
    raw_lbr.select("OP_QTY").show()
    raw_lbr.write.mode("overwrite").parquet(S3_DATA_OUTPUT_PATH)
    print(f"Selected data was successfully saved to s3 {S3_DATA_OUTPUT_PATH}")


if __name__ == "__main__":
    main()
