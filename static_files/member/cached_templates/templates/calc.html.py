# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1392323422.647555
_enable_loop = True
_template_filename = 'C:\\myStuff\\calculator\\templates/calc.html'
_template_uri = 'calc.html'
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
        calc = context.get('calc', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        len = context.get('len', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 42
        __M_writer('  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        calc = context.get('calc', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        len = context.get('len', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer('\n\n  <!-- URL parameters -->\n  <h2>URL Parameters:</h2>\n  \n  </p>\n  \n')
        # SOURCE LINE 11
        if len(request.urlparams) > 0:
            # SOURCE LINE 12
            __M_writer('    <p>The url parameters sent in were:</p>\n')
            # SOURCE LINE 13
            for i, param in enumerate(request.urlparams):
                # SOURCE LINE 14
                __M_writer('      <div>')
                __M_writer(str( i ))
                __M_writer(': ')
                __M_writer(str( param ))
                __M_writer('</div>\n')
            # SOURCE LINE 16
        else:
            # SOURCE LINE 17
            __M_writer('    <p>There were no url parameters.  Try submitting the form and then looking at the url above.</p>\n')
        # SOURCE LINE 19
        __M_writer('  \n  <!-- Example use of static url for graphics, css files, scripts, etc. -->\n  <img style="float: right;" src="')
        # SOURCE LINE 21
        __M_writer(str( STATIC_URL ))
        __M_writer('calculator/images/calculator-icon.png"/>\n  <!-- Calculator -->\n  <h2>Calculator Example:</h2>\n')
        # SOURCE LINE 24
        if calc:
            # SOURCE LINE 25
            __M_writer('    <p>The last calculation was: ')
            __M_writer(str( calc ))
            __M_writer('</p>\n')
        # SOURCE LINE 27
        __M_writer('  \n  <p>New calculation:</p>\n  <form action="/calculator/calc/A/B/C/" method="post">\n  ')
        # SOURCE LINE 30
        __M_writer(str( form.as_p() ))
        __M_writer('\n  <input type="submit" value="Submit"/>\n  </form>\n  \n  \n  <!-- Ajax buttons -->\n  <h2>Ajax Example:</h2>\n  <p id="calculator-log">Log not loaded yet.</p>\n  <button id="load-calculator-log">(Re)Load Log</button>\n  <button id="delete-calculator-log">Delete Log</button>\n\n  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


