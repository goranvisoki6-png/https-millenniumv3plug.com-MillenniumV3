class ProviderBase:
    def __init__(self, name):
        """
        Base provider class.

        Parameters:
            name (str): Provider name.
        """
        self.name = name

    def fetch(self, query):
        """
        Fetch raw data from the provider.

        Parameters:
            query (str): Search query.

        Returns:
            Any: Raw response data.

        Raises:
            NotImplementedError: Must be implemented in subclass.
        """
        raise NotImplementedError

    def parse(self, data):
        """
        Parse raw provider data into structured items.

        Parameters:
            data (Any): Raw data returned by fetch().

        Returns:
            list: Parsed items.

        Raises:
            NotImplementedError: Must be implemented in subclass.
        """
        raise NotImplementedError

    def build_item(self, parsed):
        """
        Build a final Kodi item from parsed data.

        Parameters:
            parsed (dict): Parsed item data.

        Returns:
            dict: Kodi-compatible item.

        Raises:
            NotImplementedError: Must be implemented in subclass.
        """
        raise NotImplementedError
