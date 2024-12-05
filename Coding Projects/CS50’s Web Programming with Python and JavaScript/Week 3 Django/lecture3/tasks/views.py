from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

def index(request)->render:
    """_summary_
    Render a page that displays a list of all my tasks. Here we have a list that is generated in tasks
    Args:
        request (_type_): Django requirment
    """
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["tasks"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html",{
                "form": form
            })
            
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
