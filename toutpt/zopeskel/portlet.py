import copy
import os

from zopeskel.nested_namespace import NestedNamespace
from zopeskel.base import get_var
from zopeskel.plone3_portlet import Plone3Portlet

class CollectivePortlet(Plone3Portlet):
    category = "Plone Development"
    _template_dir = "templates/toutpt_collectiveportlet"
    summary= u"A plone3 portlet"
    ndots = 2
    use_local_commands = False #or setup.cfg will be re created
    use_cheetah = True

    vars = copy.deepcopy(Plone3Portlet.vars)

    def post(self, command, output_dir, vars):
        #add gitignore
        path = os.path.join(output_dir)
        try:
            os.rename(os.path.join(path, 'gitignore'),
                      os.path.join(path, '.gitignore'))
        except OSError, e:
            msg = """WARNING: Could not create .gitignore file: %s"""
            self.post_run_msg = msg % str(e)
        try:
            os.rename(os.path.join(path, 'travis.yml'),
                      os.path.join(path, '.travis.yml'))
        except OSError, e:
            msg = """WARNING: Could not create .travis.yml file: %s"""
            self.post_run_msg = msg % str(e)
