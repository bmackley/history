# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1405792653.52821
_enable_loop = True
_template_filename = 'C:\\compfitition\\Manager\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['website', 'menu', 'footer', 'content', 'center', 'header']


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
        def website():
            return render_website(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'website'):
            context['self'].website(**pageargs)
        

        # SOURCE LINE 5
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        # SOURCE LINE 23
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 27
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        # SOURCE LINE 34
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 38
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        # SOURCE LINE 41
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_website(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def website():
            return render_website(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer('\r\n  <div class="row">\r\n   \r\n    <div class="col-md-9">\r\n\r\n      <ul class="nav nav-pills">\r\n        <li class="active"><a href="/member/index">Home</a></li>\r\n        <li><a href="/Manager/groups">Groups</a></li>\r\n      </ul>\r\n    </div>\r\n    <div class=\'col-md-3\'>\r\n')
        # SOURCE LINE 17
        if request.user.is_authenticated():
            # SOURCE LINE 18
            __M_writer('      <a href=\'/Manager/index\' class="navbar-link"> Welcome ')
            __M_writer(str(request.user.first_name))
            __M_writer('</a>\r\n')
        # SOURCE LINE 20
        __M_writer("      <a class='btn btn-danger' href= '/Manager/logout'>Log Out</a>\r\n    </div>\r\n  </div>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 36
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer('\r\n<div class="row">\r\n  <div class="col-md-8"></div>\r\n  <div class="col-md-4"></div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


