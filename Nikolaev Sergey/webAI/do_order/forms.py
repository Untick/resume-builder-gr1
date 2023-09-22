from django import forms
from .models import OrderCV, OrderCL


class OrderCVForm(forms.ModelForm):
    class Meta:
        model = OrderCV
        fields = "__all__"
        widgets = {
            "fullname": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "position_sought": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "schedule": forms.TextInput(attrs={"class": "form-control"}),
            "experience_level": forms.Select(attrs={"class": "form-select"}),
            "last_job": forms.TextInput(attrs={"class": "form-control"}),
            "last_position": forms.TextInput(attrs={"class": "form-control"}),
            "tasks_at_previous_jobs": forms.Textarea(attrs={"class": "form-control"}),
            "about_me": forms.Textarea(attrs={"class": "form-control"}),
            "key_skills": forms.Textarea(attrs={"class": "form-control"}),
            "education_university": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }

    employment_type = forms.MultipleChoiceField(
        choices=[
            ("full_time", "Полная занятость"),
            ("part_time", "Частичная занятость"),
            ("remote", "Удалённая работа"),
            ("internship", "Стажировка"),
        ],
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
    )


class OrderCLForm(forms.ModelForm):
    class Meta:
        model = OrderCL
        fields = "__all__"
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "job_title": forms.TextInput(attrs={"class": "form-control"}),
            "company_name": forms.TextInput(attrs={"class": "form-control"}),
            "experience": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "skills": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }
