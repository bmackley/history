# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440794169.514989
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/AssyrianProject2/homePage/templates/create_user.html'
_template_uri = 'create_user.html'
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
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

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
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="container">\n        <center>\n        <div class="card black">\n            <div class="card-content amber-text">\n              <h1 class="red-text text-darken-4">Create Account</h1>\n              <form method ="POST" action = "/homepage/create_user">\n                <div class="input-field col s12">\n                <tr><th><label for="id_username">Username:</label></th><td><input class="form-control" id="id_username" name="username" type="text" /></td></tr>\n                </div>\n                <div class="input-field col s12">\n                <tr><th><label for="id_email">Email:</label></th><td><input class="form-control" id="id_email" name="email" type="text" /></td></tr>\n                </div>\n                <div class="input-field col s12">\n                <tr><th><label for="id_password">Password:</label></th><td><input class="form-control" id="id_password" name="password" type="password" /></td></tr>\n                </div>\n                <div class="input-field col s12">\n                <tr><th><label for="id_retypepassword">Re-Enter Password:</label></th><td><input class="form-control" id="id_retypepassword" name="retypepassword" type="password" /></td></tr>\n                </div>\n                <button class="btn waves-effect waves-light grey darken-1" type="submit" name="action">Submit\n                </button> \n              </form>\n            </div>\n        </div>\n        </center>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"75": 69, "51": 2, "36": 1, "69": 13, "57": 2, "41": 12, "27": 0, "63": 13}, "filename": "/Users/benmackley/Projects/AssyrianProject2/homePage/templates/create_user.html", "uri": "create_user.html"}
__M_END_METADATA
"""
