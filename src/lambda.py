import json
import scraper


def handler(event, context):
    proxies = scraper.free_proxies()
    return {
        "statusCode": 200,
        "body": json.dumps(proxies),
    }