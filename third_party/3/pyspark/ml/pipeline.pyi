# Stubs for pyspark.ml.pipeline (Python 3.5)
#

from typing import Any, List, Optional, Union
from pyspark.ml.base import Estimator, Model, Transformer
from pyspark.ml.param import Param
from pyspark.ml.util import JavaMLWriter, JavaMLReader, MLReadable, MLWritable

PipelineStage = Union[Estimator, Transformer]

class Pipeline(Estimator, MLReadable, MLWritable):
    stages = ...  # type: Any
    def __init__(self, stages: Optional[List[PipelineStage]] = ...) -> None: ...
    def setStages(self, stages: List[PipelineStage]) -> Pipeline: ...
    def getStages(self) -> List[PipelineStage]: ...
    def setParams(self, stages: Optional[List[PipelineStage]] = ...) -> Pipeline: ...
    def copy(self, extra: Optional[Dict[Param, Any]] = ...) -> Pipeline: ...
    def write(self) -> JavaMLWriter: ...
    def save(self, path) -> None: ...
    @classmethod
    def read(cls) -> JavaMLReader: ...

class PipelineModel(Model, MLReadable, MLWritable):
    stages = ...  # type: Any
    def __init__(self, stages: List[Transformer]) -> None: ...
    def copy(self, extra: Optional[Dict[Param, Any]] = ...) -> PipelineModel: ...
    def write(self) -> JavaMLWriter: ...
    def save(self, path) -> None: ...
    @classmethod
    def read(cls) -> JavaMLReader: ...