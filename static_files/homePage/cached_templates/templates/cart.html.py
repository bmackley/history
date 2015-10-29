# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394240051.851041
_enable_loop = True
_template_filename = 'C:\\myStuff\\homePage\\templates/cart.html'
_template_uri = 'cart.html'
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
        Objects = context.get('Objects', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        empty = context.get('empty', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        Objects = context.get('Objects', UNDEFINED)
        def content():
            return render_content(context)
        empty = context.get('empty', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\r\n<a href="/homePage/catalog/" class="btn btn-sm btn-info"><span class="glyphicon glyphicon-circle-arrow-left"></span> Back to products</a>\r\n<a href="/homePage/checkout/" class="btn btn-sm btn-success"><span class="glyphicon glyphicon-circle-arrow-right"></span> Checkout</a>\r\n<h1>Cart</h1>\r\n')
        # SOURCE LINE 8
        if empty == True:
            # SOURCE LINE 9
            __M_writer('\t\t<h3>Looks like you need to put some items in your cart</h3>\r\n')
        # SOURCE LINE 11
        for catalogProduct in Objects:
            # SOURCE LINE 12
            __M_writer('\t<div class="panel panel-default">  \r\n\t\t<table class = "table table-striped">\r\n\t\t\t<thead>\r\n\t\t\t\t<tr class = "default">\r\n\t\t\t\r\n\t\t\t</thead>\r\n\t\t\t<tbody>\r\n\r\n\t\t\t<tr class ="active">\t\t\r\n\t\t\t\t<td><a href="/manager/index"><img src="')
            # SOURCE LINE 21
            __M_writer(str( STATIC_URL ))
            __M_writer('base_app/images/canonlarge.jpg"/></a></td>\r\n\t\t\t\t<td><p><span style="font-size:24px;">')
            # SOURCE LINE 22
            __M_writer(str(catalogProduct.catalogProductID))
            __M_writer('</span></p>\r\n\t\t\t\t\t<p><span style="font-size:20px;">Item Price:<span style="color:#ff0000;">$')
            # SOURCE LINE 23
            __M_writer(str(catalogProduct.price))
            __M_writer('</span></span></p>\r\n\t\t\t\t\t<p>')
            # SOURCE LINE 24
            __M_writer(str(catalogProduct.description))
            __M_writer('</p>\r\n\t\t\t\t\t<p>Quantity: ')
            # SOURCE LINE 25
            __M_writer(str(Objects[catalogProduct]))
            __M_writer('\r\n\t\t\t\t\t<a href="/homePage/cart/remove/')
            # SOURCE LINE 26
            __M_writer(str(catalogProduct.id))
            __M_writer('" class="btn btn-primary btn-danger"><span class="glyphicon glyphicon-shopping-cart"></span> Remove Item</a>\r\n\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n\r\n\t\t\t</tbody>\r\n\t\t</table>\r\n\t</div>\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


