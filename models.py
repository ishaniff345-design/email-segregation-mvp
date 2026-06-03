"""
Data models for email classification and extraction.
"""

from typing import Optional, Dict, Any
from dataclasses import dataclass, asdict


@dataclass
class TonnageData:
    """Fields extracted from Tonnage (Open Vessel) emails."""
    vessel_name: Optional[str] = None
    account_name: Optional[str] = None
    open_port: Optional[str] = None
    open_date: Optional[str] = None
    vessel_type: Optional[str] = None
    vessel_size: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values."""
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class CargoVCData:
    """Fields extracted from Cargo VC (Voyage Charter) emails."""
    account_name: Optional[str] = None
    cargo_name: Optional[str] = None
    loading_port: Optional[str] = None
    discharge_port: Optional[str] = None
    laycan: Optional[str] = None
    cargo_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values."""
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class CargoTCData:
    """Fields extracted from Cargo TC (Time Charter) emails."""
    account_name: Optional[str] = None
    cargo_name: Optional[str] = None
    delivery_port: Optional[str] = None
    redelivery_port: Optional[str] = None
    duration: Optional[str] = None
    laycan: Optional[str] = None
    cargo_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values."""
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class ExtractionResult:
    """Complete result of email classification and extraction."""
    category: str  # 'tonnage', 'cargo_vc', 'cargo_tc', or 'unknown'
    confidence: float  # 0.0 to 1.0
    data: Dict[str, Any]  # extracted fields

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON response."""
        return {
            "category": self.category,
            "confidence": round(self.confidence, 2),
            "data": self.data
        }
