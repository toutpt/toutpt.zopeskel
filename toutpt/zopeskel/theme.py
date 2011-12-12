import copy
import os

from zopeskel import plone3_theme
from zopeskel.base import get_var
from zopeskel.plone import Plone

class Theme(plone3_theme.Plone3Theme):
    """diazo theme"""
    _template_dir = "templates/toutpt_diazotheme"
    summary= u"A diazo theme based on 960 css"

    use_local_commands = False #or setup.cfg will be re created

    vars = copy.deepcopy(plone3_theme.Plone3Theme.vars)
    get_var(vars, 'description').default = 'An installable diazo theme for Plone 4'
    get_var(vars, 'skinbase').default = 'Sunburst Theme'
    get_var(vars, 'url').default =  'https://github.com/collective/'
    get_var(vars, 'skinname').default = 'My theme'

    vars.remove(get_var(vars, 'empty_styles'))
    vars.remove(get_var(vars, 'include_doc'))

    def post(self, command, output_dir, vars):
        vars['empty_styles'] = False
        vars['include_doc'] = False
        super(Theme, self).post(command, output_dir, vars)
        
        #remove setup.cfg
        path = os.path.join(output_dir)
        try:
            os.remove(os.path.join(path, 'setup.cfg'))
        except OSError, e:
            msg = """WARNING: Could not find setup.cfg: %s"""
            self.post_run_msg = msg % str(e)

        #add gitignore
        try:
            os.rename(os.path.join(path, 'gitignore'),
                      os.path.join(path, '.gitignore'))
        except OSError, e:
            msg = """WARNING: Could not create .gitignore file: %s"""
            self.post_run_msg = msg % str(e)

        #remove README.txt (use README.rst)
        try:
            os.remove(os.path.join(path, 'README.txt'))
        except OSError, e:
            msg = """WARNING: Could not remove README.txt: %s"""
            self.post_run_msg = msg % str(e)
