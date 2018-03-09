from urllib import request
import numpy as np


class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.map = np.zeros(rows*cols)
        self.types = np.chararray(rows*cols)

    def append(self, prospect_map):
        for sector_id, ore_type, estimated_tonnes in prospect_map:
            if estimated_tonnes == 0:
                continue

            self.map[sector_id] = estimated_tonnes
            self.types[sector_id] = ore_type

            #TODO: UPDATE URL
            request.post("http://localhost:3000/dashboard/map", data={'prospect_map': prospect_map, 'rows': self.rows,
                                                                      'cols': self.cols})

