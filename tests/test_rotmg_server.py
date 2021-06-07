import unittest
from models.rotmg_server import Server


class TestRotmgServer(unittest.TestCase):
    def testInit(self):
        server = Server('USW4','a','a',1,1,'00:00 UTC') 
        assert server.server == 'USW4'
        assert server.realm == 'a'
        assert server.current_event == 'a'
        assert server.player_count == 1
        assert server.remaining == 1
        assert server.last_updated == '00:00 UTC'

    def testEq(self):
        serverA = Server('USW4','realm','a',1,1,'00:00 UTC')
        serverB = Server('USW4','realm','b',2,2,'12:00 UTC')
        
        assert serverA == serverB

    def testServerFormating(self):
        serverA = Server('USWest4','a','a',1,1,'00:00 UTC')
        assert serverA.server == 'USW4'
    
    def testServerFormatingException(self):
        with self.assertRaises(KeyError):
            Server('badname','a','a',1,1,'00:00 UTC')
            