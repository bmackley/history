# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446759657.537765
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/history/base_app/templates/base_template.htm'
_template_uri = 'base_template.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'head', 'footer', 'header']


from base_app import static_files 

import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def footer():
            return render_footer(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def head():
            return render_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n\n</body>\n      \n</html>\n\n')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        static_renderer = context.get('static_renderer', UNDEFINED)
        def head():
            return render_head(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <head>\n    <title>\n    Assyrian Project\n    </title>\n    \n    <!-- Meta -->\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer(' \n  ')
        __M_writer('\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n    \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 37, "70": 25, "76": 25, "17": 5, "82": 10, "19": 19, "21": 0, "100": 28, "90": 10, "91": 18, "92": 18, "93": 18, "94": 19, "36": 3, "37": 5, "38": 6, "42": 6, "47": 20, "112": 21, "52": 23, "118": 21, "57": 27, "124": 118, "106": 28, "62": 30, "63": 37}, "filename": "/Users/benmackley/Projects/history/base_app/templates/base_template.htm", "uri": "base_template.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
