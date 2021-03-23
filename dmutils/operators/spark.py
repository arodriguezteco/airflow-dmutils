from dmutils.config.cluster import LOW
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

__all__ = ["LowSparkSubmitOperator"]


class LowSparkSubmitOperator(SparkSubmitOperator):
    def __init__(self, **kwargs):
        kwargs = kwargs.update(LOW)
        super().__init__(**kwargs)
