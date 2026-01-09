from abc import ABC, abstractmethod

class AbstractApiClient(ABC):

    @abstractmethod
    def _get(self, **kwargs):
        ...

    @abstractmethod
    def _post(self, **kwargs):
        ...

    @abstractmethod
    def _put(self, **kwargs):
        ...

    @abstractmethod
    def _delete(self, **kwargs):
        ...