from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def calculate_performance(self):
        pass

    def __del__(self):
        print(f"[CLEANUP] Person {self.name} deleted")
