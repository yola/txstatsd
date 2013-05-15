from yoconfigurator.dicts import merge_dicts


def update(config):
    new = {
        'txstatsd': {
            'port': 8125,
            'flush_interval': 60000,
            'path': {
                'log': '/var/log/txstatsd.log',
            },
        },
    }
    return merge_dicts(config, new)
