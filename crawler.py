from urllib.parse import urlparse
from client import Client
from bs4 import BeautifulSoup
from models import Domain


class Crawler():

    def _get_page_html(self, domain: Domain):
        client = Client()
        url = '{}://{}'.format(domain.scheme, domain.netloc)
        html = client.request(url)

        return html

    def _find_links(self, domain: Domain):
        data = self._get_page_html(domain)
        html = BeautifulSoup(data, 'lxml')

        for link in html.find_all('a'):
            href = link.get('href')
            if isinstance(href, str) and href.startswith('http'):
                uri = urlparse(href.strip())

                if not Domain.objects(netloc=uri.netloc):
                    Domain(scheme=uri.scheme, netloc=uri.netloc).save()

    def run(self):
            if Domain.objects.count() == 0:
                Domain(scheme='https', netloc='sametmax.com').save()

            for domain in Domain.objects:
                self._find_links(domain)


if __name__ == "__main__":
    crawler = Crawler()
    crawler.run()
