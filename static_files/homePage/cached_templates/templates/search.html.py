# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1407608591.112314
_enable_loop = True
_template_filename = 'C:\\compfitition\\homePage\\templates/search.html'
_template_uri = 'search.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer', 'header', 'products', 'content']


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
        def header():
            return render_header(context._locals(__M_locals))
        results = context.get('results', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def products():
            return render_products(context._locals(__M_locals))
        Objects = context.get('Objects', UNDEFINED)
        search = context.get('search', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 13
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 41
        __M_writer('\r\n\r\n\r\n\r\n\r\n<div class="col-md-8">\r\n\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'products'):
            context['self'].products(**pageargs)
        

        # SOURCE LINE 48
        __M_writer('\r\n</div>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        # SOURCE LINE 52
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer('\r\n\r\n')
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
        __M_writer("\r\n\t<div class = 'col-md-8'>\r\n\t\t<h1>Catalog</h1>\r\n\t</div>\r\n\t<div class = 'col-md-2'>\r\n\t</div>\r\n\t<div class = 'col-md-2'>\r\n\t\t\r\n\t</div>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_products(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def products():
            return render_products(context)
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer('\r\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        Objects = context.get('Objects', UNDEFINED)
        results = context.get('results', UNDEFINED)
        search = context.get('search', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer('\r\n')
        # SOURCE LINE 16
        if search == True:
            # SOURCE LINE 17
            if results == False:
                # SOURCE LINE 18
                __M_writer('\t\t\t<center>\r\n\t\t\tNo results.  Please search again\r\n\t\t\t</center>\r\n')
            # SOURCE LINE 22
            for c in Objects:
                # SOURCE LINE 23
                __M_writer('\t\t<div class = \'Groups\'>\r\n\t\t\t<div class="col-sm-6 col-md-4">\r\n\t\t\t    <div class="thumbnail">\r\n\t\t\t    <a href="/member/join/')
                # SOURCE LINE 26
                __M_writer(str(c.id))
                __M_writer('" class="btn btn-primary btn-primary"><span class = \'title\'> </span></a>\r\n\t\t\t    \r\n\t\t\t      <div class="caption">  \r\n\t\t\t        <div class = \'brand\'>')
                # SOURCE LINE 29
                __M_writer(str(c.groupName))
                __M_writer("</div>\r\n\t\t\t        <div class = 'price'>")
                # SOURCE LINE 30
                __M_writer(str(c.city))
                __M_writer('</div>\r\n\t\t\t      </div>\r\n\t\t\t    </div>\r\n\t\t  \t</div>\r\n\t\t</div>\r\n')
            # SOURCE LINE 36
        else:
            # SOURCE LINE 37
            __M_writer('\t\t<center>\r\n\t\t\t"Search did not return any results"\r\n\t\t</center>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


