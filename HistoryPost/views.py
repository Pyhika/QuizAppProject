from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import HistoryModel

@login_required
def list_historyview(request):
    history_object_all = HistoryModel.objects.all()
    return render(request, 'list_history.html', {'history_object_all': history_object_all})


class HistoryCreate(CreateView):
    template_name = 'create_history.html'
    model = HistoryModel
    fields = ('title', 'summary', 'content', 'author', 'images', 'category')
    success_url = reverse_lazy('list_history')


@login_required
def detail_historyview(request, pk):
    history_object = HistoryModel.objects.get(pk=pk)
    return render(request, 'detail_history.html', {'history_object': history_object})


class HistoryDelete(DeleteView):
    template_name = 'delete_history.html'
    model = HistoryModel
    success_url = reverse_lazy('list_history')


class HistoryUpdate(UpdateView):
    template_name = 'update_history.html'
    model = HistoryModel
    fields = ('title', 'summary', 'content')
    success_url = reverse_lazy('list_history')
