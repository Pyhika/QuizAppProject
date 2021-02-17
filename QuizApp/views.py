from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import QuizModel
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

@login_required
def list_quizview(request):
    quiz_object_list = QuizModel.objects.all()
    return render(request, 'list_quiz.html', {'quiz_object_list': quiz_object_list})


class QuizCreate(CreateView):
    template_name = 'create_quiz.html'
    model = QuizModel
    fields = ('question', 'answer', 'author', 'tag')
    success_url = reverse_lazy('list_quiz')


class QuizDelete(DeleteView):
    template_name = 'delete_quiz.html'
    model = QuizModel
    success_url = reverse_lazy('list_quiz')


class QuizUpdate(UpdateView):
    template_name = 'update_quiz.html'
    model = QuizModel
    fields = ('question', 'answer', 'author', 'tag')
    success_url = reverse_lazy('list_quiz')
