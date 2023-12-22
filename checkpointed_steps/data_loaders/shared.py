import abc

import checkpointed
from checkpointed.arg_spec.constraints import Constraint
from checkpointed.arg_spec.arguments import Argument, StringArgument


class GenericFileLoader(checkpointed.PipelineStep, abc.ABC):

    @classmethod
    def supports_step_as_input(cls, step: type[checkpointed.PipelineStep]) -> bool:
        return False

    @classmethod
    def get_arguments(cls) -> dict[str, Argument]:
        return {
            'filename': StringArgument(
                name='filename',
                description='Path to the file to load'
            )
        }

    @classmethod
    def get_constraints(cls) -> list[Constraint]:
        return []
