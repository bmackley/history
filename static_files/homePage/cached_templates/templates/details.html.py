# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394248068.306556
_enable_loop = True
_template_filename = 'C:\\myStuff\\homePage\\templates/details.html'
_template_uri = 'details.html'
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
        product = context.get('product', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        product = context.get('product', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\r\n<div id = "details">\t\r\n<div class="panel panel-default">\r\n  \r\n\r\n<table class = "table table-striped">\r\n\t<thead>\r\n\t\t<tr class = "default">\r\n\r\n\t\t</tr>\r\n\t</thead>\r\n\t<tbody>\r\n\t\r\n\t\t\r\n\t<tr>\t\r\n\t\t\r\n\t\t\t<td ><img src="')
        # SOURCE LINE 21
        __M_writer(str( STATIC_URL + product.imagePath))
        __M_writer('" width=\'190\' height=\'180\'/></td>\r\n\t\t\r\n\t\t<td><p><span style="font-size:24px;">')
        # SOURCE LINE 23
        __M_writer(str(product.catalogProductID))
        __M_writer('</span></p>\r\n\t\t\t<p><span style="font-size:20px;">Item Price:<span style="color:#ff0000;">$')
        # SOURCE LINE 24
        __M_writer(str(product.price))
        __M_writer('</span></span></p>\r\n\t\t\t<p>')
        # SOURCE LINE 25
        __M_writer(str(product.description))
        __M_writer('</p>\r\n\t\t</td>\r\n\t</div>\r\n\t</tr>\r\n\t</tbody>\r\n\t</table>\r\n\t\r\n</div>\r\n<a href="/homePage/add/')
        # SOURCE LINE 33
        __M_writer(str(product.id))
        __M_writer('" id =\'add\' class="btn btn-primary btn-primary"><span class="glyphicon glyphicon-shopping-cart"></span> Add to Cart</a>\r\n\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


