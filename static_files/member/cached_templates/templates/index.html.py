# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1408847184.233439
_enable_loop = True
_template_filename = 'C:\\compfitition\\member\\templates/index.html'
_template_uri = 'index.html'
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
        weights = context.get('weights', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(' ')
        __M_writer('\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 44
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        weights = context.get('weights', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\r\n<div class="row">\r\n  <div class="col-md-3"> \r\n\t<a class=\'btn btn-primary\' href=\'/member/userGroup\'>Back to group</a>\r\n  </div>\r\n  <div class="col-md-9">\r\n    <form method="POST">\r\n      <table>\r\n        <tbody>\r\n          ')
        # SOURCE LINE 14
        __M_writer(str( form ))
        __M_writer('\r\n        </tbody>\r\n      </table>\r\n      <input class="btn btn-primary" type="submit" value="Submit" /> \r\n    </form>\r\n  </div>\r\n  <div class="col-md-12">\r\n\t<table class= "table table-striped table-hover">\r\n')
        # SOURCE LINE 22
        if weights:
            # SOURCE LINE 23
            __M_writer('\t\t\t<thead>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>Weight</th>\r\n\t\t\t\t\t<th>Date</th>\r\n\t\t\t\t</tr>\r\n\t\t\t</thead>\r\n\r\n\t\t\t<tbody>\r\n')
            # SOURCE LINE 31
            for user in weights:
                # SOURCE LINE 32
                __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 33
                __M_writer(str(user.weight))
                __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 34
                __M_writer(str(user.dateWeighed))
                __M_writer('</td>\r\n\t\t\t\t\t</tr>\r\n')
        # SOURCE LINE 38
        __M_writer('\t\t\t</tbody>\r\n\t</table>\r\n</div>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


