#
from Land import LandParams, Land
from Way import Way, WayParams
from Rat import Rat, RatParams, RatEnv

b = LandParams()
a = Land(b)
w = Way(WayParams())
a.replace_way(w, 0, 1)
a.replace_way(w, 1, 2)
a.replace_way(w, 0, 2)
# print(a.calculate_ways())


rp = RatParams
re = RatEnv(a, 0, 1)
r = Rat(rp, re)
r.walk()