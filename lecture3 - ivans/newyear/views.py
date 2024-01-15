import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    # now = datetime.datetime(2023,1,1)
    return render(
        request, "newyear/index.html", {
            "newyear": now.month == 1 and now.day == 1
            }
    )
