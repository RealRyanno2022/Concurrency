# io_bound/synchronous.py
import requests
import time

def get_session():
    return requests.Session()

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        indicator = "J" if "jython" in url else "R"
        print(indicator, sep='', end='', flush=True)

def download_all_sites(sites):
    for url in sites:
        download_site(url)

    print()

if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    print("Starting downloads")
    start = time.time()
    download_all_sites(sites)
    duration = time.time() - start
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
