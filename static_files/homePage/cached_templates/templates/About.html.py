# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1410692654.6652
_enable_loop = True
_template_filename = 'C:\\compFITition\\homePage\\templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t\t\t<div class="jumbotron">\r\n\t\t\t\t<h3>\r\n\t\t\t\t\t<center>\r\n\t\t\t\t\t\tCompFITition strives to be the best competitve platform for personal and commercial use. We provide a motivational atmosphere that allows users to interact with their friends and peers to push each other to new limits.\r\n\t\t\t\t\t</center>\r\n\t\t\t\t</h3>\r\n\t\t\t</div>\r\n\t\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\compFITition\\homePage\\templates/about.html", "uri": "about.html", "source_encoding": "ascii", "line_map": {"34": 1, "51": 3, "39": 13, "57": 51, "27": 0, "45": 3}}
__M_END_METADATA
"""
