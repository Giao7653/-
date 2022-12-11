import re
import jwt
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from StemEncyclopedia.settings import SECRET_KEY


class VisitLimit(MiddlewareMixin):
    def process_request(self, request):
        pass


