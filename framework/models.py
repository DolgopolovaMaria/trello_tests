from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass(frozen=True)
class BoardData:
    id: str
    name: str
    url: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass(frozen=True)
class ListData:
    id: str
    name: str
    idBoard: str = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass(frozen=True)
class CardData:
    id: str
    name: str
    idList: str = None
