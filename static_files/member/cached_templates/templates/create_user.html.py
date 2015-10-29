# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1410692654.6242
_enable_loop = True
_template_filename = 'C:\\compFITition\\member\\templates/create_user.html'
_template_uri = 'create_user.html'
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
        __M_writer('d\r\n<script src="js/bootstrap-datepicker.js"></script>\r\n<script src="/static/member/scripts/create_user.js"></script>\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
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
        __M_writer('\r\n<div class="jumbotron"\r\n\t<form method="POST">\r\n\t<center>\r\n\t\t<table>\r\n\t\t\t<tbody>\r\n\t\t\t\t')
        __M_writer(str( form ))
        __M_writer('\r\n\t\t\t</tbody>\r\n\t\t</table>\r\n\t</center>\r\n\t<ul style="list-style: none;">\r\n\t\t<center>\r\n\t\t\t<li>\r\n\t            <h3>\r\n\t                <input type="submit" Value="Submit"/>\r\n\t            </h3>\r\n\t        </li>\r\n\t    </center>\r\n\t</ul> \r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\compFITition\\member\\templates/create_user.html", "uri": "create_user.html", "source_encoding": "ascii", "line_map": {"35": 2, "53": 7, "54": 13, "55": 13, "40": 28, "27": 0, "61": 55, "46": 7}}
__M_END_METADATA
"""
