from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass(frozen=True)
class BoardData:
    id: str
    name: str
    url: str
