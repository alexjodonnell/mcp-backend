from threading import Thread

import api
import utils
from map import Map

WEEK = 350


class AI:
    def __init__(self):
        status_report = api.startup()
        start_time = status_report['team']['start_time']
        self.start_epoch = utils.convert(start_time)

        parameters = api.parameters()
        self.lifetime = parameters['lifetime']
        self.hub_capacity = parameters['hub_capacity']
        self.mining_rate = parameters['mining_rate']
        self.ms_per_week = parameters['ms_per_week']

        costs = parameters['costs']
        self.build_cost = costs['build']['rate']
        self.build_weeks = costs['build']['weeks']

        self.deploy_cost = costs['deploy']['rate']
        self.deploy_weeks = costs['deploy']['weeks']

        self.ship_cost = costs['ship']['rate']
        self.ship_weeks = costs['ship']['weeks']

        self.move_cost = costs['build']['rate']
        self.move_weeks = costs['build']['weeks']

        self.map = Map(parameters['rows'], parameters['cols'])

    def run(self):
        getter = Thread(target=self.get_data)
        getter.start()

        alg = Thread(target=self.algorithm)
        alg.start()

        getter.join()
        alg.join()
        print('Finished')

    def get_data(self):
        print(self.start_epoch)
        while True:
            next_epoch = self.start_epoch
            if utils.current_epoch() > next_epoch:
                prospect_report = api.prospect_report()
                next_epoch += WEEK * 78
                self.map.append(prospect_report['report'])

                status_report = api.status_report()
                print(status_report['team']['week'])

    def algorithm(self):
        pass


if __name__ == '__main__':
    AI().run()
