from django.views.generic import( ListView , 
                                    UpdateView , 
                                    CreateView ,
                                    DetailView, 
                                    DeleteView,
                                    TemplateView)
                                    
from .models import Thing
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


class ThingListView(ListView):
    template_name = 'things_list.html'
    model = Thing
    context_object_name = 'thing_list'


class ThingDetailView(DetailView):
    template_name = 'things_detail.html'
    model = Thing


class ThingCreateView(CreateView):
    template_name = 'thing_create.html'
    model = Thing
    fields = ['name' , 'raiting' , 'reviewer']

class ThingUpdateView(UpdateView):
    template_name = 'thing_update.html'
    model = Thing
    fields = ['name' , 'raiting']

class ThingDeleteView(DeleteView):
    template_name = 'thing_delete.html'
    model = Thing
    success_url = '/'