# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1430354240.509098
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/compfitition-2.1/member/templates/create_group.html'
_template_uri = 'create_group.html'
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div id="wrapper">\n<!-- PAGE TITLE -->\n\t\t\t<header id="page-title">\n\t\t\t\t<div class="container">\n\t\t\t\t\t<h1>Create Group</h1>\n\n\t\t\t\t\t<ul class="breadcrumb">\n\t\t\t\t\t\t<li><a href="http://localhost:8000/">Home</a></li>\n\t\t\t\t\t\t<!--need a general user page-->\n\t\t\t\t\t\t<li><a href="#">User</a></li>\n\t\t\t\t\t\t<li class="active">Create Group</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t</header>\n\n<div class="jumbotron">\n<center>\n\t<form method="POST">\n\t<table>\n\t\t<tbody>\n\t\t\t')
        __M_writer(str( form ))
        __M_writer('\n\t\t</tbody>\n\t</table>\n<input class="btn btn-primary" type="submit" value="Submit" /> \n</center>\n</div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "create_group.html", "source_encoding": "ascii", "filename": "/Users/benmackley/Projects/compfitition-2.1/member/templates/create_group.html", "line_map": {"35": 2, "36": 3, "54": 5, "55": 27, "56": 27, "41": 35, "27": 0, "62": 56, "47": 5}}
__M_END_METADATA
"""
