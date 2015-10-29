# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1430357089.748372
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/compfitition-2.1/member/templates/groupMembers.html'
_template_uri = 'groupMembers.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'footer', 'header']


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
        zip = context.get('zip', UNDEFINED)
        members = context.get('members', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        userWeights = context.get('userWeights', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        zip = context.get('zip', UNDEFINED)
        members = context.get('members', UNDEFINED)
        userWeights = context.get('userWeights', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("\n<div class = 'col-md-5'>\n\t<h1>Fitness Groups</h1>\n</div>\n<div class = 'col-md-5'>\n</div>\n<div class = 'col-md-2'>\n\t<a class='btn btn-primary' href='/member/userGroup'>Back to group</a>\n</div>\n")
        if userWeights:
            __M_writer('\t<div class="col-md-12">\n\t\t<table class= "table table-striped table-hover">\n\t\t\t\t<thead>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<th>Member Name</th>\n\t\t\t\t\t\t<th> Weight Lost</th>\n\t\t\t\t\t</tr>\n\t\t\t\t</thead>\n\t\t\t\t<tbody>\n')
            for f, q in zip(members, userWeights):
                __M_writer('\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(f))
                __M_writer('</a></td>\n\t\t\t\t\t\t\t<td>')
                __M_writer(str(q))
                __M_writer('</a></td>\t\t\t\t\n\t\t\t\t\t\t</tr>\n')
            __M_writer('\t\t\t\t</tbody>\n\t\t</table>\n\t</div>\n')
        else:
            __M_writer('\t<h1>Looks like nobody else has joined the group yet.  Enter your friends emails to get the group started!</h1>\n\t<form class="navbar-form navbar-left" role="search" action="/homePage/search/">\n\t    <div class="form-group">\n\t      <input type="text" class="form-control" name = "search" placeholder="Email address">\n\t    </div>\n\t    <button type="submit" class="btn btn-default">Invite</button>\n\t</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "groupMembers.html", "source_encoding": "ascii", "filename": "/Users/benmackley/Projects/compfitition-2.1/member/templates/groupMembers.html", "line_map": {"70": 7, "71": 16, "72": 17, "73": 26, "74": 27, "75": 28, "76": 28, "77": 29, "78": 29, "79": 32, "80": 35, "81": 36, "87": 46, "27": 0, "93": 46, "99": 4, "41": 1, "46": 6, "111": 105, "51": 44, "105": 4, "61": 7}}
__M_END_METADATA
"""
