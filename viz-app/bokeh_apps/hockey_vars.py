BASE_URL = 'https://statsapi.web.nhl.com/api/v1/'

TEAM_COLORS_DICT = {
    'Anaheim Ducks': '#FC4C02',
    'Arizona Coyotes': '#89222F',
    'Boston Bruins': '#FDB927',
    'Buffalo Sabres': '#002D62',
    'Calgary Flames': '#D42604',
    'Carolina Hurricanes': '#E13A3E',
    'Chicago Blackhawks': '#D1001B',
    'Colorado Avalanche': '#8B2942',
    'Columbus Blue Jackets': '#01265B',
    'Dallas Stars': '#006341',
    'Detroit Red Wings': '#C8102E',
    'Edmonton Oilers': '#CF4520',
    'Florida Panthers': '#B9975B',
    'Los Angeles Kings': '#000000',
    'Minnesota Wild': '#015836',
    'Montréal Canadiens': '#A6192E',
    'Nashville Predators': '#FBBD2C',
    'New Jersey Devils': '#C8102E',
    'New York Islanders': '#003087',
    'New York Rangers': '#0039A6',
    'Ottawa Senators': '#E4173E',
    'Philadelphia Flyers': '#FD4300',
    'Pittsburgh Penguins': '#FFC80C',
    'San Jose Sharks': '#006E7F',
    'St. Louis Blues': '#0447A0',
    'Tampa Bay Lightning': '#003E7E',
    'Toronto Maple Leafs': '#003876',
    'Vancouver Canucks': '#002E56',
    'Vegas Golden Knights': 'darkgoldenrod',
    'Washington Capitals': '#CF132B',
    'Winnipeg Jets': '#A8A9AD'
}

TOOLTIPS = [
    ("Name", "@name"),
    ("Team", "@team"),
    ("SV%", "@savePercentage"),
    ("GAA", "@goalAgainstAverage")
]

ES_TOOLTIPS = [
    ("Name", "@name"),
    ("Team", "@team"),
    ("SV%", "@evenStrengthSavePercentage"),
    ("GAA", "@goalAgainstAverage")
]
SH_TOOLTIPS = [
    ("Name", "@name"),
    ("Team", "@team"),
    ("SV%", "@shortHandedSavePercentage"),
    ("GAA", "@goalAgainstAverage")
]
PP_TOOLTIPS = [
    ("Name", "@name"),
    ("Team", "@team"),
    ("SV%", "@powerPlaySavePercentage"),
    ("GAA", "@goalAgainstAverage")
]

TOOLS = "box_select,lasso_select"
