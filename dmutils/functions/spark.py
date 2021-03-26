from pyspark.sql import SparkSession

def create_session(appname):
    return SparkSession.builder.enableHiveSupport().appName(name).getOrCreate()