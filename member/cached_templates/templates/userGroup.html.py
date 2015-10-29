# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1430354237.3031
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/compfitition-2.1/member/templates/userGroup.html'
_template_uri = 'userGroup.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'footer', 'header']


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
        groups = context.get('groups', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        groups = context.get('groups', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div>\n\t\n</div>\n\n<!-- WRAPPER -->\n\t\t<div id="wrapper">\n\n\t\t\t<!-- PAGE TITLE -->\n\t\t\t<header id="page-title">\n\t\t\t\t<div class="container">\n\t\t\t\t\t<h1>Groups</h1>\n\n\t\t\t\t\t<ul class="breadcrumb">\n\t\t\t\t\t\t<li><a href="http://localhost:8000/">Home</a></li>\n\t\t\t\t\t\t<!--we need a general user page-->\n\t\t\t\t\t\t<li><a href="http://localhost:8000/">User</a></li>\n\t\t\t\t\t\t<li class="active">Groups</li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t</header>\n\n')
        if groups:
            __M_writer('\t<div class="col-md-12">\n\t\t<table class= "table table-striped table-hover">\n\t\t\t\t<thead>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<th>Group Name</th>\n\t\t\t\t\t\t<th>Group Admin</th>\n\t\t\t\t\t</tr>\n\t\t\t\t</thead>\n\t\t\t\t<tbody>\n')
            for q in groups:
                __M_writer('\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t<td><a href ="/member/group_members/')
                __M_writer(str(q.group.id))
                __M_writer('">')
                __M_writer(str(q.group))
                __M_writer('</a></td>\n')
                if q.group.administrator == request.user:
                    __M_writer("\t\t\t\t\t\t\t\t<td><a class='btn btn-primary' href='/Manager/groups/")
                    __M_writer(str(q.group.id))
                    __M_writer("'>Go to Admin Page</a></td>\n")
                else:	
                    __M_writer('\t\t\t\t\t\t\t\t<a href ="google.com"> <td>')
                    __M_writer(str(q.group.administrator))
                    __M_writer('</td>\t</a>\n\t\t\t\t\t\t\t\t\n')
                __M_writer("\t\t\t\t\t\t\t<td><a class='btn btn-primary' href='/member/'>Make an Entry</a></td>\t\t\t\t\n\t\t\t\t\t\t</tr>\n")
            __M_writer('\t\t\t\t</tbody>\n\t\t</table>\n\t</div>\n\t<div>\n\t<form class="navbar-form navbar-left" role="search" action="/homePage/search/">\n\t    <div class="form-group">\n\t      <input type="text" class="form-control" name = "search" placeholder="Find another group to join">\n\t    </div>\n\t    <button type="submit" class="btn btn-default">Search</button>\n\t</form>\n\t</div>\n')
        else:
            __M_writer('\t<div class="jumbotron">\n\t\t<p>\n\t\t\t<h2>\n\t\t\t\t<center>\n\t\t\t\t\tYour Fitness Groups\n\t\t\t\t</center>\n\t\t\t</h2>\n\t\t</p>\n\t<p>\n\t\t<h3>\n\t\t\t<center>\n\t\t\t\tLooks like you have not joined any groups yet.\n\t\t\t\t<br>\n\t\t\t\tSearch for or check out some different groups to get started.\n\t\t\t</center>\n\t\t</h3>\n\t</P>\n\t<p>\n\t\t<center><h3>\n\t\t\t<a href="/Manager/edit_group/new">\n\t\t\t\tCreate Group\n\t\t\t</a></h3>\n\t\t</center>\n\t</p>\n\t\n\t</div>\n\n\n\t\t\t<section class="container">\n\n\t\t\t\t<!-- CALLOUT -->\n\t\t\t\t<div class="row bs-callout">\n\t\t\t\t\t<div class="col-md-8 text-center">\n\t\t\t\t\t\t<h3 class="padding20">Search <strong>now</strong>, and start <strong>competing</strong> !</h3>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<div class="col-md-4">\n\n\t\t\t\t\t\t<p class="nomargin">Type a group name here:</p>\n\n\t\t\t\t\t\t<form method="get" action="/homePage/search/" class="input-group"> <!--action send information to this location-->\n\t\t\t\t\t\t\t<input type="text" class="form-control" name="k" id="k" value="" placeholder="Find a group to join" />\n\t\t\t\t\t\t\t<span class="input-group-btn">\n\t\t\t\t\t\t\t\t<button class="btn btn-primary"><i class="fa fa-search"></i></button>\n\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t</form>\n\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<p><center><h4>-or-</h4></center></p>\n\t\t\t\t<!-- /CALLOUT -->\n\n\t\t\t</section>\n\n\t\t\t<section id="portfolio" class="container">\n\n\t\t\t\t<center><h2><strong>Compete</strong> with a group near you!</h2></center>\n\n\t\t\t\t<p class="lead">People are always competing. Listed below are a some local groups that you may want to join. Click a group to learn more!</p>\n\n\t\t\t\t<ul class="nav nav-pills isotope-filter isotope-filter" data-sort-id="isotope-list" data-option-key="filter">\n\t\t\t\t\t<li data-option-value="*" class="active"><a href="#">Show All</a></li>\n\t\t\t\t\t<li data-option-value=".development"><a href="#">Development</a></li>\n\t\t\t\t\t<li data-option-value=".photography"><a href="#">Photography</a></li>\n\t\t\t\t\t<li data-option-value=".design"><a href="#">Design</a></li>\n\t\t\t\t</ul>\n\n\n\t\t\t\t<div class="row">\n\n\t\t\t\t\t<ul class="sort-destination isotope" data-sort-id="isotope-list">\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 development"><!-- item -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover" href="portfolio-single.html">\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>PROJECT</strong> DETAIL\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/scouter-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Atropos Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 photography"><!-- item 2 -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover lightbox" href="http://www.youtube.com/watch?v=W7Las-MJnJo" data-plugin-options=\'{"type":"iframe"}\'>\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>VIEW</strong> VIDEO\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/black-kitty-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Video Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 design"><!-- item 3 -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover" href="portfolio-single.html">\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>PROJECT</strong> DETAIL\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/merchant2-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Atropos Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 photography"><!-- item 4 -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover" href="portfolio-single.html">\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>PROJECT</strong> DETAIL\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/flippin-the-bird1-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Atropos Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 development"><!-- item 5 -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover lightbox" href="http://www.youtube.com/watch?v=W7Las-MJnJo" data-plugin-options=\'{"type":"iframe"}\'>\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>VIEW</strong> VIDEO\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/night_to_remember1-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Video Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 design"><!-- item 6 -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover" href="portfolio-single.html">\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>PROJECT</strong> DETAIL\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/spacebound-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Atropos Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 photography design"><!-- item 7 -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover lightbox" href="http://www.youtube.com/watch?v=W7Las-MJnJo" data-plugin-options=\'{"type":"iframe"}\'>\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>VIEW</strong> VIDEO\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/be-my-guest1-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Atropos Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 development"><!-- item 8 -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover" href="portfolio-single.html">\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>PROJECT</strong> DETAIL\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/black-box5-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Atropos Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 development"><!-- item -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover" href="portfolio-single.html">\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>PROJECT</strong> DETAIL\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/weather-app-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Atropos Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 photography"><!-- item 2 -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover lightbox" href="http://www.youtube.com/watch?v=W7Las-MJnJo" data-plugin-options=\'{"type":"iframe"}\'>\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>VIEW</strong> VIDEO\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/theMoose-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Atropos Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 design"><!-- item 3 -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover" href="portfolio-single.html">\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>PROJECT</strong> DETAIL\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/tumblr_mopqj9QUeq1st5lhmo1_12801-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Atropos Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t\t<li class="isotope-item col-sm-6 col-md-4 photography"><!-- item 4 -->\n\t\t\t\t\t\t\t<div class="item-box">\n\t\t\t\t\t\t\t\t<figure>\n\t\t\t\t\t\t\t\t\t<a class="item-hover lightbox" href="http://www.youtube.com/watch?v=W7Las-MJnJo" data-plugin-options=\'{"type":"iframe"}\'>\n\t\t\t\t\t\t\t\t\t\t<span class="overlay color2"></span>\n\t\t\t\t\t\t\t\t\t\t<span class="inner">\n\t\t\t\t\t\t\t\t\t\t\t<span class="block fa fa-plus fsize20"></span>\n\t\t\t\t\t\t\t\t\t\t\t<strong>VIEW</strong> VIDEO\n\t\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t<img class="img-responsive" src="assets/images/demo/portfolio/scouter-600x403.jpg" width="260" height="260" alt="">\n\t\t\t\t\t\t\t\t</figure>\n\t\t\t\t\t\t\t\t<div class="item-box-desc">\n\t\t\t\t\t\t\t\t\t<h4>Atropos Project</h4>\n\t\t\t\t\t\t\t\t\t<small class="styleColor">29 June, 2014</small>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\n\t\t\t\t\t</ul>\n\n\t\t\t\t</div><!-- /.masonry-container -->\n\n\t\t\t\t<!-- CALLOUT -->\n\t\t\t\t<div class="bs-callout text-center nomargin-bottom">\n\t\t\t\t\t<h3>Do you like what you see? <a href="contact-us.html" target="_blank" class="btn btn-primary btn-lg">Yes, let uss work together!</a></h3>\n\t\t\t\t</div>\n\t\t\t\t<!-- /CALLOUT -->\n\n\n\t\t\t</section>\n\n\t\t</div>\n\t\t<!-- /WRAPPER -->\n\n')
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


"""
__M_BEGIN_METADATA
{"uri": "userGroup.html", "source_encoding": "ascii", "filename": "/Users/benmackley/Projects/compfitition-2.1/member/templates/userGroup.html", "line_map": {"68": 6, "69": 28, "70": 29, "71": 38, "72": 39, "73": 40, "74": 40, "75": 40, "76": 40, "77": 41, "78": 42, "79": 42, "80": 42, "81": 43, "82": 44, "83": 44, "84": 44, "85": 47, "86": 50, "87": 61, "88": 62, "27": 0, "94": 381, "100": 381, "40": 1, "106": 3, "45": 5, "112": 3, "50": 379, "118": 112, "60": 6}}
__M_END_METADATA
"""
