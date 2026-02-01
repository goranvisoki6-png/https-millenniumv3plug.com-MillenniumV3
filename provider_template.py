from .provider_base import ProviderBase


class ProviderTemplate(ProviderBase):
    def __init__(self):
        """
        Template provider — copy this file to create new providers.
        """
        super().__init__(name="ProviderTemplate")

    def fetch(self, query):
        """
        Fetch raw data from the provider.

        Parameters:
            query (str): Search query.

        Returns:
            Any: Raw response data.
        """
        # TODO: Implement request logic
        # Example:
        # response = requests.get("https://api.example.com/search", params={"q": query})
        # return response.json()
        raise NotImplementedError

    def parse(self, data):
        """
        Parse raw provider data into structured items.

        Parameters:
            data (Any): Raw data returned by fetch().

        Returns:
            list: Parsed items.
        """
        # TODO: Convert raw data into parsed items
        # Example:
        # items = []
        # for entry in data.get("results", []):
        #     items.append({
        #         "title": entry["title"],
        #         "url": entry["stream_url"],
        #         "quality": entry.get("quality", "Unknown")
        #     })
        # return items
        raise NotImplementedError

    def build_item(self, parsed):
        """
        Build a final Kodi item from parsed data.

        Parameters:
            parsed (dict): Parsed item data.

        Returns:
            dict: Kodi-compatible item.
        """
        # TODO: Convert parsed item into Kodi item format
        # Example:
        # return {
        #     "label": parsed["title"],
        #     "path": parsed["url"],
        #     "isPlayable": True,
        #     "info": {
        #         "quality": parsed.get("quality", "Unknown")
        #     }
        # }
        raise NotImplementedError
