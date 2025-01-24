from django.http import JsonResponse
from django.views import View
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections
from todo.search_indexes import TodoIndex


class TodoSearchView(View):
    def get(self, request):
        query = request.GET.get("q", "")  # Get the search term from query params
        if not query:
            return JsonResponse({"error": "Search query is required"}, status=400)

        # Elasticsearch query
        client = connections.get_connection()
        s = Search(using=client, index=TodoIndex.Index.name).query(
            "multi_match",
            query=query,
            fields=["title", "description"],
            fuzziness="AUTO",
        )

        # Execute search
        response = s.execute()
        results = [
            {"id": hit.meta.id, "title": hit.title, "description": hit.description}
            for hit in response
        ]

        return JsonResponse({"results": results})
