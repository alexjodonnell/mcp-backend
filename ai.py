from threading import Thread

import pprint
import math

import api
import utils
from centroid_finder import centroid_locator
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

        self.map = Map(self.start_epoch, self.ms_per_week, self.hub_weeks, parameters['rows'], parameters['cols'])

        self.pp = pprint.PrettyPrinter(indent=6)

    def run(self):
        alg = Thread(target=self.algorithm)
        alg.start()

        alg.join()
        print('Finished')

    def algorithm(self):
        print('Starting algorithm')

        next_epoch = self.start_epoch
        while True:
            if utils.current_epoch() > next_epoch:
                prospect_report = api.prospect_report()
                next_epoch += self.ms_per_week * 78

                self.pp.pprint(prospect_report['report'])
                self.map.append(prospect_report['report'])

                centroids = centroid_locator(self.map.points(), 0.15, 3)
                self.map.mine(centroids[:1])
                break

    def watch(self):
        week_delay = int(math.floor((self.hub_capacity / 8 / self.mining_rate)))
        print('Week Delay: {}'.format(week_delay))


if __name__ == '__main__':
    AI().run()
