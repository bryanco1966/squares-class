class PolygonIterator:
    def init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        if R < 0:
            raise ValueError('R cannot be negative')
        self._m  = m
        self. _R = R
        self._i = 3

    def __inter__(self):
        return self

    def __next__(self):
        if self._i > self._m:
            raise StopIteration

        else:
            result = Polygon(self._i, self._R)
            self._i += 1
            return result








class Polygons:
    def init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        if R < 0:
            raise ValueError('R cannot be negative')
        self._m  = m
        self. _R = R


        def __len__(self):
            return self._m-2

        def __repr__(self):
            return f"Polygons(m={self._m}, R={self._R})"

        def __iter__(self):
            return PolygonIterator(self._m, self._R)

        @property
        def max_efficiency_polygon(self):
            sorted_polygons= sorted(PolygonIterator(self._m,self._R),
                                    key=lambda p: p.area/p.perimeter,
                                    reverse = True)
            return sorted_polygons[0]
