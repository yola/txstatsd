import logging

from yodeploy.hooks.configurator import ConfiguratedApp
from yodeploy.hooks.python import PythonApp
from yodeploy.hooks.templating import TemplatedApp
from yodeploy.hooks.daemon import DaemonApp
from yodeploy.util import touch

log = logging.getLogger(__name__)


class Hooks(ConfiguratedApp, PythonApp, DaemonApp, TemplatedApp):
    def prepare(self):
        super(Hooks, self).prepare()
        self.template('txstatsd.conf.template', '/etc/yola/txstatsd.conf')

        logfile = self.config.get(self.app).path.log
        if logfile:
            touch(logfile, 'root', 'adm', 0o640)

hooks = Hooks
