from django import template
from django.utils.crypto import get_random_string
from django.templatetags import static

register = template.Library()


class StaticExtraNode(static.StaticNode):

    def render(self, context):
        return super().render(context) + '?v=' + get_random_string(32)


@register.tag('static_no_cache')
def do_static_extra(parser, token):
    return StaticExtraNode.handle_token(parser, token)


def static_extra(path):
    return StaticExtraNode.handle_simple(path)
