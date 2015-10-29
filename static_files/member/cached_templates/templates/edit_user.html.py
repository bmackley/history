# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1408409048.832816
_enable_loop = True
_template_filename = 'C:\\compfitition\\member\\templates/edit_user.html'
_template_uri = 'edit_user.html'
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
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\r\n <script src="/static/member/scripts/create_user.js"></script>\r\n\t<div class="row">\r\n\t  <div class="col-md-4">\r\n\t  </div>\r\n\t  <div class="col-md-5">\r\n\t  \t<form method="POST">\r\n\t\t\t<table>\r\n\t\t\t\t<tbody>\r\n\t\t\t\t\t')
        # SOURCE LINE 12
        __M_writer(str( form ))
        __M_writer('\r\n\t\t\t\t</tbody>\r\n\t\t\t</table>\r\n\t\t\t<h3>\r\n\t\t\t\t<center>\r\n\t\t\t\t\t<span class="label label-success">\r\n\t\t\t\t\t\t<input type="submit" value="Submit" />\r\n\t\t\t\t\t</span>\r\n\t\t\t\t</center>\r\n\t\t\t</h3> \r\n\t\t\t<a href=\'/shop/update_pass/')
        # SOURCE LINE 22
        __M_writer(str(request.user.id))
        __M_writer('\'>\r\n\t\t\t\t<h3>\r\n\t\t\t\t\t<center>\r\n\t                 \t<span class="label label-primary">\r\n\t                   \t\tChange Password\r\n\t                    </span>\r\n\t                 </center>\r\n                 </h3>\r\n\t\t\t</a>\r\n\t\t\t<a href=\'/shop/delete/')
        # SOURCE LINE 31
        __M_writer(str(request.user.id))
        __M_writer('\'>\r\n\t\t\t\t<h3>\r\n\t\t\t\t\t<center>\r\n\t                 \t<span class="label label-warning">\r\n\t                   \t\tDelete Account\r\n\t                    </span>\r\n\t                </center>\r\n                </h3>\r\n\t\t\t</a>\r\n\t\t</form>\r\n\t  </div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


