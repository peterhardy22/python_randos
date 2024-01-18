import threading
import requests
from pathlib import Path

def download_file(url: str, filename: str) -> None:
    print(f"Downloading content from {url} to {filename}")
    response: dict = requests.get(url)
    Path(filename).write_bytes(response.content)
    print(f"Finished downloading contents to {filename}")

base_url: str = "https://raw.githubusercontent.com/JacobCallahan/Understanding/master/Python/file_io"
urls = [
    f"{base_url}/binary_file",
    f"{base_url}/files.py",
    f"{base_url}/names.txt",
    f"{base_url}/new_file.txt"
]

threads_list: list = []
for url in urls:
    filename: str = f"downloads/{url.split('/')[-1]}"
    t = threading.Thread(target=download_file, args=(url, filename))
    t.start()
    threads_list.append(t)

[t.join() for t in threads_list]
