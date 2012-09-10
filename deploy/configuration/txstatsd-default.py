from yola.configurator.dicts import merge_dicts


def update(config):
    new = {
        'txstatsd': {
            'path': {
                'log': '/var/log/txstatsd.log',
            },
        },
    }
    return merge_dicts(config, new)
