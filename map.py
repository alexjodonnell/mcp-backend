import numpy as np

import api
from utils import convert_to_week, delay_until


class Map:
    def __init__(self, start_epoch, ms_per_week, build_weeks, rows, cols):
        self.rows = rows
        self.cols = cols
        self.map = np.zeros([rows, cols])
        self.types = np.chararray([rows, cols])

        self.hubs = {}

        self.start_epoch = start_epoch
        self.ms_per_week = ms_per_week
        self.build_weeeks = build_weeks

    def append(self, prospect_map):
        for sector_id, ore_type, estimated_tonnes in prospect_map:
            row, col = divmod(sector_id, self.cols)

            self.map[row][col] = estimated_tonnes
            self.types[row][col] = ore_type

    def mine(self, coords):
        sector_ids = [coord[0] * self.cols + coord[1] for coord in coords]

        new_hubs = ['H{}'.format(sector_id) for sector_id in sector_ids]
        api.build_hubs(new_hubs)

        status_report = api.status_report()
        orders = status_report['orders']
        build_time = orders[new_hubs[0]]['start_time']
        current_week = convert_to_week(build_time, self.start_epoch, self.ms_per_week)
        delay_until(self.start_epoch, current_week + self.build_weeeks, self.ms_per_week)
        api.deploy_hubs(new_hubs, sector_ids)

        for new_hub, sector_id in zip(new_hubs, sector_ids):
            self.hubs[new_hub] = sector_id

    def points(self):
        points = []
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row, col] != 0:
                    points.append([row, col])
        return points

