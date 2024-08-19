import scrapy  #type: ignore
import requests #type: ignore

def get_web(site) -> str :
    try:
        response = requests.get(site,timeout=5)
        print(response.content)
    except Exception as e:
        print(f"Failed to Connect to {site}")
        pass

get_web("https://www.amazon.com")

