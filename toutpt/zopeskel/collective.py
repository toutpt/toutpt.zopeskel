import copy
import os

from zopeskel.base import get_var
from zopeskel.plone import Plone

class Collective(Plone):
    """diazo theme"""
    _template_dir = "templates/toutpt_collective"
    summary= u"A collective package"

    use_local_commands = False #or setup.cfg will be re created

    vars = copy.deepcopy(Plone.vars)
    get_var(vars, 'description').default = 'Addon for Plone'
    get_var(vars, 'url').default =  'https://github.com/collective/'

    def post(self, command, output_dir, vars):
        super(Collective, self).post(command, output_dir, vars)
        
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
