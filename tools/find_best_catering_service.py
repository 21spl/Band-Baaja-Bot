from smolagents import Tool
from typing import Any, Optional

class SimpleTool(Tool):
    name = "find_best_catering_service"
    description = "Finds the best catering service in a given location using DuckDuckGo search."
    inputs = {'location': {'type': 'string', 'description': 'The city or region where the catering service is needed.'}}
    output_type = "string"

    def forward(self, location: str) -> str:
        """
        Finds the best catering service in a given location using DuckDuckGo search.
        Args:
            location: The city or region where the catering service is needed.
        Returns:
            A string with suggested catering services.
        """
        from smolagents import DuckDuckGoSearchTool
        search_tool = DuckDuckGoSearchTool()
        results = search_tool.search(query=f"Best wedding catering services in {location}")
        return results if results else f"No catering services found for {location}. Try checking online directories."