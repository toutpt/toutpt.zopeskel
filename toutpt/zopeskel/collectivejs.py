import copy
import os

from zopeskel.nested_namespace import NestedNamespace
from zopeskel.base import get_var

class CollectiveJS(NestedNamespace):
    category = "Plone Development"
    _template_dir = "templates/toutpt_collectivejs"
    summary= u"A package to embed a javascript"
    ndots = 2
    use_local_commands = False #or setup.cfg will be re created
    use_cheetah = True

    vars = copy.deepcopy(NestedNamespace.vars)
    get_var(vars, 'namespace_package').default = 'collective'
    get_var(vars, 'namespace_package2').default = 'js'

    def post(self, command, output_dir, vars):
        #add gitignore
        path = os.path.join(output_dir)
        try:
            os.rename(os.path.join(path, 'gitignore'),
                      os.path.join(path, '.gitignore'))
        except OSError, e:
            msg = """WARNING: Could not create .gitignore file: %s"""
            self.post_run_msg = msg % str(e)
