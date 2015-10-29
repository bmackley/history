# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394082943.04525
_enable_loop = True
_template_filename = 'C:\\myStuff\\shop\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center', 'content', 'menu', 'changeable', 'header']


# SOURCE LINE 7
from base_app import static_files 

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
        static = context.get('static', UNDEFINED)
        def menu():
            return render_menu(context._locals(__M_locals))
        def changeable():
            return render_changeable(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n')
        # SOURCE LINE 5
        __M_writer('\r\n')
        # SOURCE LINE 7
        __M_writer('\r\n')
        # SOURCE LINE 8
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    <title>My Site</title>\r\n\r\n  <script src="/static/base_app/scripts/jquery.js"></script>\r\n  <link href=\'http://fonts.googleapis.com/css?family=Rock+Salt\' rel=\'stylesheet\' type=\'text/css\'>\r\n  <link rel="stylesheet" href="/static/base_app/styles/bootstrap.css">\r\n  <link rel="stylesheet" href="/static/base_app/styles/base_template.css">\r\n')
        # SOURCE LINE 21
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  <script src="/static/base_app/scripts/bootstrap.js"></script>\r\n  <script src="/static/base_app/scripts/jquery.loadmodal.js"></script>\r\n  \r\n</head>\r\n<body>\r\n  <div class = \'header\'>\r\n    <h1>Hex Photo</h1>\r\n  </div>\r\n     \r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        # SOURCE LINE 67
        __M_writer('\r\n  </div>\r\n\r\n\r\n\r\n  <div class="row">\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        # SOURCE LINE 76
        __M_writer('\r\n  </div>\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        # SOURCE LINE 82
        __M_writer('\r\n\r\n  <div class="row">\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 86
        __M_writer('\r\n  </div>\r\n\r\n\r\n\r\n</body>\r\n</html>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def center():
            return render_center(context)
        __M_writer = context.writer()
        # SOURCE LINE 79
        __M_writer('\r\n    \r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        # SOURCE LINE 85
        __M_writer('\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        static = context.get('static', UNDEFINED)
        def menu():
            return render_menu(context)
        def changeable():
            return render_changeable(context)
        __M_writer = context.writer()
        # SOURCE LINE 33
        __M_writer('\r\n    <nav class="navbar navbar-inverse" role="navigation">\r\n      <div class="container">\r\n        <ul class="nav navbar-nav">\r\n          <li class="active"><a href="')
        # SOURCE LINE 37
        __M_writer(str(static))
        __M_writer('/homePage/catalog">Homepage</a></li>\r\n          <li><a href="#">Catalog</a></li>\r\n          <li class="dropdown">\r\n            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>\r\n            <ul class="dropdown-menu">\r\n              <li><a href="#">Action</a></li>\r\n              <li><a href="#">Another action</a></li>\r\n              <li><a href="#">Something else here</a></li>\r\n              <li class="divider"></li>\r\n              <li><a href="#">Separated link</a></li>\r\n              <li class="divider"></li>\r\n              <li><a href="#">One more separated link</a></li>\r\n            </ul>\r\n          </li>\r\n        </ul>\r\n        <form class="navbar-form navbar-left" role="search">\r\n          <div class="form-group">\r\n            <input type="text" class="form-control" placeholder="Search a product">\r\n          </div>\r\n          <button type="submit" class="btn btn-default">Submit</button>\r\n        </form>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'changeable'):
            context['self'].changeable(**pageargs)
        

        # SOURCE LINE 65
        __M_writer('\r\n      </div>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_changeable(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def changeable():
            return render_changeable(context)
        __M_writer = context.writer()
        # SOURCE LINE 58
        __M_writer('\r\n          <div class = \'navbar-right\'>\r\n          \r\n            <ul class="nav navbar-nav navbar-right">\r\n\r\n            </ul>\r\n          </div>\r\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer('\r\n    \r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


