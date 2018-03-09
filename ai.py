from threading import Thread

import math

import api
import context
import utils
from map import Map


class AI:
    def __init__(self):
        status_report = api.startup()
        start_time = status_report['team']['start_time']
        self.start_epoch = utils.convert(start_time)
        context.balance = 175

        parameters = api.parameters()
        self.lifetime = parameters['lifetime']
        self.hub_capacity = parameters['hub_capacity']
        self.mining_rate = parameters['mining_rate']
        self.ms_per_week = parameters['ms_per_week']

        costs = parameters['costs']
        self.map = Map(self.start_epoch, self.ms_per_week, costs, parameters['rows'], parameters['cols'])

    def run(self):
        watcher = Thread(target=self.ship_move_build)
        watcher.start()

        getter = Thread(target=self.getter)
        getter.start()

        getter.join()
        watcher.join()
        print('Finished')

    def getter(self):
        next_epoch = self.start_epoch
        while True:
            if utils.current_epoch() > next_epoch:
                prospect_report = api.prospect_report()
                next_epoch += self.ms_per_week * 78

                self.map.append(prospect_report['report'])

    def ship_move_build(self):
        week_delay = int(math.floor((self.hub_capacity / 8 / self.mining_rate)))
        print('Week Delay: {}'.format(week_delay))
        week = 0

        next_epoch = self.start_epoch
        while True:
            if utils.current_epoch() > next_epoch:
                status_report = api.status_report()
                next_epoch += self.ms_per_week * week_delay
                week += week_delay

                hubs = status_report['hubs']
                for key in hubs:
                    hub = hubs[key]
                    space_remaining = hub['space_remaining']
                    active = hub['active']

                    if space_remaining and not active:
                        self.map.move(hub)
                    elif space_remaining < 10 or week > 480:
                        self.map.ship(hub, insure=True)

                self.map.build()


if __name__ == '__main__':
    AI().run()
