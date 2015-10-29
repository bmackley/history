# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1441946192.712916
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/AssyrianProject2/homePage/templates/hotspots2.html'
_template_uri = 'hotspots2.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(' <html>\n <head>\n  <title>jQuery Image Scroller Plugin</title>\n  <meta charset="utf-8" />\n  <link href="/static/homepage/css/screen.css" type="text/css" rel="stylesheet" media="screen,projection" />\n</head>\n<body>\n  <div id="container">\n  <div class="image-scroller">\n     <div id="hb-map-wrap">\n         <img id =\'Tablet\' src ="/static/homepage/images/Tablet1.png" class="feature-image" height="1280" width="960" />\n      </div>\n    <div class="preview">\n      <img src ="/static/homepage/images/Tablet1.png" height="180" width="135" />\n      <!--<img src="images/preview.jpg" alt="" height="180" width="135" />-->\n    </div>\n  </div>\n</div>\n  this is text\n  <script src="/static/homepage/js/lib/jquery.min.js"></script>\n  <script type="text/javascript" src="/static/homepage/js/jquery.imageScroller.js"></script>\n  <script type="text/javascript">\n    $(document).ready(function() {\n      $(\'div.image-scroller\').imageScroller();\n    });\n  </script>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/benmackley/Projects/AssyrianProject2/homePage/templates/hotspots2.html", "line_map": {"16": 0, "27": 21, "21": 1}, "source_encoding": "ascii", "uri": "hotspots2.html"}
__M_END_METADATA
"""
