from dataclasses import dataclass


@dataclass
class AverageRatingDTO:
    value: float
    num_ratings: int
