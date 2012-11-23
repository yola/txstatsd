import logging

from yola.deploy.hooks.configurator import ConfiguratedApp
from yola.deploy.hooks.python import PythonApp
from yola.deploy.hooks.templating import TemplatedApp
from yola.deploy.hooks.upstart import UpstartApp
from yola.deploy.util import touch

log = logging.getLogger(__name__)


class Hooks(ConfiguratedApp, PythonApp, UpstartApp, TemplatedApp):
    def prepare(self):
        super(Hooks, self).prepare()
        self.template('txstatsd.conf.template', '/etc/yola/txstatsd.conf')

        logfile = self.config.get(self.app).path.log
        if logfile:
            touch(logfile, 'root', 'adm', 0640)

hooks = Hooks
