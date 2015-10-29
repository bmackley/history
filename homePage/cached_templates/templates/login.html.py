# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440718369.385885
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/AssyrianProject2/homePage/templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['nav', 'content']


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
        def nav():
            return render_nav(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nav():
            return render_nav(context)
        __M_writer = context.writer()
        __M_writer('\n  <nav>\n   <div class="nav-wrapper black">\n     <div class="row">\n        <div class="col s3 offset-s1 grid-example"><a href="/" class="brand-logo">Logo</a></div>\n         <div class="col s3 offset-s8 grid-example">  \n        </div>\n      </div>\n    </div>\n  </nav>\n')
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
        __M_writer('\n\n    <div class="container">\n        <center>\n        <div class="card indigo">\n            <div class="card-content white-text">\n                <span class="card-title">Login</span>\n                <span class="white-text">\n                <form method="POST" action = "/homepage/login">\n                  ')
        __M_writer(str( form ))
        __M_writer('\n                  <button class="btn waves-effect waves-light grey darken-1" type="submit" value ="submit"name="action">Submit\n                  </button> \n                </form>\n                </span>\n            </div>\n        </div>\n        </center>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "login.html", "line_map": {"80": 74, "65": 13, "59": 2, "53": 2, "73": 22, "72": 13, "47": 31, "42": 12, "27": 0, "74": 22, "37": 1}, "filename": "/Users/benmackley/Projects/AssyrianProject2/homePage/templates/login.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
