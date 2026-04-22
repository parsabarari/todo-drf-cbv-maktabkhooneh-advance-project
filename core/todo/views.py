from django.views.generic import ListView, CreateView,UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from todo.models import TaskModel
from accounts.models import Profile
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect


class TaskListView(LoginRequiredMixin, ListView):
    model = TaskModel
    template_name = 'tasks/task_list.html'
    context_object_name = 'todos'
    
    def get_queryset(self):
        return TaskModel.objects.filter(author__user=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = TaskModel
    fields = ['title', 'description', 'priority', 'completed']
    template_name = 'tasks/task_create.html'
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TaskModel
    template_name = 'tasks/task_update.html'
    success_url = '/tasks/'
    fields = ['title', 'description', 'priority', 'completed']

    def test_func(self):
        task = self.get_object()
        return task.author.user == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # اینجا می‌تونیم فیلد priority رو read-only کنیم اگر بخواهیم
        # context['form'].fields['priority'].disabled = True
        return context

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TaskModel
    template_name = 'tasks/task_confirm_delete.html'
    success_url = '/tasks/'
    context_object_name = 'task'

    def test_func(self):
        task = self.get_object()
        return task.author.user == self.request.user

    def delete(self, request, *args, **kwargs):
        # اضافه کردن پیام موفقیت پس از حذف
        messages.success(request, f'تسک "{self.get_object().title}" با موفقیت حذف شد.')
        return super().delete(request, *args, **kwargs)

class TaskCompleteToggleView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(TaskModel, pk=pk)

        if task.author.user != request.user:
            messages.error(request, 'شما اجازه دسترسی به این تسک را ندارید.')
            return redirect('task_list')

        task.completed = not task.completed
        task.save()

        status = "تکمیل شد" if task.completed else "به عنوان ناتمام علامت‌گذاری شد"
        messages.success(request, f'تسک "{task.title}" با موفقیت {status}.')
        return redirect('task_list')
