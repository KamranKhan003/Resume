from django.shortcuts import redirect, HttpResponse, render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ResumeForm
from .models import Resume

# Reume Form View
class HomeView(CreateView, ListView):

    model = Resume
    context_object_name = 'condidates'

    form_class = ResumeForm
    template_name = 'uploader/home.html'
    success_url = '/'

# Candidate Detail List View
class UserDetailView(DetailView):

    model = Resume
    template_name = 'uploader/details.html'
    context_object_name = 'detail'

# Delete Candidate
def delete(request, id):
    if request.method == 'POST':
        Resume.objects.get(id=id).delete()
        return redirect('/')
    else:
        return HttpResponse("Method is GET")

# Update Info
def update(request, id):
    user = Resume.objects.get(id=id)
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = ResumeForm(instance=user)
    contaxt = {'form':form}
    return render(request, 'uploader/update.html', contaxt)
