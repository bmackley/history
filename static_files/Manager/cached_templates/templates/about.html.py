# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1389398854.385254
_enable_loop = True
_template_filename = 'C:\\mystuff\\homePage\\templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer', 'center', 'left_side']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def footer():
            return render_footer(context._locals(__M_locals))
        def center():
            return render_center(context._locals(__M_locals))
        def left_side():
            return render_left_side(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_side'):
            context['self'].left_side(**pageargs)
        

        # SOURCE LINE 8
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        # SOURCE LINE 28
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer("\n<br>\n<br>\n<h3>ABOUT</h3>\n<br>\nWe started as professors at traditional universities. We still are; we teach classes, we serve in our disciplines, we write textbooks, and we conduct research. We understand what it means to be academics.\n\n\nSince becoming professors, we had watched textbook prices steadily increase even while publishing and distribution costs decreased.\n\n\nWe also realized the market for educational materials was shifting. Traditional textbooks were being enveloped by digital materials which offered much more convenience, flexibility, and dynamic content. More and more students were bringing laptops and tablets to school.\n\n\nWe decided to start new type of publishing company in 2010. We strive for textbooks that not only can be used at the world's best institutions, but also that can remain low cost. Further, we embed section-level videos, adaptive problem sets, and other technologies the modern web provides.\n\n\nCome, and rediscover the textbook. We think you'll be pleased.\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_side(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_side():
            return render_left_side(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n<br>\n<br>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


