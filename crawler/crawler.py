


from curl_cffi import requests as cffi_requests


class IRCCCrawler:
    """
    Downloads a single web page.
    """

    def fetch_page(self, url: str) -> str:
        response = cffi_requests.get(
            url,
            timeout=60,
            impersonate="chrome124",
        )
        response.raise_for_status()
        return response.text




