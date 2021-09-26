from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result


class Operation(ActionRunner):

    def __init__(self, **kwargs):
        pass

    async def run(self, payload):
        return Result(port="payload", value=payload)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_string_operations.plugin',
            className='Operation',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Patryk Migaj",
            init={}
        ),
        metadata=MetaData(
            name='trardi-string-operations',
            desc='This plug-in is to make a string operations like: lowercase remove spaces split and other',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )