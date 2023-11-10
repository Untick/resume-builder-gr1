from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from do_order.models import OrderCL
from .models import DoCL


@login_required
def create_cl(request):
    user_id = request.user.id
    if request.method == 'POST':
        action = request.POST.get('action', '')
        order = OrderCL.objects.filter(user_id=user_id).order_by('-created_time')[0]
        order_id = order.id
        # Create letter cover order
        if action == 'order':
            cl_order = {
                'user_id': user_id,
                'fullname': request.POST.get('fullname', ''),
                'email': request.POST.get('email', ''),
                'phone': request.POST.get('phone', ''),
                'job_title': request.POST.get('job_title', ''),
                'company_name': request.POST.get('company_name', ''),
                'experience': request.POST.get('experience', ''),
                'skills': request.POST.get('skills', ''),
            }
            clo = DoCL(**cl_order)
            clo.save()

        # Retrieve the form data from the request
        if action == 'result':
            cl_data = {
                'user_id': user_id,
                'order_id': order_id,
                'fullname': request.POST.get('fullname', ''),
                'email': request.POST.get('email', ''),
                'phone': request.POST.get('phone', ''),
                'job_title': request.POST.get('job_title', ''),
                'company_name': request.POST.get('company_name', ''),
                'experience': request.POST.get('experience', ''),
                'skills': request.POST.get('skills', ''),
            }

            cl = DoCL(**cl_data)
            cl.save()
            messages.success(request, 'The cover letter saved successfully.')
            return redirect('dashboard.html')
    context = {
        'cl': DoCL.objects.filter(user_id=user_id).order_by('-created_time')[0]
    }
    return render(request, 'create_cl.html', context)


@login_required
def update_cl(request, cl_id):
    cl = get_object_or_404(DoCL, id=cl_id)

    if request.method == 'POST':
        cl.full_name = request.POST.get('fullname', cl.full_name)
        cl.email = request.POST.get('email', cl.email)
        cl.phone = request.POST.get('phone', cl.phone)
        cl.job_title = request.POST.get('job_title', cl.job_title)
        cl.company_name = request.POST.get('company_name', cl.company_name),
        cl.experience = request.POST.get('experience', cl.experience),
        cl.skills = request.POST.get('skills', cl.skills),

        cl.save()
        messages.success(request, 'This cover letter was edited successfully.')
        return redirect('dashboard.html')
    else:
        return render(request, 'edit_cl.html', {'cl': cl})
