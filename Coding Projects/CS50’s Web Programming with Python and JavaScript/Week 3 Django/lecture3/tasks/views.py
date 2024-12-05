from django.shortcuts import render

# Create your views here.

#sample tasks
tasks = ["foo","bar","baz"]

def index(request)->render:
    """_summary_
    Render a page that displays a list of all my tasks. Here we have a list that is generated in tasks
    Args:
        request (_type_): Django requirment
    """
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
