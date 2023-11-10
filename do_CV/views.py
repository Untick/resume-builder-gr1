from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from do_order.models import OrderCV
from .models import DoCV


@login_required
def create_cv(request):
    # Retrieve the currently authenticated user
    user_id = request.user.id
    if request.method == 'POST':
        action = request.POST.get('action', '')

        # Save the order
        if action == 'order':
            cv_order = {
                'user_id': user_id,
                'fullname': request.POST.get('fullname', ''),
                'gender': request.POST.get('gender', ''),
                'age': request.POST.get('age', 0),
                'salary': request.POST.get('salary', 0),
                'position_sought': request.POST.get('position_sought', ''),
                'city': request.POST.get('city', ''),
                'employment_type': request.POST.get('employment_type', ''),
                'schedule': request.POST.get('schedule', ''),
                'experience_level': request.POST.get('experience_level', ''),
                'last_job': request.POST.get('last_job', ''),
                'last_position': request.POST.get('last_position', ''),
                'tasks_at_previous_jobs': request.POST.get('tasks_at_previous_jobs', ''),
                'about_me': request.POST.get('about_me', ''),
                'key_skills': request.POST.get('key_skills', ''),
                'education_university': request.POST.get('education_university', ''),
            }
            cvo = DoCV(**cv_order)
            cvo.save()

        # Retrieve the form data from the request
        if action == 'result':
            order = OrderCV.objects.filter(user_id=user_id).order_by('-created_time')[0]
            order_id = order.id
            cv_data = {
                'user_id': user_id,
                'order_id': order_id,
                'fullname': request.POST.get('fullname', ''),
                'gender': request.POST.get('gender', ''),
                'age': request.POST.get('age', 0),
                'salary': request.POST.get('salary', 0),
                'position_sought': request.POST.get('position_sought', ''),
                'city': request.POST.get('city', ''),
                'employment_type': request.POST.get('employment_type', ''),
                'schedule': request.POST.get('schedule', ''),
                'experience': request.POST.get('experience_level', ''),
                'last_job': request.POST.get('last_job', ''),
                'last_position': request.POST.get('last_position', ''),
                'tasks_at_previous_jobs': request.POST.get('tasks_at_previous_jobs', ''),
                'about_me': request.POST.get('about_me', ''),
                'key_skills': request.POST.get('key_skills', ''),
                'education_university': request.POST.get('education_university', ''),
            }
            # Create a new DoCV instance and save it to the database
            cv = DoCV(**cv_data)
            cv.save()
            messages.success(request, 'CV saved successfully.')
            return redirect('dashboard.html')

    context = {
        'cv': DoCV.objects.filter(user_id=user_id).order_by('-created_time')[0]
    }
    return render(request, 'create_cv.html', context)


@login_required
def update_cv(request, cv_id):
    # Retrieve the CV to edit
    cv = get_object_or_404(DoCV, id=cv_id)

    if request.method == 'POST':
        # Update the CV with the edited data
        cv.fullname = request.POST.get('fullname', cv.fullname)
        cv.gender = request.POST.get('gender', cv.gender)
        cv.age = request.POST.get('age', cv.age)
        cv.salary = request.POST.get('salary', cv.salary)
        cv.position_sought = request.POST.get('position_sought', cv.position_sought),
        cv.city = request.POST.get('city', cv.city),
        cv.employment_type = request.POST.get('employment_type', cv.employment_type),
        cv.schedule = request.POST.get('schedule', cv.schedule),
        cv.experience_level = request.POST.get('experience_level', cv.experience_level),
        cv.last_job = request.POST.get('last_job', cv.last_job),
        cv.last_position = request.POST.get('last_position', cv.last_position),
        cv.tasks_at_previous_jobs = request.POST.get('tasks_at_previous_jobs', cv.tasks_at_previous_jobs),
        cv.about_me = request.POST.get('about_me', cv.about_me),
        cv.key_skills = request.POST.get('key_skills', cv.key_skills),
        cv.education_university = request.POST.get('education_university', cv.education_university),

        cv.save()  # Save the edited CV
        messages.success(request, 'CV edited successfully.')
        return redirect('dashboard.html')
    else:
        return render(request, 'edit_cv.html', {'cv': cv})
