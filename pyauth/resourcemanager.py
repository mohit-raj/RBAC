from typing import List, Union


class ResourceManager:
    def __init__(self, resources: List[str] = []) -> None:
        self.resources = set(resources)

    def get_resources(self) -> List[str]:
        return self.resources.copy()

    def add_resources(self, new_resource: Union[str, List[str]]) -> None:
        self.resources.update(new_resource)

    def remove_resources(self, del_resource: Union[str, List[str]]) -> None:
        if type(del_resource) is list:
            for resource in del_resource:
                self.resources.discard(resource)
        else:
            self.resources.discard(del_resource)
