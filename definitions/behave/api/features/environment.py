import os
import behave_restful.app as br_app

from lib.runner.execute.interact.interact import Interact


# Exemplo de implementação dos gatilhos do BDD


def before_all(context):
    this_directory = os.path.abspath(os.path.dirname(__file__))
    br_app.BehaveRestfulApp().initialize_context(context, this_directory)
    context.hooks.invoke(br_app.BEFORE_ALL, context)


def after_all(context):
    context.hooks.invoke(br_app.AFTER_ALL, context)


def before_feature(context, feature):
    context.hooks.invoke(br_app.BEFORE_FEATURE, context, feature)


def after_feature(context, feature):
    context.hooks.invoke(br_app.AFTER_FEATURE, context, feature)


def before_scenario(context, scenario):
    context.hooks.invoke(br_app.BEFORE_SCENARIO, context, scenario)


def after_scenario(context, scenario):
    context.hooks.invoke(br_app.AFTER_SCENARIO, context, scenario)


def before_step(context, step):
    context.hooks.invoke(br_app.BEFORE_STEP, context, step)


def after_step(context, step):
    context.hooks.invoke(br_app.AFTER_STEP, context, step)


def before_tag(context, tag):
    context.hooks.invoke(br_app.BEFORE_TAG, context, tag)
    context._session = Interact.open_session()
    context.url, context.payload = Interact.load_request_data(tag, 'payload.json')


def after_tag(context, tag):
    context.hooks.invoke(br_app.AFTER_TAG, context, tag)
