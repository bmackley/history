# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1430362907.869479
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/compfitition-2.1/member/templates/create_user.html'
_template_uri = 'create_user.html'
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n<script src="js/bootstrap-datepicker.js"></script>\n<script src="/static/member/scripts/create_user.js"></script>\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n<!--\n\t\t\t\t\t\t<!--\t\t\n\t\t\t\t\t\t\t<form class="white-row" method="post" action="#">\n\n\t\t\t\t\t\t\t\t<!-- alert failed -->\n\t\t\t\t\t\t\t\t<div class="alert alert-danger">\n\t\t\t\t\t\t\t\t\t<i class="fa fa-frown-o"></i> \n\t\t\t\t\t\t\t\t\t<strong>Password</strong> do not match!\n\t\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t\t<div class="row">\n\t\t\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t\t\t<div class="col-md-12">\n\t\t\t\t\t\t\t\t\t\t\t<label>E-mail Address</label>\n\t\t\t\t\t\t\t\t\t\t\t<input type="text" value="" class="form-control">\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class="row">\n\t\t\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t\t\t<div class="col-md-6">\n\t\t\t\t\t\t\t\t\t\t\t<label>Password</label>\n\t\t\t\t\t\t\t\t\t\t\t<input type="password" value="" class="form-control">\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="col-md-6">\n\t\t\t\t\t\t\t\t\t\t\t<label>Re-enter Password</label>\n\t\t\t\t\t\t\t\t\t\t\t<input type="password" value="" class="form-control">\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t-->\n-->')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\t\t<div id="wrapper">\n\n\t\t\t<div id="shop">\n\n\t\t\t\t<!-- PAGE TITLE -->\n\t\t\t\t<header id="page-title">\n\t\t\t\t\t<div class="container">\n\t\t\t\t\t\t<h1>Sign Up</h1>\n\n\t\t\t\t\t\t<ul class="breadcrumb">\n\t\t\t\t\t\t\t<li><a href="http://localhost:8000/">Home</a></li>\n\t\t\t\t\t\t\t<li class="active">Sign Up</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</div>\n\t\t\t\t</header>\n\n\n\t\t\t\t<section class="container">\n\n\t\t\t\t\t<div class="row">\n\n\t\t\t\t\t\t<!-- REGISTER -->\n\t\t\t\t\t\t<div class="col-md-6">\n\n\t\t\t\t\t\t\t<h2>Create A <strong>Personal Account</strong></h2>\n\t\t\t\t\t\t\t<form method="POST">\n\t\t\t\t\t\t\t\t')
        __M_writer(str( form ))
        __M_writer('\n\t\n\t\t\t\t\t\t\t\t<div class="row">\n\t\t\t\t\t\t\t\t<br>\n\t\t\t\t\t\t\t\t\t<div class="col-md-8">\n\t\t\t\t\t\t\t\t\t\t<input type="submit" value="Sign Up" class="btn btn-primary pull-right push-bottom" data-loading-text="Loading...">\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t</form>\n\t\t\t\t\t\t\t<p><center>\n\t\t\t\t\t\t\t\t<h3>\n\t\t\t\t\t\t\t\t\tAlready have an account?\n\t\t\t\t\t\t\t\t\t<a href="page-signin.html">Click to Sign In</a>\n\t\t\t\t\t\t\t\t</h3></center>\n\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<!-- /REGISTER -->\n\n\t\t\t\t\t\t<!-- WHY? -->\n\t\t\t\t\t\t<div class="col-md-6">\n\n\t\t\t\t\t\t\t<h2>Why Compete?</h2>\n\n\t\t\t\t\t\t\t<div class="white-row">\n\n\t\t\t\t\t\t\t\t<h4>Why create a CompFITition account?</h4>\n\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t<ul class="list-icon check">\n\t\t\t\t\t\t\t\t\t<li>Easy tracking of your progress</li>\n\t\t\t\t\t\t\t\t\t<li>Get updates of your competitors progress</li>\n\t\t\t\t\t\t\t\t\t<li>Trash talk the competition</li>\n\t\t\t\t\t\t\t\t\t<li>Receive nutrition and fitness tips</li>\n\t\t\t\t\t\t\t\t\t<li>Join as many competition groups as you want</li>\n\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t<p>All we ask is that you put in the work...we will do the rest.</p>\n\n\t\t\t\t\t\t\t\t<hr class="half-margins" />\n\n\t\t\t\t\t\t\t\t<!--<p>\n\t\t\t\t\t\t\t\t\tAlready have an account?\n\t\t\t\t\t\t\t\t\t<a href="page-signin.html">Click to Sign In</a>\n\t\t\t\t\t\t\t\t</p>-->\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="white-row">\n\t\t\t\t\t\t\t\t<h4>Contact Customer Support</h4>\n\t\t\t\t\t\t\t\t<p>\n\t\t\t\t\t\t\t\t\tIf you are looking for more help or have a question to ask, please <a href="contact-us.html">contact us</a>.\n\t\t\t\t\t\t\t\t</p>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<!-- /WHY? -->\n\n\t\t\t\t\t</div>\n\n\t\t\t\t</section>\n\n\t\t\t</div>\n\t\t</div>\n\t\t<!-- /WRAPPER -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/benmackley/Projects/compfitition-2.1/member/templates/create_user.html", "line_map": {"35": 2, "53": 7, "54": 34, "55": 34, "40": 97, "27": 0, "61": 55, "46": 7}, "uri": "create_user.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
