import datetime

from django.db.models import Count
from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from robots.excel import to_excel, PATH_TEMP_FILE
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


def get_robots_info(request):
    last_week = datetime.datetime.now() - datetime.timedelta(weeks=1)
    robots = (Robot.objects
              .filter(created__gt=last_week)
              .values('model', 'version')
              .annotate(rcount=Count('serial'))
              .order_by()
              )
    to_excel(robots)
    return FileResponse(open(PATH_TEMP_FILE, 'rb'))

