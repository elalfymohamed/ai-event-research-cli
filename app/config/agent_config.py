# Standard library
from dataclasses import dataclass

#
@dataclass
class AgentConfig:
    model: str = "gemini-2.5-pro"  # gemini-2.5-flash  |  gemini-2.5-pro | gemini-2.5-flash-preview-04-17
    temperature: float =0.4
    top_p: float =1.0
    top_k: int =1
    max_output_tokens: int | None = None
