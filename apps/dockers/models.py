from dataclasses import dataclass, field
from typing import Optional, List, Dict

from datetime import datetime

@dataclass
class PullingImageDescription:

    repository: str
    tag: Optional[str] = None

@dataclass
class DockerImage:

    image_id: str
    tag: str
    created_at: datetime

    comment: Optional[str]
    size: int

    # env_var: List[str] = field(default_factory=List)
    # cmd: List[str] = field(default_factory=List)
    #
    # volumes: Optional[Dict[str, Dict]] = field(default_factory=dict)

    @staticmethod
    def of(attrs: Dict) -> 'DockerImage':
        return DockerImage(
            image_id=attrs.get('Id')
            , tag=attrs.get('RepoTags')[0]
            , created_at=attrs.get('Created')
            , comment=attrs.get('Comment')
            , size=attrs.get('Size')
        )

@dataclass
class DockerContainer:

    container_id: str
    image_id: str

    created_at: str

    state: Dict = field(default_factory=Dict)
    args: List = field(default_factory=List)

    host_config: Dict = field(default_factory=Dict)

    mount: List = field(default_factory=List)

    config: Dict = field(default_factory=Dict)
    network: Dict = field(default_factory=Dict)

    @staticmethod
    def of(attrs: Dict) -> 'DockerContainer':
        return DockerContainer(
            container_id=attrs.get('Id'),
            image_id=attrs.get('Image'),
            created_at=attrs.get('Created'),
            # created_at=datetime.fromisoformat(attrs.get('Created').split('.')[0]),
            state=attrs.get('State'),
            args=attrs.get('Args'),
            host_config=attrs.get('HostConfig'),
            mount=attrs.get('Mounts'),
            config=attrs.get('Config'),
            network=attrs.get('NetworkSettings')
        )

