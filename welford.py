"""
Online Variance with Welfords method.

Computes the variance of a dataset by incrementally adding values to an accumulator.
Welfords method is more numerically stable than the standard method.

Welfords method goes back to a 1962 paper by B. P. Welford and is presented in
Donald Knuth's Art of Computer Programming, Vol 2.

This implemenation is modelled after the following acticles:
    * Accurately computing running variance: www.johndcook.com/blog/standard_deviation
    * Computing skewness and kurtosis in one pass: www.johndcook.com/blog/skewness_kurtosis
"""

import math
from collections.abc import Iterable

class Welford():
    """Accumulator object for Welfords online variance algorithm."""

    def __init__(self, data=None):
        """Initialize with an optional data. Data can be a scalar value or an iterable of values."""
        self.__count = 0
        self.__m1 = 0.0     # mean
        self.__m2 = 0.0     # sum of squared differences from the mean
        if data is not None:
            if isinstance(data, Iterable):
                self.add_all(data)
            else:
                self.add(data)

    def __repr__(self):
        """Return a nice representation of the accumulator object."""
        return("({0}, {1}, {2})".format(self.__count, self.__m1, self.__m2))

    @property
    def acc(self):
        """Return the accumulator as a 3-tuple of count, mean and sum of squared differences from the mean"""
        return (self.__count, self.__m1, self.__m2)

    @property
    def count(self):
        """The number of recorded values"""
        return self.__count

    @property
    def mean(self):
        """Mean of the recorded values"""
        return self.__m1

    @property
    def var(self):
        """Sample variance of the recorded values"""
        if self.__count < 2:
            return float('nan')
        else:
            return self.__m2 / (self.__count - 1)

    @property
    def varp(self):
        """Population variance of the recorded values"""
        if self.__count < 2:
            return float('nan')
        else:
            return self.__m2 / self.__count

    @property
    def std(self):
        """Standard deviation based on sample variance"""
        return math.sqrt(self.var)

    @property
    def stdp(self):
        """Standard deviation based on population variance"""
        return math.sqrt(self.varp)

    def add(self, elem):
        """Add an element. Element can be a scalar value or an instance of this class."""
        if isinstance(elem, Welford):
            self.merge(elem)
        else:
            self.__count += 1
            delta = elem - self.__m1
            self.__m1 += delta / self.__count
            self.__m2 += delta * (elem - self.__m1)
        return self

    def add_all(self, iterable):
        """Adds all values from iterable."""
        for elem in iterable:
            self.add(elem)
        return self

    def merge(self, other):
        """Merge this accumulator with another one."""
        count = self.__count + other.__count
        delta = self.__m1 - other.__m1
        delta2 = delta*delta
        m1 = (self.__count * self.__m1 + other.__count * other.__m1) / count
        m2 = self.__m2 + other.__m2 + delta2 * (self.__count * other.__count) / count
        self.__count = count
        self.__m1 = m1
        self.__m2 = m2
        return self
