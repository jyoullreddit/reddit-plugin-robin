from pylons.i18n import N_

from r2.lib.configparse import ConfigValue
from r2.lib.js import LocalizedModule
from r2.lib.plugin import Plugin


class Robin(Plugin):
    needs_static_build = True

    js = {
        "robin": LocalizedModule("robin.js",
            # TODO: your javascript files go here, e.g.:
            # "robin/something.js",
        ),
    }

    config = {
        # TODO: your static configuratation options go here, e.g.:
        # ConfigValue.int: [
        #     "robin_blargs",
        # ],
    }

    live_config = {
        # TODO: your live configuratation options go here, e.g.:
        # ConfigValue.int: [
        #     "robin_realtime_blargs",
        # ],
    }

    errors = {
        # TODO: your API errors go here, e.g.:
        # "ROBIN_NOT_COOL": N_("not cool"),
    }

    def add_routes(self, mc):
        # TODO: register your routes here, e.g.:
        #
        # mc("/myplugin", controller="robincontroller", action="something")
        pass

    def load_controllers(self):
        # TODO: import any other controllers you define here
        from reddit_robin.controllers import (
            RobinController,
        )

        # TODO: register any hooks you define in your modules here, e.g.:
        #
        # from reddit_robin import some_module
        # some_module.hooks.register_all()

    def declare_queues(self, queues):
        # TODO: add any queues / bindings you need here, e.g.:
        #
        # queues.some_queue_defined_elsewhere << "routing_key"
        #
        # or
        #
        # from r2.config.queues import MessageQueue
        # queues.declare({
        #     "some_q": MessageQueue(),
        # })
        pass
