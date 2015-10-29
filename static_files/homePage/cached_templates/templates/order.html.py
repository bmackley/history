# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394327481.275648
_enable_loop = True
_template_filename = 'C:\\myStuff\\homePage\\templates/order.html'
_template_uri = 'order.html'
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
        EndDate = context.get('EndDate', UNDEFINED)
        needOption = context.get('needOption', UNDEFINED)
        useroption = context.get('useroption', UNDEFINED)
        usershipping = context.get('usershipping', UNDEFINED)
        totalcharged = context.get('totalcharged', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        needBilling = context.get('needBilling', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        userbilling = context.get('userbilling', UNDEFINED)
        Objects = context.get('Objects', UNDEFINED)
        needShipping = context.get('needShipping', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        EndDate = context.get('EndDate', UNDEFINED)
        needOption = context.get('needOption', UNDEFINED)
        useroption = context.get('useroption', UNDEFINED)
        usershipping = context.get('usershipping', UNDEFINED)
        totalcharged = context.get('totalcharged', UNDEFINED)
        def content():
            return render_content(context)
        needBilling = context.get('needBilling', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        userbilling = context.get('userbilling', UNDEFINED)
        Objects = context.get('Objects', UNDEFINED)
        needShipping = context.get('needShipping', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer('\r\n<br>\r\n<h3>Your Ordered Items</h3>\r\n')
        # SOURCE LINE 8
        for product in Objects:
            # SOURCE LINE 9
            __M_writer('<div class="panel panel-default">  \r\n<table class = "table table-striped">\r\n\t<thead>\r\n\t\t<tr class = "default">\r\n\t\t\t\r\n\t\t\t<th></th>\r\n\t\t\t<th></th>\r\n\t\t\t\r\n\t\t\t<th></th>\r\n\t\t\t\r\n\t\t</tr>\r\n\t</thead>\r\n\t<tbody>\r\n\t\t\r\n\t<tr class ="active">\t\t\r\n\t\t<td><a href="/manager/index"><img src="')
            # SOURCE LINE 24
            __M_writer(str( STATIC_URL ))
            __M_writer(str(product.imagePath))
            __M_writer('" width="190" height="180"/></a></td>\r\n\t\t<td><p><span style="font-size:24px;">')
            # SOURCE LINE 25
            __M_writer(str(product.catalogProductID))
            __M_writer('</span></p>\r\n\t\t\t<p><span style="font-size:20px;">Item Price:<span style="color:#ff0000;">$')
            # SOURCE LINE 26
            __M_writer(str(product.price))
            __M_writer('</span></span></p>\r\n\t\t\t<p>')
            # SOURCE LINE 27
            __M_writer(str(product.description))
            __M_writer('</p>\r\n\t\t\t<p>Quantity: ')
            # SOURCE LINE 28
            __M_writer(str(Objects[product]))
            __M_writer('\r\n\t\t\t\t\t\t\t</td>\r\n\t</tr>\r\n\r\n\t</tbody>\r\n\t</table>\r\n\r\n</div>\t\r\n')
        # SOURCE LINE 37
        __M_writer('\r\n\r\n<br>\r\n')
        # SOURCE LINE 40
        if needBilling == True:
            # SOURCE LINE 41
            __M_writer('<span style="color:#ff0000;">You must choose a valid billing option</span>\r\n')
        # SOURCE LINE 43
        __M_writer('<h3>Your Billing Option</h3>\r\n\t<table class = "table table-striped table-hover">\r\n\t\t<thead>\r\n\t\t\t<tr class="success">\r\n\t\t\t\t\t<th>Name on Card</th>\r\n\t\t\t\t\t<th>Description</th>\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\r\n\t\t\t\t<tr class="active">\r\n\t\t\t\t\t<td>')
        # SOURCE LINE 54
        __M_writer(str(userbilling.name))
        __M_writer('</td>\r\n\t\t\t\t\t<td>')
        # SOURCE LINE 55
        __M_writer(str(userbilling.cardtype.name))
        __M_writer(' ending in ')
        __M_writer(str(userbilling.number[-4:]))
        __M_writer('</td>\r\n\t\t\t\t</tr>\r\n\t\t</tbody>\r\n\t</table>\r\n\r\n<br>\r\n<br>\r\n')
        # SOURCE LINE 62
        if needShipping == True:
            # SOURCE LINE 63
            __M_writer('<span style="color:#ff0000;">You must choose a valid shipping option</span>\r\n')
        # SOURCE LINE 65
        __M_writer('<h3>Your Shipping Information</h3>\r\n\t<table class = "table table-striped table-hover">\r\n\t\t<thead>\r\n\t\t\t<tr class="success">\r\n')
        # SOURCE LINE 69
        for value in usershipping.customer():
            # SOURCE LINE 70
            __M_writer('\t\t\t\t\t<th>')
            __M_writer(str(value.key))
            __M_writer('</th>\r\n')
        # SOURCE LINE 72
        __M_writer('\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\t\t\t\t<tr class="active">\r\n')
        # SOURCE LINE 76
        for value in usershipping.customer():
            # SOURCE LINE 77
            __M_writer('\t\t\t\t\t\t<td>')
            __M_writer(str(value.value))
            __M_writer('</td>\r\n')
        # SOURCE LINE 79
        __M_writer('\t\t\t\t</tr>\r\n\t\t</tbody>\r\n\t</table>\r\n<br>\r\n<br>\r\n<p></p>\r\n')
        # SOURCE LINE 85
        if needOption == True:
            # SOURCE LINE 86
            __M_writer('<span style="color:#ff0000;">You must choose a valid shipping option</span>\r\n')
        # SOURCE LINE 88
        __M_writer('<h3>Your Delivery Option</h3>\r\n\t<table class = "table table-striped table-hover">\r\n\t\t<thead>\r\n\t\t\t<tr class="success">\r\n\t\t\t\t\t<th>Option</th>\r\n\t\t\t\t\t<th>Price</th>\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\r\n\t\t\t\t<tr class="active">\r\n\t\t\t\t\t<td>')
        # SOURCE LINE 99
        __M_writer(str(useroption.daystoarrive))
        __M_writer('-Day Shipping</td>\r\n\t\t\t\t\r\n')
        # SOURCE LINE 101
        if useroption.price == 0:
            # SOURCE LINE 102
            __M_writer('\t\t\t\t\t<td>Free!</td>\r\n')
            # SOURCE LINE 103
        else:	
            # SOURCE LINE 104
            __M_writer('\t\t\t\t\t<td>$')
            __M_writer(str(useroption.price))
            __M_writer('</td>\r\n')
        # SOURCE LINE 106
        __M_writer('\t\t\t\t</tr>\r\n\t\t</tbody>\r\n\t</table>\r\n<br>\r\nYour Order Details\r\n\t<table class = "table table-striped table-hover">\r\n\t\t<thead>\r\n\t\t\t<tr class="success">\r\n\t\t\t\t<th>Estimated Arrival</th>\r\n\t\t\t\t<th>Order Total</th>\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\r\n\t\t\t<tr class="active">\r\n\t\t\t\t<td>')
        # SOURCE LINE 121
        __M_writer('&nbsp')
        __M_writer('&nbsp')
        __M_writer('&nbsp')
        __M_writer('&nbsp')
        __M_writer(str(EndDate))
        __M_writer('</td>\r\n\t\t\t\t<td>')
        # SOURCE LINE 122
        __M_writer('&nbsp')
        __M_writer('&nbsp')
        __M_writer('&nbsp')
        __M_writer('&nbsp')
        __M_writer(str(totalcharged))
        __M_writer('</td>\r\n\t\t\t</tr>\r\n\t\t</tbody>\r\n\t</table>\r\n ')
        return ''
    finally:
        context.caller_stack._pop_frame()


