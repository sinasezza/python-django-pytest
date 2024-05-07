import requests
from unittest.mock import patch, Mock, MagicMock
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "run the script in the specified directory"


    def handle(self, *args, **kwargs):
        print(f"is instance of Mock: {isinstance(MagicMock(), Mock)}")

        my_cool_mock_obj = MagicMock()
        print(f"type of my coll mock obj is : {type(my_cool_mock_obj)}")
        
        print('-' * 100)
        
        # print(f"dir of my_cool_mock_obj: {dir(my_cool_mock_obj)}")
        
        print(my_cool_mock_obj())

        my_cool_mock_obj.assert_called_once()
        
        
        