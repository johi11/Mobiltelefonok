from functools import total_ordering
from __future__ import annotations

@total_ordering
class Mobile:

    manufacturer: str
    __type:str
    __year: int

    def __init__(self,manufacturer:str, __type:str, __year:int=2022):
        self.manufacturer=manufacturer
        self.__type=__type
        self.__year=__year

    @property
    def type(self)->str:
        return self.__type

    @type.setter
    def type(self, value):
        self.__type=value

    @property
    def year(self)->int:
        return self.__year

    @year.setter
    def year(self, value):
        self.__year=value

    def __repr__(self)->str:
        return f"{self.manufacturer}, {self.__type},{self.__year}"

    def __str__(self)->str:
        return f"{self.manufacturer} // {self.__type} ({self.__year})"

    def __eq__(self, other:object)->bool:
        return isinstance(other, Mobile) and self.manufacturer==other.manufacturer and self.__type==other.__type and self.__year==other.__year

    def __lt__(self, other:object)->bool:
        if not isinstance(other, Mobile):
            return NotImplemented

        return (self.manufacturer, -self.__year, self.__type) < (other.manufacturer, -other.__year, other.__type)

    @staticmethod
    def before(phones:list[Mobile], year:int)->list[str]:
        result=[]
        for phone in phones:
            if phone.__year>year:
                result.apped(phone)
        return result

@total_ordering
class Phone(Mobile):
    __camera: str

    def __init__(self, manufacturer:str, __type:str, __year:int, __camera:str):
        super().__init__(manufacturer, __type, __year)
        self.__camera=__camera

    @property
    def camera(self)->str:
        return self.__camera

    @camera.setter
    def camera(self, value:str):
        self. __camera=value

    def __repr__(self)->str:
        return f"{super().__repr__()}, {self.__camera}"

    def __str__(self)->str:
        return f"{super().__str__()}: {self.__camera}"


