# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1394326271.396447
_enable_loop = True
_template_filename = 'C:\\myStuff\\homePage\\templates/checkout.html'
_template_uri = 'checkout.html'
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
        subtotal = context.get('subtotal', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        Objects = context.get('Objects', UNDEFINED)
        shippingobject = context.get('shippingobject', UNDEFINED)
        billings = context.get('billings', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        shippings = context.get('shippings', UNDEFINED)
        shippingoptions = context.get('shippingoptions', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        subtotal = context.get('subtotal', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        Objects = context.get('Objects', UNDEFINED)
        shippingobject = context.get('shippingobject', UNDEFINED)
        billings = context.get('billings', UNDEFINED)
        def content():
            return render_content(context)
        shippings = context.get('shippings', UNDEFINED)
        shippingoptions = context.get('shippingoptions', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer('\r\n<h3>Checkout</h3>\r\n<form action = "/homePage/order/" method = \'POST\'>\r\n<br>\r\nYour Ordered Items\r\n')
        # SOURCE LINE 8
        for product in Objects:
            # SOURCE LINE 9
            __M_writer('<div class="panel panel-default">  \r\n<table class = "table table-striped">\r\n\r\n\t<tbody>\r\n\t\t\r\n\t<tr class ="active">\r\n\t\t\t\r\n\t\t\t<td><a href=""><img src="')
            # SOURCE LINE 16
            __M_writer(str( STATIC_URL + product.imagePath))
            __M_writer('" width=\'150\' height=\'140\'/></a></td>\r\n\t\t\t<td><p><span style="font-size:24px;">')
            # SOURCE LINE 17
            __M_writer(str(product.catalogProductID))
            __M_writer('</span></p>\r\n\t\t\t\t<p><span style="font-size:20px;">Item Price:<span style="color:#ff0000;">')
            # SOURCE LINE 18
            __M_writer(str(product.price))
            __M_writer("</span></span></p>\r\n\t\t\t\t<p class = 'underline'>")
            # SOURCE LINE 19
            __M_writer(str(product.description))
            __M_writer('</p>\r\n\t\t\t\t<p>Quantity: ')
            # SOURCE LINE 20
            __M_writer(str(Objects[product]))
            __M_writer('\r\n\t\t\t\t<a href="/homePage/cart/remove/')
            # SOURCE LINE 21
            __M_writer(str(product.id))
            __M_writer('" class="btn btn-primary btn-danger"><span class="glyphicon glyphicon-shopping-cart"></span> Remove Item</a></td>\r\n\t\t</div>\r\n\t</tr>\r\n\r\n\t</tbody>\r\n\t</table>\r\n\r\n</div>\t\r\n')
        # SOURCE LINE 30
        __M_writer('\r\n<h3>Billing Information</h3>\r\n\t<table class = "table table-striped table-hover">\r\n\t\t<thead>\r\n\t\t\t<tr class="success">\r\n\t\t\t\t\t<th></th>\r\n\t\t\t\t\t<th>Name on Card</th>\r\n\t\t\t\t\t<th>Description</th>\r\n\t\t\t\t\t<th></th>\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\r\n')
        # SOURCE LINE 43
        for o in billings:
            # SOURCE LINE 44
            __M_writer('\t\t\t\t<tr class="active">\r\n\t\t\t\t\t<td><input type="radio" name="billing" value="')
            # SOURCE LINE 45
            __M_writer(str(o.id))
            __M_writer('}"></td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 46
            __M_writer(str(o.name))
            __M_writer('</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 47
            __M_writer(str(o.cardtype.name))
            __M_writer(' ending in ')
            __M_writer(str(o.number[-4:]))
            __M_writer('</td>\r\n\t\t\t\t\t<td><a href="/homePage/billing/')
            # SOURCE LINE 48
            __M_writer(str(o.id))
            __M_writer('/checkout">Edit</a></td>\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 51
        __M_writer('\t\t</tbody>\r\n\t</table>\r\n\t<a href="/homePage/billing/checkout" class="btn btn-primary btn-primary"><span class="glyphicon glyphicon-shopping-cart"></span>New Billing Option</a>\r\n\r\n<br>\r\n<h3>Shipping Information</h3>\r\n\t<table class = "table table-striped table-hover">\r\n\t\t<thead>\r\n\t\t\t<tr class="success">\r\n\t\t\t\t<th></th>\r\n')
        # SOURCE LINE 61
        for value in shippingobject.customer():
            # SOURCE LINE 62
            __M_writer('\t\t\t\t\t<th>')
            __M_writer(str(value.key))
            __M_writer('</th>\r\n')
        # SOURCE LINE 64
        __M_writer('\t\t\t\t<th></th>\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\t\t\t\r\n\r\n')
        # SOURCE LINE 70
        for o in shippings:
            # SOURCE LINE 71
            __M_writer('\t\t\t\t<tr class="active">\r\n\t\t\t\t\t<td><input type="radio" name="shipping" value="')
            # SOURCE LINE 72
            __M_writer(str(o.id))
            __M_writer('}"></td>\r\n')
            # SOURCE LINE 73
            for value in o.customer():
                # SOURCE LINE 74
                __M_writer('\t\t\t\t\t\t<td>')
                __M_writer(str(value.value))
                __M_writer('</td>\r\n')
            # SOURCE LINE 76
            __M_writer('\t\t\t\t\t<td><a href="/homePage/shipping_details/')
            __M_writer(str(o.id))
            __M_writer('/checkout">Edit</a></td>\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 79
        __M_writer('\t\t\t\r\n\t\t</tbody>\r\n\t</table>\r\n\t<a href="/homePage/shipping_details/checkout" class="btn btn-primary btn-primary">New Shipping Address</a>\r\n<br>\r\n<br>\r\n<p></p>\r\n\r\n<h3>Shipping Options</h3>\r\n\t<table class = "table table-striped table-hover">\r\n\t\t<thead>\r\n\t\t\t<tr class="success">\r\n\t\t\t\t\t<th></th>\r\n\t\t\t\t\t<th>Option</th>\r\n\t\t\t\t\t<th>Price</th>\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\r\n')
        # SOURCE LINE 98
        for o in shippingoptions:
            # SOURCE LINE 99
            __M_writer('\t\t\t\t<tr class="active">\r\n\t\t\t\t\t<td><input type="radio" name="shippingoptions" value="')
            # SOURCE LINE 100
            __M_writer(str(o.id))
            __M_writer('}"></td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 101
            __M_writer(str(o.daystoarrive))
            __M_writer('-Day Shipping</td>\r\n\t\t\t\t\r\n')
            # SOURCE LINE 103
            if o.price == 0:
                # SOURCE LINE 104
                __M_writer('\t\t\t\t\t<td>Free!</td>\r\n')
                # SOURCE LINE 105
            else:	
                # SOURCE LINE 106
                __M_writer('\t\t\t\t\t<td>$')
                __M_writer(str(o.price))
                __M_writer('</td>\r\n')
            # SOURCE LINE 108
            __M_writer('\t\t\t\t</tr>\r\n')
        # SOURCE LINE 110
        __M_writer('\t\t</tbody>\r\n\t</table>\r\n<br>\r\n\r\n\r\n\r\n\r\n\r\nYour Order Details\r\n\t<table class = "table table-striped table-hover">\r\n\t\t<thead>\r\n\t\t\t<tr class="success">\r\n\t\t\t\t<th>Estimated Arrival</th>\r\n\t\t\t\t<th>Order Total</th>\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\r\n\t\t\t\r\n\t\t\t<tr class="active">\r\n\t\t\t\t<td>')
        # SOURCE LINE 130
        __M_writer('&nbsp')
        __M_writer('&nbsp')
        __M_writer('&nbsp')
        __M_writer('&nbspMarch 17th, 2014</td>\r\n\t\t\t\t<td>')
        # SOURCE LINE 131
        __M_writer('&nbsp')
        __M_writer('&nbsp')
        __M_writer('&nbsp')
        __M_writer('&nbsp')
        __M_writer(str(subtotal))
        __M_writer("</td>\r\n\t\t\t</tr>\r\n\t\t</tbody>\r\n\t</table>\r\n\r\n<button type = 'submit' class = 'btn btn-success'> Submit Order</button>\r\n</form>\r\n ")
        return ''
    finally:
        context.caller_stack._pop_frame()


