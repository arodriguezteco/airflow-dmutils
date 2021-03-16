from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

class LowSparkSubmitOperator(SparkSubmitOperator):
    def __init__(self,
        executor_cores='4',
        executor_memory='8g',
        num_executors="2",
        master="yarn",
        verbose=True,
        yarn_queue="AIRFLOW",
        conf=",".join([
            "spark.dynamicAllocation.enabled=true",
            "spark.dynamicAllocation.initialExecutors=2",
            "spark.dynamicAllocation.minExecutors=2",
            "spark.dynamicAllocation.maxExecutors=8",
            "spark.shuffle.service.enabled=true",
        ]),
        **kwargs
    ):
        super().__init__(**kwargs)