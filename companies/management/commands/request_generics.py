import json
import requests
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Make a request to a specified GENERIC URL"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str, help="The URL to request")

    def handle(self, *args, **kwargs):
        url = kwargs["url"]
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            self.stdout.write(
                self.style.SUCCESS(f"Successfully made a request to {url}")
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"response content is {json.loads(response.content)}"
                )
            )
        except requests.RequestException as e:
            self.stderr.write(self.style.ERROR(f"Error making a request to {url}: {e}"))
