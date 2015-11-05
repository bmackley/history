# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446737713.502876
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/history/homePage/templates/login.html'
_template_uri = 'login.html'
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
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
        __M_writer('\n\n    <div class="container">\n        <center>\n        <div class="card indigo">\n            <div class="card-content white-text">\n                <span class="card-title">Login</span>\n                <span class="white-text">\n                <form method="POST" action = "/homePage/hotspots">\n                  ')
        __M_writer(str( form ))
        __M_writer('\n                  <button class="btn waves-effect waves-light grey darken-1" type="submit" value ="submit"name="action">Submit\n                  </button> \n                </form>\n                </span>\n            </div>\n        </div>\n        </center>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"36": 1, "54": 3, "55": 12, "56": 12, "41": 21, "28": 0, "62": 56, "47": 3}, "filename": "/Users/benmackley/Projects/history/homePage/templates/login.html", "uri": "login.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
