all = ["LOW"]

LOW = {
    "spark_binary": "/bin/spark-submit",
    "executor_cores": "4",
    "executor_memory": "8g",
    "num_executors": "2",
    "master": "yarn",
    "verbose": True,
    "yarn_queue": "AIRFLOW",
    "conf": {
        "spark.dynamicAllocation.enabled": "true",
        "spark.dynamicAllocation.initialExecutors": "2",
        "spark.dynamicAllocation.minExecutors": "2",
        "spark.dynamicAllocation.maxExecutors": "8",
        "spark.shuffle.service.enabled": "true",
    },
}
