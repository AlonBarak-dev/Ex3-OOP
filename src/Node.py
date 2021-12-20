from src.GeoLocation import GeoLocation
from src.Links import Links


class Node(object):
    """
    This class represent a vertex in a graph.
    """

    def __init__(self, pos: GeoLocation = None, key: int = None):
        """
        a constructor for the Node class.
        :param pos: GeoLocation of the Node.
        :param key: the ID of the Node
        """

        self.key: int = key
        self.pos: GeoLocation = pos
        self.tag: int = 0
        self.edges_in = {}
        self.edges_out = {}
        self.weight: float = 0.0
        self.info: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> 'Node':
        """
        this method creates a Node from a dictionary.
        :param data: Data dict
        :return: Node
        """

        # check for None values and raise exception
        # if 'id' not in data or 'key' not in data:
        #     raise ValueError("Cant create a Node without id and data")
        key: int = data.get('id')  # initialize the node ID


        # initialize the node location
        pos = data.get('pos')
        if pos is not None:
            pos = GeoLocation(*pos.split(','))  # create new GeoLocation

        node: Node = Node(pos, key)

        return node

    def to_dict(self) -> dict:
        """
        this method return a dict representing the Node
        :return: dict with the Node values
        """
        dic = {
            'pos': self.pos.__repr__(),
            'id': self.key
        }
        return dic

    def get_geoLocation(self) -> GeoLocation:
        """
        return the position of the Node
        :return: GeoLocation object
        """
        return self.pos

    def set_geoLocation(self, geo: GeoLocation):
        """
        set the position of the Node to a new position
        :param geo: GeoLocation object
        """
        if not isinstance(geo, GeoLocation):
            raise ValueError("should be GeoLocation type")
        self.pos = geo

    def set_edges_dict(self, edges: dict):
        """
        set the edges dict to a new edges dict
        """
        if Links.IN not in edges or Links.OUT not in edges:
            raise ValueError("missing values")
        self.edges_in = edges.get('EDGES_IN')
        self.edges_out = edges.get('EDGES_OUT')

    def get_key(self) -> int:
        return self.key

    def get_pos(self) -> GeoLocation:
        return self.pos

    def __repr__(self):
        return "{}: |edges out| {} |edges in| {}".format(self.key, len(self.edges_out), len(self.edges_in))
