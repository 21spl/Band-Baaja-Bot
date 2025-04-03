from smolagents import Tool
from typing import Any, Optional

class SimpleTool(Tool):
    name = "suggest_menu"
    description = "Suggests a wedding menu based on the type of Indian wedding."
    inputs = {'shaadi_type': {'type': 'string', 'description': 'The type of Indian wedding.'}}
    output_type = "string"

    def forward(self, shaadi_type: str) -> str:
        """
        Suggests a wedding menu based on the type of Indian wedding.
        Args:
            shaadi_type: The type of Indian wedding.
        Returns:
            A string containing the suggested menu.
        """
        if shaadi_type == "Bengali":
            return "Shorshe Ilish, Chingri Malai Curry, Mishti Doi, Kosha Mangsho, Luchi, and Rasgulla."
        elif shaadi_type == "Punjabi":
            return "Butter Chicken, Sarson da Saag & Makki di Roti, Chole Bhature, Amritsari Fish, and Lassi."
        elif shaadi_type == "Marathi":
            return "Puran Poli, Misal Pav, Batata Vada, Modak, and Bharli Vangi."
        elif shaadi_type == "South Indian":
            return "Dosa, Idli, Sambar, Bisi Bele Bath, Payasam, and Filter Coffee."
        elif shaadi_type == "Gujarati":
            return "Dhokla, Thepla, Undhiyu, Fafda-Jalebi, and Kadhi-Khichdi."
        elif shaadi_type == "Rajasthani":
            return "Dal Baati Churma, Gatte ki Sabzi, Ker Sangri, Laal Maas, and Ghewar."
        elif shaadi_type == "Kashmiri":
            return "Rogan Josh, Yakhni, Dum Aloo, Modur Pulao, and Kahwa."
        elif shaadi_type == "Bihari":
            return "Litti Chokha, Sattu Paratha, Thekua, Dal Pitha, and Khaja."
        else:
            return "Sorry, we don't have menu suggestions for this type of wedding."