import math
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

def distance(p1: Point, p2: Point) -> float:
    return math.hypot(p2.x - p1.x, p2.y - p1.y)
