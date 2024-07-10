from ...comparison_level_library import (
    ArrayIntersectLevelBase,
    ColumnsReversedLevelBase,
    DatediffLevelBase,
    DistanceFunctionLevelBase,
    DistanceInKMLevelBase,
    ElseLevelBase,
    ExactMatchLevelBase,
    LevenshteinLevelBase,
    NullLevelBase,
    PercentageDifferenceLevelBase,
)
from ...comparison_library import (
    ArrayIntersectAtSizesBase,
    DatediffAtThresholdsBase,
    DistanceFunctionAtThresholdsBase,
    DistanceInKMAtThresholdsBase,
    ExactMatchBase,
    LevenshteinAtThresholdsBase,
)
from .yellowbrick_base import (
    YellowbrickBase,
)


# Class used to feed our comparison_library classes
class YellowbrickComparisonProperties(YellowbrickBase):
    @property
    def _exact_match_level(self):
        return exact_match_level

    @property
    def _null_level(self):
        return null_level

    @property
    def _else_level(self):
        return else_level

    @property
    def _datediff_level(self):
        return datediff_level

    @property
    def _array_intersect_level(self):
        return array_intersect_level

    @property
    def _distance_in_km_level(self):
        return distance_in_km_level

    @property
    def _levenshtein_level(self):
        return levenshtein_level


#########################
### COMPARISON LEVELS ###
#########################
class null_level(YellowbrickBase, NullLevelBase):
    pass


class exact_match_level(YellowbrickBase, ExactMatchLevelBase):
    pass


class else_level(YellowbrickBase, ElseLevelBase):
    pass


class columns_reversed_level(YellowbrickBase, ColumnsReversedLevelBase):
    pass


class distance_function_level(YellowbrickBase, DistanceFunctionLevelBase):
    pass


class levenshtein_level(YellowbrickBase, LevenshteinLevelBase):
    pass


class array_intersect_level(YellowbrickBase, ArrayIntersectLevelBase):
    pass


class percentage_difference_level(YellowbrickBase, PercentageDifferenceLevelBase):
    pass


class distance_in_km_level(YellowbrickBase, DistanceInKMLevelBase):
    pass


class datediff_level(YellowbrickBase, DatediffLevelBase):
    pass


##########################
### COMPARISON LIBRARY ###
##########################
class exact_match(YellowbrickComparisonProperties, ExactMatchBase):
    pass


class distance_function_at_thresholds(
    YellowbrickComparisonProperties, DistanceFunctionAtThresholdsBase
):
    @property
    def _distance_level(self):
        return distance_function_level


class levenshtein_at_thresholds(
    YellowbrickComparisonProperties, LevenshteinAtThresholdsBase
):
    @property
    def _distance_level(self):
        return levenshtein_level


class array_intersect_at_sizes(YellowbrickComparisonProperties, ArrayIntersectAtSizesBase):
    pass


class datediff_at_thresholds(YellowbrickComparisonProperties, DatediffAtThresholdsBase):
    pass


class distance_in_km_at_thresholds(
    YellowbrickComparisonProperties, DistanceInKMAtThresholdsBase
):
    pass


###################################
### COMPARISON TEMPLATE LIBRARY ###
###################################
# Not yet implemented
# Currently does not support the necessary comparison levels
# required for existing comparison templates
