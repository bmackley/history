# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393979158.947204
_enable_loop = True
_template_filename = 'C:\\myStuff\\Manager\\templates/catalogProductCategories.html'
_template_uri = 'catalogProductCategories.html'
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
        catalogProductCategories = context.get('catalogProductCategories', UNDEFINED)
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
        

        # SOURCE LINE 42
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        # SOURCE LINE 46
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        catalogProductCategories = context.get('catalogProductCategories', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer('\r\n<div class = \'row\'>\r\n\t<div class = \'col-md-8\'>\r\n\t\t\t<h1>Catalog Items</h1>\r\n\t</div>\r\n\t<div class = \'col-md-2\'>\r\n\t</div>\r\n\t<div class = \'col-md-2\'>\r\n\t\t<a class=\'btn btn-info\' href=\'/Manager/edit_catalogProductCategories/new\'>New Catalog Product Category</a>\r\n\t</div>\r\n</div>\r\n<div class="col-md-11">\r\n\t<table class= "table table-striped table-hover">\r\n\t\t\t<thead>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>name</th>\r\n\t\t\t\t\t<th>url</th>\r\n\t\t\t\t\t<th>imagePath</th>\r\n\t\t\t\t\t<th>description</th>\r\n\t\t\t\t</tr>\r\n\t\t\t</thead>\r\n\t\t\t<tbody>\r\n')
        # SOURCE LINE 29
        for q in catalogProductCategories:
            # SOURCE LINE 30
            __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 31
            __M_writer(str(q.name))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 32
            __M_writer(str(q.url))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 33
            __M_writer(str(q.imagePath))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 34
            __M_writer(str(q.description))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td><a href="/Manager/edit_catalogProductCategories/')
            # SOURCE LINE 35
            __M_writer(str(q.id))
            __M_writer('/">Edit</a></td>\r\n\t\t\t\t\t\t<td><a class=\'btn btn-danger\' href=\'/Manager/catalogProductCategories/delete/')
            # SOURCE LINE 36
            __M_writer(str(q.id))
            __M_writer("/'>delete</a></td>\r\n\t\t\t\t\t</tr>\r\n")
        # SOURCE LINE 39
        __M_writer('\t\t\t</tbody>\r\n\t</table>\r\n</div>\r\n')
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
        # SOURCE LINE 44
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


