from abc import ABC, abstractmethod

class Measurement(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def init(self) -> bool :
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def send_message(self, measurement , data: str):
        pass