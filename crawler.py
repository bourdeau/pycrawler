from urllib.parse import urlparse
from client import Client
from bs4 import BeautifulSoup
from models import Domain, Url
from mongoengine import DoesNotExist


class Crawler():

    def _get_page_html(self, domain: Domain):
        client = Client()
        url = '{}://{}'.format(domain.scheme, domain.netloc)
        html = client.request(url)

        return html

    def _find_links(self, domain: Domain):
        data = self._get_page_html(domain)
        html = BeautifulSoup(data, 'lxml')

        results = []

        for link in html.find_all('a'):
            href = link.get('href')
            # We only store absolute URL @todo store relative
            if isinstance(href, str) and href.startswith('http'):
                href = href.strip()
                if href not in results:
                    results.append(href)

        self._save(results)

    def _save(self, results):

        for href in results:
            uri = urlparse(href)

            try:
                domain = Domain.objects.get(netloc=uri.netloc)
            except DoesNotExist as e:
                domain = Domain(scheme=uri.scheme, netloc=uri.netloc)

            path = uri.path
            if not path:
                path = '/'

            url = Url(path=path)
            domain.urls.append(url)
            domain.save()

    def run(self):
            # Fixtures
            if Domain.objects.count() == 0:
                domain = Domain(scheme='http', netloc='sametmax.com')
                url = Url(path='/')
                domain.urls.append(url)
                domain.save()

            for domain in Domain.objects:
                self._find_links(domain)


if __name__ == "__main__":
    crawler = Crawler()
    crawler.run()
