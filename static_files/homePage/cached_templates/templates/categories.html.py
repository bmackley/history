# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394071504.62301
_enable_loop = True
_template_filename = 'C:\\myStuff\\homePage\\templates/categories.html'
_template_uri = 'categories.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'left']


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
        def header():
            return render_header(context._locals(__M_locals))
        catalogProductCatagories = context.get('catalogProductCatagories', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 13
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer("\r\n\t<div class = 'col-md-8'>\r\n\t\t<h1>Categories</h1>\r\n\t</div>\r\n\t<div class = 'col-md-2'>\r\n\t</div>\r\n\t<div class = 'col-md-2'>\r\n\t\t\r\n\t</div>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        catalogProductCatagories = context.get('catalogProductCatagories', UNDEFINED)
        def left():
            return render_left(context)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer('\r\n\t<div class="col-md-1">\r\n')
        # SOURCE LINE 17
        for q in catalogProductCatagories:
            # SOURCE LINE 18
            __M_writer('\t    <p>')
            __M_writer(str(q.name))
            __M_writer('</p>    \r\n')
        # SOURCE LINE 20
        __M_writer('\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


