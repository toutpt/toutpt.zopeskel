import copy

from zopeskel import plone3_theme
from zopeskel.base import get_var
from zopeskel.plone import Plone

class Theme(plone3_theme.Plone3Theme):
    """diazo theme"""
    _template_dir = "templates/toutpt_diazotheme"
    summary= u"A diazo theme based on 960 css"
    
    vars = copy.deepcopy(plone3_theme.Plone3Theme.vars)
    get_var(vars, 'description').default = 'An installable diazo theme for Plone 4'
    get_var(vars, 'skinbase').default = 'Sunburst Theme'
    get_var(vars, 'url').default =  'https://github.com/collective/'

    vars.remove(get_var(vars, 'empty_styles'))
    vars.remove(get_var(vars, 'include_doc'))

    def post(self, command, output_dir, vars):
        vars['empty_styles'] = False
        vars['include_doc'] = False
        super(Theme, self).post(command, output_dir, vars)
