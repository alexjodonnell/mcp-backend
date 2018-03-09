import numpy as np


class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.map = np.zeros(rows*cols)
        self.types = np.chararray(rows*cols)

    def append(self, prospect_map):
        for sector_id, ore_type, estimated_tonnes in prospect_map:
            self.map[sector_id] = estimated_tonnes
            self.types[sector_id] = ore_type
