# Standard library
from dataclasses import dataclass

#
@dataclass
class AgentConfig:
    model: str = "llama3.2"
    temperature: float =0.2
    top_p: float =1.0
    top_k: int =1
