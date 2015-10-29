# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1426736064.820795
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/compfitition-2.1/member/templates/login.html'
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
    return runtime._inherit_from(context, 'base_ajax_template.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(' ')
        __M_writer('\n\n\n\n')
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
        __M_writer('\n  <div class="row">\n    <div class="col-md-3">\n    </div>\n    <div class="col-md-9">\n      <form method="POST" action =\'/shop/login\'>\n        <table>\n          <tbody>\n            ')
        __M_writer(str( form ))
        __M_writer('\n          </tbody>\n        </table>\n        <input class="btn btn-primary" type="submit" value="Submit" /> \n      </form>\n    </div>\n  </div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "login.html", "filename": "/Users/benmackley/Projects/compfitition-2.1/member/templates/login.html", "line_map": {"35": 1, "36": 1, "54": 5, "55": 13, "56": 13, "41": 22, "27": 0, "62": 56, "47": 5}}
__M_END_METADATA
"""
