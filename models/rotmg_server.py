
server_name_conversions = {
    "USWest4": "USW4",
    "USWest3": "USW3",
    "USWest2": "USW2",
    "USWest": "USW",
    "USSouthWest": "USSW",
    "USSouth3": "USS3",
    "USSouth2": "USS2",
    "USSouth": "USS",
    "USNorthWest": "USNW",
    "USMidWest2": "USMW2",
    "USMidWest": "USMW",
    "USEast4": "USE4",
    "USEast3": "USE3",
    "USEast2": "USE2",
    "USEast": "USE",
    "EUWest2": "EUW2",
    "EUWest": "EUW",
    "EUSouthWest": "EUSW",
    "EUSouth": "EUS",
    "EUNorth2": "EUN2",
    "EUNorth": "EUN",
    "EUEast2": "EUE2",
    "EUEast": "EUE",
    "Australia": "AUS",
    "AsiaSouthEast": "ASE",
    "AsiaEast": "AE"
}


class Server():
    def __init__(self, server: str, realm: str, current_event: str, player_count: int, remaining: int, last_updated: str):
        self.server = self._format_server_name(server)
        self.realm = realm
        self.current_event = current_event
        self.player_count = player_count
        self.remaining = remaining
        self.last_updated = last_updated

    def _format_server_name(self, server):
        """Formats server as abbreviation for user readability e.g. AsiaEast -> AE. If the supplied server name is already
        abbreviated, then it is returned. If the supplied server name is not recognized as a server name or server abbreviation, 
        then a KeyError is raised"""
        try:
            return server_name_conversions[server]
        except KeyError:
            if server in server_name_conversions.values():
                return server
            raise KeyError

    def __eq__(self, other):
        """ Two rotmg_server's are equal if and only if they have the same realm in the same game server"""
        if isinstance(other, Server):
            return self.server == other.server and self.realm == other.realm
        return False

    def __repr__(self):
        """ Represents essential server information for printing in a table format"""
        return '{:<6} {:<10} {:<25} {:>2} remaining {:>3} players {:<5}'.format(self.server, self.realm, self.current_event, self.remaining, self.player_count, self.last_updated)

    def formated(self):
        pass
