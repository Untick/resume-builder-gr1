from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderCV, OrderCL
from django.contrib import messages
from .forms import OrderCVForm
from django.views import View

class OrderCVCreateView(View):
    template_name = "order_cv_form.html"

    def get(self, request, *args, **kwargs):
        form = OrderCVForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = OrderCVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success_page")
        context = {"form": form}
        return render(request, self.template_name, context)

class OrderCVUpdateView(View):
    template_name = "order_cv_form.html"

    def get(self, request, pk, *args, **kwargs):
        order_cv = OrderCV.objects.get(pk=pk)
        form = OrderCVForm(instance=order_cv)
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        order_cv = OrderCV.objects.get(pk=pk)
        form = OrderCVForm(request.POST, request.FILES, instance=order_cv)
        if form.is_valid():
            form.save()
            return redirect("success_page")  # Redirect to a success page
        context = {"form": form}
        return render(request, self.template_name, context)


class OrderCLView(View):
    def get(self, request):
        orders = OrderCL.objects.all()
        return render(
            request, "orders.html", {"orders": orders}
        )  # Replace 'orders.html' with your actual template name

    def post(self, request):
        action = request.POST.get("action")

        if request.method == "POST":
            if action == "create":
                full_name = request.POST["full_name"]
                email = request.POST["email"]
                phone = request.POST["phone"]
                job_title = request.POST["job_title"]
                company_name = request.POST["company_name"]
                experience = request.POST["experience"]
                skills = request.POST["skills"]

                # Create a new OrderCL instance
                order = OrderCL(
                    full_name=full_name,
                    email=email,
                    phone=phone,
                    job_title=job_title,
                    company_name=company_name,
                    experience=experience,
                    skills=skills,
                )
                order.save()
                messages.success(request, "Order created successfully.")
                return redirect("orders")

            elif action == "update":
                order_id = request.POST["order_id"]
                order = get_object_or_404(OrderCL, pk=order_id)
                order.full_name = request.POST["full_name"]
                order.email = request.POST["email"]
                order.phone = request.POST["phone"]
                order.job_title = request.POST["job_title"]
                order.company_name = request.POST["company_name"]
                order.experience = request.POST["experience"]
                order.skills = request.POST["skills"]
                order.save()
                messages.success(request, "Order information updated successfully.")
                return redirect("orders")

            elif action == "delete":
                order_id = request.POST["order_id"]
                order = get_object_or_404(OrderCL, pk=order_id)
                order.delete()
                messages.success(request, "Order deleted successfully.")
                return redirect("orders")
