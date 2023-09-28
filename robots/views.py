
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from robots.models import Robot
from robots.validator import data_is_valid


@require_POST
@csrf_exempt
def insert(request):
    try:
        model = request.POST.get('model')
        version = request.POST.get('version')
        created = request.POST.get('created')
    except KeyError:
        return HttpResponse(status=400)
    if data_is_valid(model, version, created):
        Robot.objects.get_or_create(serial=f"{model}-{version}",
                                    model=model,
                                    version=version,
                                    created=created
                                    )
        return HttpResponse(status=200)
    return HttpResponse(status=400)


