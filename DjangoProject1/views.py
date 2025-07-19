from django.shortcuts import render

def jobapp(request):
    return render(request, "job_application.html")


def include(request):
    return None