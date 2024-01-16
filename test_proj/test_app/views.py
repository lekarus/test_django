import json

from django.core import serializers
from django.core.exceptions import BadRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from test_app.models import TestTable


def get(request):
    obj_id = request.GET.get('pk', None)
    queryset = list()
    if obj_id:
        queryset.append(get_object_or_404(TestTable, pk=obj_id))
    queryset = queryset or TestTable.objects.all()

    serialized = serializers.serialize("json", queryset)
    return HttpResponse(serialized)


@csrf_exempt
def post(requests):
    obj_values = json.loads(requests.body)
    if "description" not in obj_values.keys():
        raise BadRequest("description not provided")
    new_obj = TestTable(pk=obj_values.get("id", None), description=obj_values.get("description"))
    new_obj.save()
    return HttpResponse(f"{new_obj.pk}, {new_obj.description} was successfully saved")
