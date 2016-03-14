from google import search
import csv


SITES = (
    'convoytrucking.net',
)

START = 0
LIMIT = 100
PAGE_SIZE = 10
PAUSE_SECONDS = 2.0


def scrape_site_links(site):
    query = 'site:{}'.format(site)
    with open(u'{}.csv'.format(site), mode='wb') as f:
        writer = csv.writer(f)
        for url in search(query, stop=LIMIT, start=START, num=PAGE_SIZE, pause=PAUSE_SECONDS):
            writer.writerow([url])


for site in SITES:
    scrape_site_links(site)
