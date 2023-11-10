from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from do_CL.models import DoCL
from do_CV.models import DoCV
from .models import OrderCV, OrderCL
from users.models import Registration


@login_required
def dashboard(request):
    user_id = request.User.id
    user = get_object_or_404(Registration, user_id=user_id)
    cv_order = OrderCV.objects.all()
    cv = DoCV.objects.get(user_id=user_id)
    cl_order = OrderCL.obejects.all()
    cl = DoCL.objects.get(user_id=user_id)
    context = {
        'user': user,
        'cv_order': cv_order,
        'cv': cv,
        'cl_order': cl_order,
        'cl': cl,
    }
    return render(request, 'dashboard.html', context)
