from django.shortcuts import render
from myapp.models import Activity

def activity_manage(request):
    # get all activties
    activities = Activity.objects.all()


    return render(request, 'activity_manage.html', {'activities': activities})

