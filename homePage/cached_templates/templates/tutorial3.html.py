# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1446850962.990785
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/history/homePage/templates/tutorial3.html'
_template_uri = 'tutorial3.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(' ')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<center><h1>How to Identify Hotspots</h1>\n   <div class = "row">\n\n<!-- Update the path to raphael js -->\n\n\n<style type=\'text/css\'>\nsvg {\n    border: solid 1px #000;\n}\n</style>\n\n<div >\n\n\n</div>\n\n\n\n\n\n\n\n  <!-- Block to Show Animation -->\n    <div class="col s12 m12 l12" >\n      <div id="raphael">\n        <div class="card large">\n            <div class="card-image">\n              <img id = "animate_img" src ="/static/homePage/images/Line.jpeg" > \n            </div>\n            <div class="card-content">\n              The most important part is creating the hotspots for each character. \n            </div>\n            <div class="card-action">\n               <a class="animate waves-effect waves-teal btn-flat">Animate</a>\n            </div>\n        </div>\n        <div id="raphaelContainer">\n        </div>\n      </div>\n    </div>\n \n\n<div id="modal_continue" class="modal">\n    <div class="modal-content">\n      <p>Congratulations! Now that you have the basic concept down, we are going to take it up a notch.  </p>\n    </div>\n    <div class="modal-footer">\n      <a href="#!" class=" modal-action modal-close waves-effect waves-green btn-flat">Let&#8217;s Go!</a>\n    </div>\n  </div>\n\n\n\n<script type="text/javascript"src="https://cdnjs.cloudflare.com/ajax/libs/raphael/1.5.2/raphael-min.js"></script>\n<script type=\'text/javascript\'\n    src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>\n<script src="/static/homePage/js/tutorial3.js"></script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "36": 1, "52": 2, "58": 52, "28": 0, "46": 2}, "filename": "/Users/benmackley/Projects/history/homePage/templates/tutorial3.html", "source_encoding": "ascii", "uri": "tutorial3.html"}
__M_END_METADATA
"""
