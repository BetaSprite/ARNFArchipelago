import typing
from typing import NamedTuple, List, Dict

if typing.TYPE_CHECKING:
    import BaseClasses

    CollectionRule = typing.Callable[[BaseClasses.CollectionState, int], bool]
    ItemRule = typing.Callable[[BaseClasses.Item], bool]
else:
    CollectionRule = typing.Callable[[object], bool]
    ItemRule = typing.Callable[[object], bool]

    
class ARNFRegionData(NamedTuple):
    connecting_regions: Dict[str, CollectionRule] = {}


region_data_table: Dict[str, ARNFRegionData] = {
    "Menu": ARNFRegionData({"BreakoutOne": lambda state, player: True}),
    "BreakoutOne": ARNFRegionData({"BreakoutTwo": lambda state, player: state.has("ProgItem4", player)}),
    "BreakoutTwo": ARNFRegionData({"BreakoutThree": lambda state, player: state.has("ProgItem7", player)}),
    "BreakoutThree": ARNFRegionData({"Victory": lambda state, player: True}),
    "Victory": ARNFRegionData()
}


# def create_regions(world, player: int, active_locations):
    # menu_region = create_region(world, player, active_locations, 'Menu', None)
    # breakout_one = create_region(world, player, active_locations, LocationName.breakout_one, None)
    # breakout_two = create_region(world, player, active_locations, LocationName.breakout_two, None)
    # breakout_three = create_region(world, player, active_locations, LocationName.breakout_three, None)
    # breakout_four = create_region(world, player, active_locations, LocationName.breakout_four, None)
    
    # world.regions += [
        # menu_region,
        # breakout_one,
        # breakout_two,
        # breakout_three,
        # breakout_four
    # ]


# def connect_regions(world, player):
    # names: typing.Dict[str, int] = {}
    
    # connect(world, player, names, "Menu", LocationName.breakout_one)
    # connect(world, player, names, LocationName.breakout_one, LocationName.breakout_two)
    # connect(world, player, names, LocationName.breakout_two, LocationName.breakout_three)
    # connect(world, player, names, LocationName.breakout_three, LocationName.breakout_four)


# def create_region(world: MultiWorld, player: int, active_locations, name: str, locations=None):
    # ret = Region(name, player, world)
    # if locations:
        # for locationName in locations:
            # loc_id = active_locations.get(locationName, 0)
            # if loc_id:
                # location = ARNFLocation(player, locationName, loc_id, region)
                # ret.Locations.append(location)
    # return ret

# def add_location_to_region(world: MultiWorld, player: int, active_locations, region_name: str, location_name: str,
                           # rule: typing.Optional[typing.Callable] = None):