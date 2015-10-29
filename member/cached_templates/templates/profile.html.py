# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1430447375.140678
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/compfitition-2.1/member/templates/profile.html'
_template_uri = 'profile.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'footer', 'content']


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
        def footer():
            return render_footer(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        runs = context.get('runs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        runs = context.get('runs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!-- WRAPPER -->\n\t\t<div id="wrapper">\n\n\t\t\t<!-- PAGE TITLE -->\n\t\t\t<header id="page-title"> <!-- style="background-image:url(\'../assets/images/demo/parallax_bg.jpg\')" -->\n\t\t\t\t<!--\n\t\t\t\t\tEnable only if bright background image used\n\t\t\t\t\t<span class="overlay"></span>\n\t\t\t\t-->\n\n\t\t\t\t<div class="container">\n\t\t\t\t\t<h1>Profile</h1>\n\n\t\t\t\t\t<ul class="breadcrumb">\n\t\t\t\t\t\t<li><a href="http://localhost:8000/">Home</a></li>\n\t\t\t\t\t\t<li class="active">Profile</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t</header>\n\n\n\t\t\t<section class="container">\n\n\t\t\t\t<div class="row">\n\n\t\t\t\t\t<aside class="col-md-3">\n\n\t\t\t\t\t\t<ul class="nav nav-list">\n\t\t\t\t\t\t\t<li><a href="shortcodes-rows.html"><i class="fa fa-circle-o"></i> Groups</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-counters.html"><i class="fa fa-circle-o"></i> Create Group</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-toggles.html"><i class="fa fa-circle-o"></i> Find Group</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-forms.html"><i class="fa fa-circle-o"></i> Edit Profile</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-editor.html"><i class="fa fa-circle-o"></i><span class="label label-warning pull-right">New</span> Your History</a></li>\n\t\t\t\t\t\t\t<!--<li><a href="shortcodes-buttons.html"><i class="fa fa-circle-o"></i> Buttons</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-tabs-and-accordions.html"><i class="fa fa-circle-o"></i> Tabs &amp; Accordions</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-callouts.html"><i class="fa fa-circle-o"></i> Callouts</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-dividers.html"><i class="fa fa-circle-o"></i> Dividers</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-lightbox.html"><i class="fa fa-circle-o"></i> Lightbox</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-icons-and-boxes.html"><i class="fa fa-circle-o"></i> Icons &amp; Boxes</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-carousel.html"><i class="fa fa-circle-o"></i> Carousel</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-progress-bars.html"><i class="fa fa-circle-o"></i> Progress Bars</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-alerts.html"><i class="fa fa-circle-o"></i> Alerts</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-video.html"><i class="fa fa-circle-o"></i> Video</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-tooltips-and-popover.html"><i class="fa fa-circle-o"></i> Tooltips &amp; Popover</a></li>\n\t\t\t\t\t\t\t<li><a href="shortcodes-modals.html"><i class="fa fa-circle-o"></i> Modals</a></li>\n\t\t\t\t\t\t\t-->\n\t\t\t\t\t\t</ul>\n\n\t\t\t\t\t</aside>\n\n\t\t\t\t\t<div class="col-md-9">\n\n\t\t\t\t\t\t<h2><strong>')
        __M_writer(str(request.user))
        __M_writer('&#39;s</strong> <small class="font300">Profile</small></h2>\n\n\t\t\t\t\t\t<!-- WHITE ROWS -->\n\t\t\t\t\t\t<div class="white-row">\n\t\t\t\t\t\t\t<h3><strong>Goals</h3>\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t<!--Counters-->\n\t\t\t\t\t\t\t<section class="paddings white-row">\n\t\t\t\t\t\t\t\t<div class="row text-center countTo">\n\t\t\t\t\t\t\t\t\t<div class="col-md-4">\n')
        if runs != 'False':
            for i in runs:
                __M_writer('\t\t\t\t\t\t\t\t\t\t\t<strong data-to=')
                __M_writer(str(i.totalDistance))
                __M_writer('></strong>\n')
        else:
            __M_writer('\t\t\t\t\t\t\t\t\t\t<strong data-to="0">0</strong>\n')
        __M_writer('\t\t\t\t\t\t\t\t\t\t<label>Miles Run</label>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t\t\t\t\t\t<strong data-to="67">0</strong>\n\t\t\t\t\t\t\t\t\t\t<label>lbs Lost</label>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t\t\t\t\t\t<strong data-to="32">0</strong>\n\t\t\t\t\t\t\t\t\t\t<label>Groups</label>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</section>\n\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t<div class="row">\n\n\t\t\t\t\t\t\t<div class="col-md-6">\n\t\t\t\t\t\t\t\t<div class="white-row">\n\t\t\t\t\t\t\t\t\t<h2><strong>Progress</h2>\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t<!--Progress Bars-->\n\t\t\t\t\t\t\t\t\t\t<div class="progress-bars">\n\t\t\t\t\t\t\t\t\t\t<div class="progress-label">\n\t\t\t\t\t\t\t\t\t\t\t<span>Muscle Gain</span>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="progress progress-striped">\n\t\t\t\t\t\t\t\t\t\t\t<div class="progress-bar progress-bar-primary" data-appear-progress-animation="100%">\n\t\t\t\t\t\t\t\t\t\t\t\t<span class="progress-bar-tooltip">100%</span>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="progress-label">\n\t\t\t\t\t\t\t\t\t\t\t<span>Weight Loss</span>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="progress progress-striped">\n\t\t\t\t\t\t\t\t\t\t\t<div class="progress-bar progress-bar-warning" data-appear-progress-animation="75%" data-appear-animation-delay="300">\n\t\t\t\t\t\t\t\t\t\t\t\t<span class="progress-bar-tooltip">86%</span>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="progress-label">\n\t\t\t\t\t\t\t\t\t\t\t<span>Bench Press</span>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="progress progress-striped">\n\t\t\t\t\t\t\t\t\t\t\t<div class="progress-bar progress-bar-danger" data-appear-progress-animation="0%" data-appear-animation-delay="600">\n\t\t\t\t\t\t\t\t\t\t\t\t<span class="progress-bar-tooltip">69%</span>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="progress-label">\n\t\t\t\t\t\t\t\t\t\t\t<span>Group: Rick Grimes</span>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t<div class="progress progress-striped">\n\t\t\t\t\t\t\t\t\t\t\t<div class="progress-bar progress-bar-info" data-appear-progress-animation="0%" data-appear-animation-delay="900">\n\t\t\t\t\t\t\t\t\t\t\t\t<span class="progress-bar-tooltip">96%</span>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="col-md-6">\n\t\t\t\t\t\t\t\t<div class="white-row">\n\t\t\t\t\t\t\t\t\t<h2><strong>')
        __M_writer(str(request.user))
        __M_writer('&#39;s</strong> Info</h2>\n\t\t\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t<div class="row">\n\n\t\t\t\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t\t\t\t<div class="white-row">\n\t\t\t\t\t\t\t\t\t<h2><strong>White</strong> Row</h2>\n\t\t\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t\t\t\t<div class="white-row">\n\t\t\t\t\t\t\t\t\t<h2><strong>White</strong> Row</h2>\n\t\t\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="col-md-4">\n\t\t\t\t\t\t\t\t<div class="white-row">\n\t\t\t\t\t\t\t\t\t<h2><strong>White</strong> Row</h2>\n\t\t\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t<div class="row">\n\n\t\t\t\t\t\t\t<div class="col-md-3">\n\t\t\t\t\t\t\t\t<div class="white-row">\n\t\t\t\t\t\t\t\t\t<h2><strong>White</strong> Row</h2>\n\t\t\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="col-md-3">\n\t\t\t\t\t\t\t\t<div class="white-row">\n\t\t\t\t\t\t\t\t\t<h2><strong>White</strong> Row</h2>\n\t\t\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="col-md-3">\n\t\t\t\t\t\t\t\t<div class="white-row">\n\t\t\t\t\t\t\t\t\t<h2><strong>White</strong> Row</h2>\n\t\t\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t\t<div class="col-md-3">\n\t\t\t\t\t\t\t\t<div class="white-row">\n\t\t\t\t\t\t\t\t\t<h2><strong>White</strong> Row</h2>\n\t\t\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t</div>\n\n\t\t\t\t\t\t<!-- /WHITE ROWS -->\n\n\n\t\t\t\t\t\t<h3>Color Rows</h3>\n\t\t\t\t\t\t<div class="white-row styleBackground">\n\t\t\t\t\t\t\t<h3><strong>Style Background</strong> Row</h3>\n\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t</div>\n\n\n\t\t\t\t\t\t<div class="white-row styleSecondBackground">\n\t\t\t\t\t\t\t<h3><strong>Style Second Background</strong> Row</h3>\n\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>\n\t\t\t\t\t\t</div>\n\n\t\t\t\t\t</div>\n\n\t\t\t\t</div>\n\n\n\t\t\t</section>\n\n\n\t\t</div>\n\t\t<!-- /WRAPPER -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "profile.html", "filename": "/Users/benmackley/Projects/compfitition-2.1/member/templates/profile.html", "line_map": {"66": 3, "72": 229, "78": 229, "84": 6, "27": 0, "92": 6, "93": 59, "94": 59, "95": 69, "96": 70, "97": 71, "98": 71, "99": 71, "100": 73, "101": 74, "102": 76, "103": 136, "40": 1, "45": 5, "110": 104, "104": 136, "50": 227, "60": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
