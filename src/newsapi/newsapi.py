import requests
import traceback
from urllib import parse

EVERYTHING_API_BASE_URL = "https://newsapi.org/v2/everything"
TOP_HEADLINES_API_BASE_URL = "https://newsapi.org/v2/top-headlines"


class NewsAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def get_top_headlines(
        self,
        query=None,
        country=None,
        category=None,
        sources=None,
        page_size=None,
        page=None,
    ):

        params = {}
        if query:
            params["q"] = query
        if country:
            params["country"] = country
        if category:
            params["category"] = category
        if sources:
            params["sources"] = sources
        if page_size:
            # Note: News API uses 'pageSize' (camelCase)
            params["pageSize"] = page_size
        if page:
            params["page"] = page
        params["apiKey"] = self.api_key
        try:
            query_string = parse.urlencode(params)
            base_url = f"{TOP_HEADLINES_API_BASE_URL}?{query_string}"
        except Exception as exc:
            traceback.print_exc()
            raise exc
        try:
            response = requests.get(base_url)
            return response
        except Exception as exc:
            traceback.print_exc()
            raise exc

    async def get_everything(
        self,
        query=None,
        search_in=None,
        sources=None,
        domains=None,
        exclude_domains=None,
        from_date=None,
        to_date=None,
        language=None,
        sortBy=None,
        pageSize=None,
        page=None,
    ):

        params = {}
        if query:
            params["q"] = query
        if search_in:
            # Note: News API uses 'pageSize' (camelCase)
            params["searchIn"] = search_in
        if sources:
            params["sources"] = sources
        if domains:
            params["domains"] = domains
        if exclude_domains:
            params["exclude_domains"] = exclude_domains
        if from_date:
            params["from_date"] = from_date
        if to_date:
            params["to_date"] = to_date
        if language:
            params["language"] = language
        if sortBy:
            params["sortBy"] = sortBy
        if pageSize:
            params["pageSize"] = pageSize
        if page:
            params["page"] = page
        params["apiKey"] = self.api_key

        try:
            query_string = parse.urlencode(params)
            base_url = f"{EVERYTHING_API_BASE_URL}?{query_string}"
        except Exception as exc:
            traceback.print_exc()
            raise exc
        try:
            response = requests.get(base_url)
        except Exception as exc:
            traceback.print_exc()
            raise exc
        return response
