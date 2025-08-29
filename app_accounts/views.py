from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register_account(request):

    response = None

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")  # "1" на конце
            user = authenticate(username=username, password=password)
            login(request, user)
            response = HttpResponseRedirect(
                redirect_to=reverse("app_counter:index")
            )

        else:
            response = render(
                request=request,
                template_name="app_accounts/register_account.html",
                context={
                    "form": form
                }
            )

    else:
        form = UserCreationForm()
        response = render(
            request=request,
            template_name="app_accounts/register_account.html",
            context={
                "form": form
            }
        )

    return response
