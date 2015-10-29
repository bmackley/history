# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394328531.2027
_enable_loop = True
_template_filename = 'C:\\myStuff\\homePage\\templates/calculatecommissions.html'
_template_uri = 'calculatecommissions.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'title']


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
        aggregated = context.get('aggregated', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 6
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        aggregated = context.get('aggregated', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer('\r\n\t<h3>Commissions Report</h3>\r\n\t<table class = "table table-striped table-hover">\r\n\t\t<thead>\r\n\t\t\t<tr class="success">\r\n\t\t\t\t<th>Employee</th>\r\n\t\t\t\t<th>Total</th>\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n')
        # SOURCE LINE 18
        for o in aggregated:
            # SOURCE LINE 19
            __M_writer('\t\t\t\t<tr class="active">\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 20
            __M_writer(str(o.username))
            __M_writer('</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 21
            __M_writer(str(aggregated[o]))
            __M_writer('</td>\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 24
        __M_writer('\t\t</tbody>\r\n\t</table>\r\n\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\r\n  Total Commissions\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


