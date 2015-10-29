# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1410670684.8486
_enable_loop = True
_template_filename = 'C:\\compFITition\\member\\templates/userGroup.html'
_template_uri = 'userGroup.html'
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
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        groups = context.get('groups', UNDEFINED)
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
        groups = context.get('groups', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\r\n<div>\r\n\t\r\n</div>\r\n\r\n<div class = 'col-md-2'>\r\n\t\r\n</div>\r\n")
        if groups:
            __M_writer('\t<div class="col-md-12">\r\n\t\t<table class= "table table-striped table-hover">\r\n\t\t\t\t<thead>\r\n\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<th>Group Name</th>\r\n\t\t\t\t\t\t<th>Group Admin</th>\r\n\t\t\t\t\t</tr>\r\n\t\t\t\t</thead>\r\n\t\t\t\t<tbody>\r\n')
            for q in groups:
                __M_writer('\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td><a href ="/member/group_members/')
                __M_writer(str(q.group.id))
                __M_writer('">')
                __M_writer(str(q.group))
                __M_writer('</a></td>\t\r\n\t\t\t\t\t\t\t<a href ="google.com"> <td>')
                __M_writer(str(q.group.administrator))
                __M_writer("</td>\t</a>\r\n\t\t\t\t\t\t\t<td><a class='btn btn-primary' href='/member/'>Make an Entry</a></td>\t\t\t\t\r\n\t\t\t\t\t\t</tr>\r\n")
            __M_writer('\t\t\t\t</tbody>\r\n\t\t</table>\r\n\t</div>\r\n')
        else:
            __M_writer('\t<div class="jumbotron"\r\n\t\t<p>\r\n\t\t\t<h2>\r\n\t\t\t\t<center>\r\n\t\t\t\t\tFitness Groups\r\n\t\t\t\t</center>\r\n\t\t\t</h2>\r\n\t\t</p>\r\n\t<p>\r\n\t\t<h3>\r\n\t\t\t<center>\r\n\t\t\t\tLooks like you have not joined any groups yet.\r\n\t\t\t\t<br>\r\n\t\t\t\tCheck out some different groups to get started.\r\n\t\t\t</center>\r\n\t\t</h3>\r\n\t</P>\r\n\t<p>\r\n\t\t<center>\r\n\t\t\t<a href="/Manager/edit_group/new">\r\n\t\t\t\tCreate Group\r\n\t\t\t</a>\r\n\t\t</center>\r\n\t</p>\r\n\t\r\n\t</div>\r\n\t<form class="navbar-form navbar-left" role="search" action="/homePage/search/">\r\n\t    <div class="form-group">\r\n\t      <input type="text" class="form-control" name = "search" placeholder="Find a group to join">\r\n\t    </div>\r\n\t    <button type="submit" class="btn btn-default">Search</button>\r\n\t</form>\r\n')
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
{"filename": "C:\\compFITition\\member\\templates/userGroup.html", "uri": "userGroup.html", "source_encoding": "ascii", "line_map": {"65": 4, "71": 7, "78": 7, "79": 15, "80": 16, "81": 25, "82": 26, "83": 27, "84": 27, "85": 27, "86": 27, "87": 28, "88": 28, "89": 32, "90": 35, "27": 0, "97": 71, "91": 36, "39": 1, "103": 71, "44": 6, "109": 103, "49": 69, "59": 4}}
__M_END_METADATA
"""
