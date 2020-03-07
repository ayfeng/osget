import requests

source_urls = { "kali": "https://cdimage.kali.org/kali-2020.1/kali-linux-2020.1-live-amd64.iso",
                "gparted": "https://downloads.sourceforge.net/gparted/gparted-live-1.1.0-1-amd64.iso"
              }

with open("targets", "r") as target_file:
    for os in target_file.readlines():
        target = os.strip()
        if target in source_urls:
            print("Downloading " + target + " live image...")
            url = source_urls[target]
            filename = url.split('/')[-1]

            response = requests.get(url, stream=True)
            with open(filename, "wb") as image_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        image_file.write(chunk)
        else:
            print("Could not find " + target + " in supported image list")
