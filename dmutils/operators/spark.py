from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

__all__ = ["LowSparkSubmitOperator"]


class LowSparkSubmitOperator(SparkSubmitOperator):
    def __init__(self, **kwargs):
        super().__init__(
            executor_cores="4",
            executor_memory="8g",
            num_executors="2",
            master="yarn",
            verbose=True,
            yarn_queue="AIRFLOW",
            spark_binary="/bin/spark-submit22",
            conf={
                "spark.dynamicAllocation.enabled": "true",
                "spark.dynamicAllocation.initialExecutors": "2",
                "spark.dynamicAllocation.minExecutors": "2",
                "spark.dynamicAllocation.maxExecutors": "8",
                "spark.shuffle.service.enabled": "true",
            },
            **kwargs
        )
