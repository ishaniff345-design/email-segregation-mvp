"""
Field extractor for email data extraction.
Extracts structured fields based on category and patterns.
"""

from typing import Optional, Dict, Any
from patterns import PATTERNS
from models import TonnageData, CargoVCData, CargoTCData


class FieldExtractor:
    """Extracts fields from emails based on category."""

    def __init__(self):
        """Initialize extractor with compiled patterns."""
        self.patterns = PATTERNS

    def extract_tonnage(self, email_text: str) -> TonnageData:
        """
        Extract fields from Tonnage (Open Vessel) email.
        
        Args:
            email_text: Raw email text
            
        Returns:
            TonnageData object with extracted fields
        """
        result = TonnageData()

        # Extract vessel name
        vessel_match = self.patterns['vessel_name'].search(email_text)
        if vessel_match:
            result.vessel_name = vessel_match.group('vessel').strip()

        # Extract vessel size (DWT)
        dwt_match = self.patterns['dwt'].search(email_text)
        if dwt_match:
            result.vessel_size = dwt_match.group('size').strip()
        else:
            # Try K format (e.g., 38K DWT)
            dwt_k_match = self.patterns['dwt_k'].search(email_text)
            if dwt_k_match:
                result.vessel_size = dwt_k_match.group('size').strip() + 'K'

        # Extract open port
        port_match = self.patterns['open_port'].search(email_text)
        if port_match:
            result.open_port = port_match.group('open_port').strip()

        # Extract open date
        date_oa = self.patterns['open_date_oa'].search(email_text)
        if date_oa:
            result.open_date = date_oa.group('open_date').strip()
        else:
            # Try ONW format
            date_onw = self.patterns['open_date_onw'].search(email_text)
            if date_onw:
                result.open_date = date_onw.group('open_date').strip()

        return result

    def extract_cargo_vc(self, email_text: str) -> CargoVCData:
        """
        Extract fields from Cargo VC (Voyage Charter) email.
        
        Args:
            email_text: Raw email text
            
        Returns:
            CargoVCData object with extracted fields
        """
        result = CargoVCData()

        # Extract account name
        account_match = self.patterns['account'].search(email_text)
        if account_match:
            result.account_name = account_match.group('account').strip()

        # Extract loading port
        load_match = self.patterns['load_port'].search(email_text)
        if load_match:
            result.loading_port = load_match.group('loading_port').strip()

        # Extract discharge port
        disch_match = self.patterns['discharge_port'].search(email_text)
        if disch_match:
            result.discharge_port = disch_match.group('discharge_port').strip()

        # Extract cargo quantity and name
        cargo_match = self.patterns['cargo_qty_name'].search(email_text)
        if cargo_match:
            qty = cargo_match.group('quantity').strip()
            cargo_name = cargo_match.group('cargo').strip()
            result.cargo_name = f"{qty} MTS {cargo_name}" if qty else cargo_name
        else:
            # Try alternate cargo format
            cargo_alt = self.patterns['cargo_line'].search(email_text)
            if cargo_alt:
                result.cargo_name = cargo_alt.group('cargo_line').strip()

        # Extract laycan
        laycan_match = self.patterns['laycan'].search(email_text)
        if laycan_match:
            result.laycan = laycan_match.group('laycan').strip()

        return result

    def extract_cargo_tc(self, email_text: str) -> CargoTCData:
        """
        Extract fields from Cargo TC (Time Charter) email.
        
        Args:
            email_text: Raw email text
            
        Returns:
            CargoTCData object with extracted fields
        """
        result = CargoTCData()

        # Extract account name
        account_match = self.patterns['account'].search(email_text)
        if account_match:
            result.account_name = account_match.group('account').strip()

        # Extract delivery port
        dely_match = self.patterns['delivery'].search(email_text)
        if dely_match:
            result.delivery_port = dely_match.group('delivery_port').strip()

        # Extract redelivery port
        redel_match = self.patterns['redelivery'].search(email_text)
        if redel_match:
            result.redelivery_port = redel_match.group('redelivery_port').strip()

        # Extract duration
        duration_match = self.patterns['duration'].search(email_text)
        if duration_match:
            result.duration = duration_match.group('duration').strip()

        # Extract laycan
        laycan_match = self.patterns['laycan'].search(email_text)
        if laycan_match:
            result.laycan = laycan_match.group('laycan').strip()

        return result

    def extract(self, email_text: str, category: str) -> Dict[str, Any]:
        """
        Extract fields based on email category.
        
        Args:
            email_text: Raw email text
            category: Email category ('tonnage', 'cargo_vc', 'cargo_tc')
            
        Returns:
            Dictionary of extracted fields
        """
        if category == 'tonnage':
            return self.extract_tonnage(email_text).to_dict()
        elif category == 'cargo_vc':
            return self.extract_cargo_vc(email_text).to_dict()
        elif category == 'cargo_tc':
            return self.extract_cargo_tc(email_text).to_dict()
        else:
            return {}
