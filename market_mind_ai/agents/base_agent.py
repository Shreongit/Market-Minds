from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseAgent(ABC):
    """
    Abstract Base Class for all MarketMind AI Agents.
    Enforces strict Pydantic inputs and outputs for complete decoupling.
    """
    
    def __init__(self, agent_name: str):
        self.agent_name = agent_name

    @abstractmethod
    def analyze(self, ticker: str, **kwargs) -> Any:
        """
        Execute analysis for a given ticker or context and return typed Pydantic output model.
        """
        pass
