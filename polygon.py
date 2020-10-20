import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices')

        self._n = n
        self._R = R

        #caching properties
        self._interior_angle = None
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None


    def __repr__(self):
        return f"Polygon(n = {self._n}, R={self._R})"

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._R
    # make these lazy properties so not calculated until requested
    # then cache the values Using class variable
    @property
    def interior_angle(self):
        if self.interior_angle is None:
            self.interior_angle = (self._n - 2) * 180 /self._n
        return self.interior_angle


    @property
    def side_length(self):
        if self._side_length is None:
            self._side_length = 2 * self._R * math.sin(math.pi / self._n)
        return self._side_length

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._R * math.cos(math.pi / self._n)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area= self._n / 2 * self.side_length * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self._n * self.side_length
        return self._perimeter

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return(self.count_edges == other.count_edges
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented


    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_edges > other.count_edges

        else:
            return NotImplemented
