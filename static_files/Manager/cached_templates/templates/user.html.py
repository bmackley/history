# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393994050.120405
_enable_loop = True
_template_filename = 'C:\\myStuff\\Manager\\templates/user.html'
_template_uri = 'user.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer', 'content', 'header']


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
        def footer():
            return render_footer(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 6
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 61
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        # SOURCE LINE 65
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
        # SOURCE LINE 63
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer('\r\n<div class = \'col-md-5\'>\r\n\t\t<h1>Users</h1>\r\n</div>\r\n<div class = \'col-md-6\'>\r\n\t<a class="btn btn-success" href=\'/Manager/user\'>Active Users</button>\r\n\t<a class=\'btn btn-danger\' href=\'/Manager/user/all\'>All Users</a>\r\n</div>\r\n<div class = \'col-md-1\'>\r\n\t<a class=\'btn btn-info\' href=\'/Manager/edit_user/new\'>New User</a>\r\n</div>\r\n\r\n<div class="col-md-12">\r\n\t<table class= "table table-striped table-hover">\r\n\t\t\t<thead>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>Staff</th>\r\n\t\t\t\t\t<th>Super User</th>\r\n\t\t\t\t\t<th>First Name</th>\r\n\t\t\t\t\t<th>Last Name</th>\r\n\t\t\t\t\t<th>username</th>\r\n\t\t\t\t\t<th>email</th>\r\n\t\t\t\t\t<th>address</th>\r\n\t\t\t\t\t<th>City</th>\r\n\t\t\t\t\t<th>State</th>\r\n\t\t\t\t\t<th>Zip Code</th>\r\n\t\t\t\t\t<th>Phone</th>\r\n')
        # SOURCE LINE 34
        if request.user.is_superuser == True:
            # SOURCE LINE 35
            __M_writer('\t\t\t\t\t<th>Edit</th>\r\n\t\t\t\t\t<th>Delete</th>\r\n')
        # SOURCE LINE 38
        __M_writer('\t\t\t\t</tr>\r\n\t\t\t</thead>\r\n\t\t\t<tbody>\r\n')
        # SOURCE LINE 41
        for q in user:
            # SOURCE LINE 42
            __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 43
            __M_writer(str(q.is_staff))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 44
            __M_writer(str(q.is_superuser))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 45
            __M_writer(str(q.first_name))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 46
            __M_writer(str(q.last_name))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 47
            __M_writer(str(q.username))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 48
            __M_writer(str(q.email))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 49
            __M_writer(str(q.address))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 50
            __M_writer(str(q.city))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 51
            __M_writer(str(q.state))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 52
            __M_writer(str(q.zipcode))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
            # SOURCE LINE 53
            __M_writer(str(q.phone))
            __M_writer('</td>\r\n\t\t\t\t\t\t<td><a href="/Manager/edit_user/')
            # SOURCE LINE 54
            __M_writer(str(q.id))
            __M_writer('/">Edit</a></td>\r\n\t\t\t\t\t\t<td><a class=\'btn btn-danger\' href=\'/Manager/user/delete/')
            # SOURCE LINE 55
            __M_writer(str(q.id))
            __M_writer("/'>delete</a></td>\t\r\n\t\t\t\t\t</tr>\r\n")
        # SOURCE LINE 58
        __M_writer('\t\t\t</tbody>\r\n\t</table>\r\n</div>\r\n')
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
        __M_writer('\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


