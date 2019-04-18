from django.shortcuts import render
from django.http import JsonResponse

from .models import  Articles
from .serializers import ArticleSerializer

from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    rest_list = Articles.objects.order_by('-datePub')
    context = {'rest_list': rest_list}
    return render(request, 'index.html', context)


@csrf_exempt
def get_rest_list(request):
    if request.method == "GET":
        rest_list = Articles.objects.order_by('-datePub')
        serializer = ArticleSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)
