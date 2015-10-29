# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394329558.791475
_enable_loop = True
_template_filename = 'C:\\myStuff\\shop\\templates/delete.html'
_template_uri = 'delete.html'
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
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\r\n<div class="row">\r\n<p></p>\r\n</div>\r\n<div class="row">\r\n<p></p>\r\n</div>\r\n<div class="row">\r\n<p></p>\r\n</div>\r\n<div class="row">\r\n  <div class="col-md-4">\r\n  </div>\r\n  <div class="col-md-5">\r\n  \t<form method="POST">\r\n\t<table>\r\n\t<h1>You have been logged out</h1>\r\n\t\t<tbody>\r\n\t\t</tbody>\r\n\t</table>\r\n\t<a class=\'btn btn-info\' href=\'/Manager/logout/\'>ok</a>\r\n\t\r\n\t</form>\r\n  </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


