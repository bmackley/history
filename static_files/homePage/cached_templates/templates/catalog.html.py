# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1400038561.645017
_enable_loop = True
_template_filename = 'C:\\compfitition\\homePage\\templates/catalog.html'
_template_uri = 'catalog.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content']


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
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        Objects = context.get('Objects', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 13
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 38
        __M_writer('\r\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        Objects = context.get('Objects', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer('\r\n\t<div class="col-md-1">\r\n\t</div>\r\n\t<div class="col-md-11">\r\n')
        # SOURCE LINE 19
        for c in Objects:
            # SOURCE LINE 20
            __M_writer('\t\t\t<div class = \'catalogProduct\'>\r\n\t\t\t  <div class="col-sm-6 col-md-4">\r\n\t\t\t    <div class="thumbnail">\r\n\t\t\t      <img src="')
            # SOURCE LINE 23
            __M_writer(str(STATIC_URL + c.imagePath))
            __M_writer('" width =\'190\' height=\'180\'>\r\n\t\t\t      <div class="caption">\r\n\t\t\t        <a href="/homePage/details/')
            # SOURCE LINE 25
            __M_writer(str(c.id))
            __M_writer('/"><h3>')
            __M_writer(str(c.catalogProductID))
            __M_writer('</h3></a>  \r\n\t\t\t        ')
            # SOURCE LINE 26
            __M_writer(str(c.brand))
            __M_writer("\r\n\t\t\t        <span class = 'price'>")
            # SOURCE LINE 27
            __M_writer(str(c.price))
            __M_writer('</span>\r\n\t\t\t      </div>\r\n\t\t\t    </div>\r\n\t\t\t  </div>\r\n\t\t\t</div>\r\n')
        # SOURCE LINE 33
        __M_writer('\t</div>\r\n\r\n\r\n\t\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


