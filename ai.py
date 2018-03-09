from threading import Thread

import pprint
import math

import api
import utils
from map import Map


class AI:
    def __init__(self):
        status_report = api.startup()
        start_time = status_report['team']['start_time']
        self.start_epoch = utils.convert(start_time)
        self.balance = 150

        parameters = api.parameters()
        self.lifetime = parameters['lifetime']
        self.hub_capacity = parameters['hub_capacity']
        self.mining_rate = parameters['mining_rate']
        self.ms_per_week = parameters['ms_per_week']

        costs = parameters['costs']
        self.hub_cost = costs['hub']['rate']
        self.hub_weeks = costs['hub']['weeks']

        self.deploy_cost = costs['deploy']['rate']
        self.deploy_weeks = costs['deploy']['weeks']

        self.ship_cost = costs['ship']['rate']
        self.ship_weeks = costs['ship']['weeks']

        self.move_cost = costs['move']['rate']
        self.move_weeks = costs['move']['weeks']

        self.map = Map(parameters['rows'], parameters['cols'])
        self.hubs = {}
        self.hub_count = 0

        self.pp = pprint.PrettyPrinter(indent=6)

    def run(self):
        watcher = Thread(target=self.watch)

        alg = Thread(target=self.algorithm)
        alg.start()

        alg.join()
        watcher.join()
        print('Finished')

    def algorithm(self):
        print('Starting algorithm')
        print(self.start_epoch)

        next_epoch = self.start_epoch
        while True:
            if utils.current_epoch() > next_epoch:
                prospect_report = api.prospect_report()
                next_epoch += self.ms_per_week * 78

                self.pp.pprint(prospect_report['report'])
                self.map.append(prospect_report['report'])

        self.build_and_deploy([0])

    def watch(self):
        week_delay = int(math.floor((self.hub_capacity / 8 / self.mining_rate)))
        print('Week Delay: {}'.format(week_delay))

    def build_and_deploy(self, sector_ids):
        new_hubs = ['H{}'.format(self.hub_count+i) for i in sector_ids]
        api.build_hubs(new_hubs)

        for new_hub, sector_id in zip(new_hubs, sector_ids):
            self.hubs[new_hub] = sector_id


if __name__ == '__main__':
    AI().run()
