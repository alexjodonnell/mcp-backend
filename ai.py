import api
import utils


class AI:
    def __init__(self):
        res = api.startup()
        start_time = res['team']['start_time']
        self.start_epoch = utils.convert(start_time)

        res = api.parameters()
        self.lifetime = res['lifetimes']
        self.rows = res['rows']
        self.cols = res['cols']
        self.hub_capacity = res['hub_capacity']
        self.mining_rate = res['mining_rate']
        self.ms_per_week = res['ms_per_week']
        self.costs = res['costs']


if __name__ == '__name__':
    AI()
