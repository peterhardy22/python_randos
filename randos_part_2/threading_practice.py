import concurrent.futures
import requests
import time

def get_status(url):
    print(f"Getting status of {url}")
    start_time = time.monotonic()
    response = requests.get(url)
    total_time = time.monotonic() - start_time
    print(f"Finished getting status of {url} in {total_time:.2f} seconds")
    return url, response.status_code

urls: list = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.github.com",
    "https://www.linkedin.com"
]

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    futures: list = []
    for url in urls:
        future = executor.submit(get_status, url)
        futures.append(future)
    
    for future in concurrent.futures.as_completed(futures):
        try:
            url, status_code = future.result()
            print(f"Status code for {url} is {status_code}")
        except Exception as err:
            print(f"Task failed: {err}")