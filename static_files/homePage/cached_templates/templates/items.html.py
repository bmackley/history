# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393992229.409266
_enable_loop = True
_template_filename = 'C:\\myStuff\\homePage\\templates/items.html'
_template_uri = 'items.html'
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
    return runtime._inherit_from(context, 'catalog.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        catalogProduct = context.get('catalogProduct', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 38
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        catalogProduct = context.get('catalogProduct', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\r\n<div class="col-md-11">\r\n\t<table class= "table table-striped table-hover">\r\n\t\t\t<thead>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>catalogProductID</th>\r\n\t\t\t\t\t<th>description</th>\r\n\t\t\t\t\t<th>brand</th>\r\n\t\t\t\t\t<th>category</th>\r\n\t\t\t\t\t<th>commissionRate</th>\r\n\t\t\t\t\t<th>rentalPrice</th>\r\n\t\t\t\t\t<th>replacementPrice</th>\r\n\t\t\t\t\t<th>Edit</th>\r\n\t\t\t\t</tr>\r\n\t\t\t</thead>\r\n\t\t\t<tbody>\r\n')
        # SOURCE LINE 21
        for q in catalogProduct:
            # SOURCE LINE 22
            __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 23
            __M_writer(str(q.catalogProductID))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 24
            __M_writer(str(q.description))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 25
            __M_writer(str(q.brand))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 26
            __M_writer(str(q.category))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 27
            __M_writer(str(q.commissionRate))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 28
            __M_writer(str(q.rentalPrice))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 29
            __M_writer(str(q.replacementPrice))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td><a href="/Manager/edit_catalogProduct/')
            # SOURCE LINE 30
            __M_writer(str(q.id))
            __M_writer('/">Edit</a></td>\r\n\t\t\t\t\t\t<td><a class=\'btn btn-danger\' href=\'/Manager/catalogProduct/delete/')
            # SOURCE LINE 31
            __M_writer(str(q.id))
            __M_writer("/'>delete</a></td>\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t</tr>\r\n")
        # SOURCE LINE 35
        __M_writer('\t\t\t</tbody>\r\n\t</table>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


