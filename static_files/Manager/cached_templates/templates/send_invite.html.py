# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1408197213.268893
_enable_loop = True
_template_filename = 'C:\\compfitition\\Manager\\templates/send_invite.html'
_template_uri = 'send_invite.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'header', 'footer']


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
        def header():
            return render_header(context._locals(__M_locals))
        gid = context.get('gid', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 6
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 25
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        # SOURCE LINE 29
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        gid = context.get('gid', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer("\r\n<div class = 'col-md-5'>\r\n\r\n</div>\r\n<div class = 'col-md-5'>\r\n</div>\r\n<div class = 'col-md-2'>\r\n\t<a class='btn btn-info' href='/Manager/groups/")
        # SOURCE LINE 14
        __M_writer(str(gid))
        __M_writer('\'>Back to Groups</a>\r\n</div>\r\n\t<form method="POST">\r\n\t<table>\r\n\t\t<tbody>\r\n\t\t\t')
        # SOURCE LINE 19
        __M_writer(str( form ))
        __M_writer('\r\n\t\t</tbody>\r\n\t</table>\r\n\t<input class="btn btn-primary" type="submit" value="Submit" /> \r\n\t</form>\r\n</div>\r\n')
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
        __M_writer('\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


