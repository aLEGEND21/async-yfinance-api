import aiohttp


class AsyncRequester:
    """A class to make asynchronous requests to the Yahoo Finance website."""

    @classmethod    
    async def get(self, url: str, base_url: str = 'https://finance.yahoo.com/'):
        """Makes a get request to the specified url path and returns the response text.

        Args:
            url (str): The url which to make the query to
            base_url (str, optional): The base url to add to the beginning of the query. Defaults
                to 'https://finance.yahoo.com/'.

        Returns:
            str: The response text from the API
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(base_url + url) as response:
                return await response.text()