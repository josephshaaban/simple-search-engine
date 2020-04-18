from crawlers import common


class TestCommon(object):
    def test_extract_sitemaps(self):
        sitemap_url = 'https://www.bbc.co.uk/sitemap.xml'
        sitemaps = common.extract_sitemaps(sitemap_url)
        for sitemap in sitemaps[:10]:
            print(sitemap)

    def test_extract_urls_from_sitemap(self):
        sitemap_url = 'https://www.bbc.co.uk/news/localnews/locations/sitemap.xml'
        urls = common.extract_urls_from_sitemap(sitemap_url)
        for url in urls[:10]:
            print(url)
