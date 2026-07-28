from crawler.crawler import IRCCCrawler


def test_fetch_page():

    crawler = IRCCCrawler()

    url = (
        "https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada.html"
    )

    print("\nDownloading page...")

    html = crawler.fetch_page(url)

    print(f"Downloaded {len(html)} characters.")

   
    assert len(html) > 1000

    print("\nCrawler Test Passed.")