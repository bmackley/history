# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1441924420.4608
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/AssyrianProject2/homePage/templates/index.htm'
_template_uri = 'index.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html> \n<html> \n<head>\n  <title>jQuery Image Scroller Plugin</title>\n  <meta charset="utf-8" />\n  <link href="stylesheets/screen.css" type="text/css" rel="stylesheet" media="screen,projection" />\n</head>\n<body>\n  <div id="container">\n    <div class="image-scroller">\n      <img src="../images/Tablet1.png" alt="" class="feature-image" height="1800" width="960" />\n      <div class="preview">\n        <img src="images/preview.jpg" alt="" height="180" width="135" />\n      </div>\n    </div>\n  </div>\n  \n  <script type="text/javascript" src="scripts/jquery.js"></script>\n  <script type="text/javascript" src="scripts/jquery.imageScroller.min.js"></script>\n  <script type="text/javascript">\n    $(document).ready(function() {\n      $(\'div.image-scroller\').imageScroller();\n    });\n  </script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/benmackley/Projects/AssyrianProject2/homePage/templates/index.htm", "line_map": {"16": 0, "27": 21, "21": 1}, "source_encoding": "ascii", "uri": "index.htm"}
__M_END_METADATA
"""
