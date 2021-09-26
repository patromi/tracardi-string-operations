from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result
from tracardi_string_operations.model.configuration import Configuration
from tracardi_string_operations.service.operations import convert
from tracardi_dot_notation.dot_accessor import DotAccessor


class OperatorActions(ActionRunner):

    def __init__(self, **kwargs):
        self.config = Configuration(**kwargs)

    async def run(self, payload):
        dot = DotAccessor(self.profile, self.session, payload, self.event, self.flow)
        string = dot[self.config.string]

        return Result(port="payload", value=convert(string))


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_string_operations.plugin',
            className='OperationActions',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Patryk Migaj",
            init={
                "operation": None,
                "string": "event@dane"
            }
        ),
        metadata=MetaData(
            name='String operations',
            desc='This plug-in is to make a string operations like: lowercase remove spaces split and other',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )
