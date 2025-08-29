from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from app_counter.models import Counter


def index(request):

    counters = Counter.objects.all()

    return render(
        request=request,
        template_name="app_counter/index.html",
        context={
            "counters": counters
        }
    )


@login_required
def counter(request):
    try:
        counter = request.user.counter
    except Counter.DoesNotExist:
        counter = None

    return render(
        request=request,
        template_name="app_counter/counter.html",
        context={"counter": counter}
    )


@login_required
def create_counter(request):
    try:
        request.user.counter  # проверяем наличие счетчика и try/except - более профессиональный и надежный подход!
    except Counter.DoesNotExist:
        Counter.objects.create(user=request.user, value=0)

    return HttpResponseRedirect(reverse("app_counter:counter"))






@login_required
def increase_counter(request):

    Counter.objects.filter(user=request.user).update(value=F('value') + 1)

    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))


@login_required
def decrease_counter(request):

    Counter.objects.filter(user=request.user).update(value=F('value') - 1)

    return HttpResponseRedirect(redirect_to=reverse("app_counter:counter"))

