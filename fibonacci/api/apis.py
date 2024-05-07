from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import exceptions
from ..dynamic import fibonacci_dynamic_space_efficient


@api_view(["GET"])
def calc_fibonacci(request):
    n = int(request.GET.get("n", 0))
    return Response(fibonacci_dynamic_space_efficient(n), status=status.HTTP_200_OK)
