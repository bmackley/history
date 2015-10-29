# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440697818.597817
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/AssyrianProject2/homePage/templates/about.html'
_template_uri = 'about.html'
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
        __M_writer('<!DOCTYPE html>\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="section no-pad-bot" id="index-banner">\n    <div class="container">\n      <br><br>\n      <h1 class="header center amber-text">Assyrian Project</h1>\n      <div class="row center">\n        <h5 class="header col s12 light">The Assyrian Project was formed to index over 10,000 ancient Assyrian tablets.  Cuneiform tablets were written using clay and a stylus.  Although not as efficient as modern day tablets, the documents preserved extremely well and contained important data - mostly business information from transactions between wealthy mercants. Tablets were hard to make, and so the whole tablet was utilized for writing - even the sides! </h5>\n      </div>\n      <div class="row center">\n        <a class="btn-large waves-effect waves-light amber modal-trigger" href="#modal2" >Get Started</a>\n      </div>\n      <br><br>\n    </div>\n  </div>\n\n  <div class="container">\n    <div class="section">\n\n      <!--   Icon Section   -->\n      <div class="row">\n        <div class="col s12 m4">\n          <div class="icon-block">\n            <h2 class="center light-blue-text"><i class="large material-icons">broken_image</i></h2>\n            <h5 class="center">Seperate image based on lines</h5>\n\n            <p class="light">The first step to indexing the tablets is to seperate the images into lines.  Much like regular lined paper, Assyrians divided their tablets into lines to segement their writing.  Knowing which characters are in which line helps with indexing processes so that the text can be transliterated into a readable form.  </p>\n          </div>\n        </div>\n\n        <div class="col s12 m4">\n          <div class="icon-block">\n            <h2 class="center light-blue-text"><i class="large material-icons">crop</i></h2>\n            <h5 class="center">Crop Characters</h5>\n\n            <p class="light">Identifying hotspots is the first step for understanding these ancient documents.  Writing with a stylus on clay is much like handwriting - each person has their unique way of forming the characters, and because the characters are not uniform, a computer has a difficulty trying to determine which character is which character.  That is where human intervention is so helpful. </p>\n          </div>\n        </div>\n\n        <div class="col s12 m4">\n          <div class="icon-block">\n            <h2 class="center light-blue-text"><i class="large material-icons">select_all</i></h2>\n            <h5 class="center">Match the Character with its symbol</h5>\n\n            <p class="light">With each character identified, it has to be linked to its symbol in the Assyrian alphabet.  Since the number of people that can read Assyrian in the world is limited to a handful of people, we simplified the transliteration.  Identifying the characters is as simple as a matching game!</p>\n          </div>\n        </div>\n      </div>\n\n    </div>\n    <br><br>\n\n    <div class="section">\n\n    </div>\n  </div>\n\n  <footer class="page-footer orange">\n    <div class="container">\n      <div class="row">\n        <div class="col l6 s12">\n          <h5 class="white-text">Copywrite 2015 by Edward Stratford and Benjamin Mackley</h5>\n          <p class="grey-text text-lighten-4">Images used curteousy of EDLF.</p>\n\n\n        </div>\n        <div class="col l3 s12">\n          <h5 class="white-text">Settings</h5>\n          <ul>\n            <li><a class="white-text" href="#!">Link 1</a></li>\n          </ul>\n        </div>\n        <div class="col l3 s12">\n          <h5 class="white-text">Connect</h5>\n          <ul>\n            <li><a class="white-text" href="#!">Link 1</a></li>\n          </ul>\n        </div>\n      </div>\n    </div>\n    <div class="footer-copyright">\n      <div class="container">\n      Made by <a class="orange-text text-lighten-3" href="http://materializecss.com">Materialize</a>\n      </div>\n    </div>\n  </footer>\n\n\n  <!--  Scripts-->\n  <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>\n  <script src="../../bin/materialize.js"></script>\n  <script src="js/init.js"></script>\n\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/benmackley/Projects/AssyrianProject2/homePage/templates/about.html", "line_map": {"34": 1, "35": 2, "52": 3, "40": 97, "58": 52, "27": 0, "46": 3}, "source_encoding": "ascii", "uri": "about.html"}
__M_END_METADATA
"""
