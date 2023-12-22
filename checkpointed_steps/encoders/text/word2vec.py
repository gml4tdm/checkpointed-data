import typing

import checkpointed
from checkpointed import PipelineStep
from checkpointed.arg_spec import arguments

from ...data_loaders import Word2VecLoader, GloveLoader


class Word2VecEncoder(checkpointed.PipelineStep):

    @classmethod
    def supports_step_as_input(cls, step: type[PipelineStep]) -> bool:
        return step == Word2VecLoader or step == GloveLoader

    async def execute(self, *inputs) -> typing.Any:
        vectors, documents = inputs

    @staticmethod
    def save_result(path: str, result: typing.Any):
        pass

    @staticmethod
    def load_result(path: str):
        pass

    @classmethod
    def get_arguments(cls) -> dict[str, arguments.Argument]:
        pass

    @classmethod
    def get_constraints(cls) -> list[arguments.Constraint]:
        pass