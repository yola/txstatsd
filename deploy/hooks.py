import logging
import subprocess

from yola.deploy.hooks.configurator import ConfiguratedApp
from yola.deploy.hooks.python import PythonApp
from yola.deploy.hooks.templating import TemplatedApp
from yola.deploy.util import touch

log = logging.getLogger(__name__)


class Hooks(ConfiguratedApp, PythonApp, TemplatedApp):
    def prepare(self):
        super(Hooks, self).prepare()
        self.template('txstatsd.conf.template', '/etc/yola/txstatsd.conf')
        self.template('txstatsd.upstart.template', '/etc/init/txstatsd.conf')

        logfile = self.config.get(self.app).path.log
        if logfile:
            touch(logfile, 'root', 'adm', 0640)

    def deployed(self):
        super(Hooks, self).deployed()
        try:
            subprocess.call(('service', 'txstatsd', 'stop'))
            subprocess.check_call(('service', 'txstatsd', 'start'))
        except subprocess.CalledProcessError:
            log.error("Unable to restart txstatsd")

hooks = Hooks
