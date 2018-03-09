from urllib import request


def get(name, params=None):
    param_str = ''

    if params is not None:
        for param_key in params:
            param_str += '&'
            param_str += param_key + '='

            if isinstance(params[param_key], list)
                param_str += '['
                for i, val in enumerate(params[param_key]):
                    if i != 0:
                        param_str += ','
                    param_str += val
                param_str += ']'
            else:
                param_str += str(params[param_key])

    return request.urlopen("https://7066414.pythonanywhere.com/mcp/{}?token=78b9a29078a60441508d28c2f67a7ebb{}"
                           .format(name, param_str)).read()


def startup():
    return get(startup.__name__)


def status_report():
    return get(status_report.__name__)


def get_ledger():
    return get(status_report.__name__)


def parameters():
    return get(parameters.__name__)


def prospect_report():
    return get(prospect_report.__name__)


def market_report():
    return get(market_report.__name__)


def build_hubs(hubs):
    return get(build_hubs.__name__, {'hubs': hubs})


def deploy_hubs(hubs, sector_ids):
    return get(deploy_hubs.__name__, {'hubs': hubs, 'sector_ids': sector_ids})


def move_hubs(hubs, sector_ids)
    return get(move_hubs.__name__, {'hubs': hubs, 'sector_ids': sector_ids})


def ship_ore(hubs, insured)
    return get(ship_ore.__name__, {'hubs': hubs, 'insured': insured})
