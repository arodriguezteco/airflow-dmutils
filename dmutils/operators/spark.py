from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

__all__ = ["LowSparkSubmitOperator"]

class LowSparkSubmitOperator(SparkSubmitOperator):
    def __init__(
        self,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.executor_cores="4",
        self.executor_memory="8g",
        self.num_executors="2",
        self.master="yarn",
        self.verbose=True,
        self.yarn_queue="AIRFLOW",
        self.spark_binary="/bin/spark-submit22",
        self.conf=",".join(
            [
                "spark.dynamicAllocation.enabled=true",
                "spark.dynamicAllocation.initialExecutors=2",
                "spark.dynamicAllocation.minExecutors=2",
                "spark.dynamicAllocation.maxExecutors=8",
                "spark.shuffle.service.enabled=true",
            ]
        ),
