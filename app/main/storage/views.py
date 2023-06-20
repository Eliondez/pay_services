from django.http import HttpResponse
from django.shortcuts import render

from .models import Document


def upload_test_view(request):
    docs = Document.objects.all()
    for i in docs:
        print('true_link', i.true_link)
    return render(request, 'upload_template.html', {'docs': docs})


def get_protected_file(request):
    document = Document.objects.first()
    response = HttpResponse()
    response["Content-Disposition"] = "attachment; filename={0}".format(
        document.file.name)
    hdr = "/media/{0}".format(document.file.name)
    print('document.file.name', document.file.name)
    print('hdr', hdr)
    response['X-Accel-Redirect'] = hdr
    return response
