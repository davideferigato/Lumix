from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseConverter(ABC):
    @abstractmethod
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert value from one unit to another."""

    @abstractmethod
    def get_supported_units(self) -> List[str]:
        """Return list of supported units for this converter."""


class ConverterRegistry:
    _converters: Dict[str, Any] = {}

    @classmethod
    def register(cls, name: str, converter_class):
        cls._converters[name] = converter_class

    @classmethod
    def get(cls, name: str):
        return cls._converters.get(name)

    @classmethod
    def list_converters(cls) -> List[str]:
        return list(cls._converters.keys())
