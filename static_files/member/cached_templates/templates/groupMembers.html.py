# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1410670688.1806
_enable_loop = True
_template_filename = 'C:\\compFITition\\member\\templates/groupMembers.html'
_template_uri = 'groupMembers.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content', 'footer']


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
        def footer():
            return render_footer(context._locals(__M_locals))
        zip = context.get('zip', UNDEFINED)
        userWeights = context.get('userWeights', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        members = context.get('members', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        userWeights = context.get('userWeights', UNDEFINED)
        zip = context.get('zip', UNDEFINED)
        members = context.get('members', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n<div class = 'col-md-5'>\r\n\t<h1>Fitness Groups</h1>\r\n</div>\r\n<div class = 'col-md-5'>\r\n</div>\r\n<div class = 'col-md-2'>\r\n\t<a class='btn btn-primary' href='/member/userGroup'>Back to group</a>\r\n</div>\r\n")
        if userWeights:
            __M_writer('\t<div class="col-md-12">\r\n\t\t<table class= "table table-striped table-hover">\r\n\t\t\t\t<thead>\r\n\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<th>Member Name</th>\r\n\t\t\t\t\t\t<th> Weight Lost</th>\r\n\t\t\t\t\t</tr>\r\n\t\t\t\t</thead>\r\n\t\t\t\t<tbody>\r\n')
            for f, q in zip(members, userWeights):
                __M_writer('\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(f))
                __M_writer('</a></td>\r\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(q))
                __M_writer('</a></td>\t\t\t\t\r\n\t\t\t\t\t\t</tr>\r\n')
            __M_writer('\t\t\t\t</tbody>\r\n\t\t</table>\r\n\t</div>\r\n')
        else:
            __M_writer('\t<h1>Looks like nobody else has joined the group yet.  Enter your friends emails to get the group started!</h1>\r\n\t<form class="navbar-form navbar-left" role="search" action="/homePage/search/">\r\n\t    <div class="form-group">\r\n\t      <input type="text" class="form-control" name = "search" placeholder="Email address">\r\n\t    </div>\r\n\t    <button type="submit" class="btn btn-default">Invite</button>\r\n\t</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\compFITition\\member\\templates/groupMembers.html", "uri": "groupMembers.html", "source_encoding": "ascii", "line_map": {"67": 4, "73": 7, "82": 7, "83": 16, "84": 17, "85": 26, "86": 27, "87": 28, "88": 28, "89": 29, "90": 29, "91": 32, "92": 35, "93": 36, "99": 46, "105": 46, "46": 6, "111": 105, "27": 0, "51": 44, "41": 1, "61": 4}}
__M_END_METADATA
"""
