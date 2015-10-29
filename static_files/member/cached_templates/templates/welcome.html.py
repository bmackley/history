# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407901875.890773
_enable_loop = True
_template_filename = 'C:\\CompFITition\\member\\templates/welcome.html'
_template_uri = 'welcome.html'
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
    return runtime._inherit_from(context, 'base_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 26
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
        # SOURCE LINE 8
        __M_writer('\r\n\t\r\n\t<div class="jumbotron">\r\n\t\t<center>\r\n\t\t<h2>\r\n\t\tWELCOME TO COMPFITITION\r\n\t\t</h2>\r\n\t\t</center>\r\n\t\t<p>\r\n\t\t    <center>\r\n\t\t\t    <a class="btn btn-primary btn-lg" id="login_button" role="button">\r\n\t\t\t    \tLog in Here!\r\n\t\t\t    </a>\r\n\t\t    </center>\r\n\t    </p>\r\n\t</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


