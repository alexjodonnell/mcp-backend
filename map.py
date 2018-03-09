import numpy as np

import api
import context
from centroid_finder import centroid_locator
from utils import delay_until


class Map:
    def __init__(self, start_epoch, ms_per_week, costs, rows, cols):
        self.rows = rows
        self.cols = cols
        self.map = np.zeros([rows, cols])
        self.types = np.chararray([rows, cols])
        self.build_count = 0
        self.max_build = 6

        self.hubs = {}

        self.start_epoch = start_epoch
        self.ms_per_week = ms_per_week

        self.hub_cost = costs['hub']['rate']
        self.hub_weeks = costs['hub']['weeks']

        self.deploy_cost = costs['deploy']['rate']
        self.deploy_weeks = costs['deploy']['weeks']

        self.ship_cost = costs['ship']['rate']
        self.ship_weeks = costs['ship']['weeks']

        self.move_cost = costs['move']['rate']
        self.move_weeks = costs['move']['weeks']

    def append(self, prospect_map):
        for sector_id, ore_type, estimated_tonnes in prospect_map:
            row, col = divmod(sector_id, self.cols)

            self.map[row][col] = estimated_tonnes
            self.types[row][col] = ore_type

        # requests.post("http://localhost:3000/dashboard/map", data={'map': self.points()})

    def build(self):
        if context.balance < self.hub_cost + self.deploy_cost:
            return

        if self.build_count >= self.max_build:
            return

        context.balance -= self.hub_cost + self.deploy_cost
        self.build_count += 1

        points = self.points()
        if len(points) == 0:
            return

        centroids = centroid_locator(points, 0.15, 3)
        coords = centroids[:1]

        sector_ids = [coord[0] * self.cols + coord[1] for coord in coords]
        self.zero(coords)

        new_hubs = ['H{}'.format(sector_id) for sector_id in sector_ids]
        api.build_hubs(new_hubs)

        while True:
            status_report = api.status_report()
            orders = status_report['orders']
            for order in orders:
                if order['action'] == 'deliver_hubs':
                    break
            else:
                print('Trying again')
                continue

            break

        start_week = order['week']
        delay_until(self.start_epoch, start_week + self.hub_weeks, self.ms_per_week)
        api.deploy_hubs(new_hubs, sector_ids)

    def points(self):
        points = []
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row, col] != 0:
                    points.append([row, col])
        return points

    def move(self, hub):
        if context.balance < self.move_cost:
            return
        context.balance -= self.move_cost

        centroids = centroid_locator(self.points(), 0.15, 3)

        coord = centroids[0]
        sector_id = coord[0] * self.cols + coord[1]

        self.zero([coord])
        api.move_hubs([hub['hub_id']], [sector_id])

    def zero(self, coords):
        for coord in coords:
            self.map[coord[0]-1, coord[1]+1] = 0
            self.map[coord[0]-1, coord[1]-1] = 0
            self.map[coord[0]-1, coord[1]] = 0
            self.map[coord[0], coord[1]+1] = 0
            self.map[coord[0], coord[1]-1] = 0
            self.map[coord[0]+1, coord[1]+1] = 0
            self.map[coord[0]+1, coord[1]-1] = 0
            self.map[coord[0]+1, coord[1]] = 0

    def ship(self, hub, insure):
        if context.balance < self.ship_cost:
            return
        context.balance -= self.ship_cost

        api.ship_ore([hub], insured=insure)

