import os, inspect
from django.shortcuts import render
from django.views.generic import ListView,CreateView, UpdateView,DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models
from django.conf import settings

def access_denial(request):

    return render(request, 'main/access_denial.html',{})

def get_cur_folder(f):
    return os.path.dirname(os.path.abspath(f)).replace(os.path.dirname(os.path.dirname(os.path.abspath(f)))+"\\","")

def view(f):
    return ('{0}.can_view_{0}'.format(get_cur_folder(f)))

def add(f):
    return ('{0}.add_{0}'.format(get_cur_folder(f)))

def change(f):
    return ('{0}.change_{0}'.format(get_cur_folder(f)))

def delete(f):
    return ('{0}.delete_{0}'.format(get_cur_folder(f)))




class MainList(PermissionRequiredMixin,ListView):

    permission_required = view(__file__)
    login_url = '/' #redirect to incase access denied
    def dispatch(self, request, *args, **kwargs):
        print('List View by: {0}'.format(request.user.username))
        path = inspect.getfile(self.__class__)
        print('File path: {0}'.format(path.replace(settings.BASE_DIR,'')))
        print('Fun called: {0}'.format(self.__class__.__name__))
        # if check_acc(request,'view'):
        return super(MainList, self).dispatch(request, *args, **kwargs)
        # else:
        #     return access_denial(request)

    # def get_context_data(self, **kwargs):
    #     data = super(List, self).get_context_data(**kwargs)
    #     data['lv'] = int(self.request.user.userprofile.approval_level_quote)
    #     return data


class MainCreate(PermissionRequiredMixin,CreateView):

    permission_required = add(__file__)
    login_url = '/' #redirect to incase access denied

    def dispatch(self, request, *args, **kwargs):
        print('Create View by: {0}'.format(request.user.username))
        path = inspect.getfile(self.__class__)
        print('File path: {0}'.format(path.replace(settings.BASE_DIR, '')))
        print('Fun called: {0}'.format(self.__class__.__name__))
    #     if check_acc(request,'edit'):
        return super(MainCreate, self).dispatch(request, *args, **kwargs)
    #     else:
    #         return access_denial(request)

    def get_initial(self,**kwargs):
        data = {'create_by':self.request.user.username,
                }
        return data

    # def get_context_data(self, **kwargs):
    #     data = super(Create, self).get_context_data(**kwargs)
    #     data['approver'] = check_app(self.request,'approver')
    #     return data


    # def form_valid(self, form):
    #     with transaction.atomic():
    #         form.instance.create_by = self.request.user
    #         self.object = form.save()
    #     return super(MainCreate, self).form_valid(form)


class MainUpdate(PermissionRequiredMixin,UpdateView):

    permission_required = change(__file__)
    login_url = '/' #redirect to incase access denied


    def dispatch(self, request, *args, **kwargs):
        print('Update View by: {0}'.format(request.user.username))
        path = inspect.getfile(self.__class__)
        print('File path: {0}'.format(path.replace(settings.BASE_DIR, '')))
        print('Fun called: {0}'.format(self.__class__.__name__))
    #     if (check_acc(request,'edit') and owner(request,kwargs['pk'],c=True)) or check_app(request,'checker'):
        return super(MainUpdate, self).dispatch(request, *args, **kwargs)
    #     else:
    #         return access_denial(request)

    # def get_context_data(self, **kwargs):
    #     data = super(Update, self).get_context_data(**kwargs)
    #     # data['approver'] = check_app(self.request,'approver')
    #     return data

    # def form_valid(self, form):
    #     print("cus form validation")
    #     with transaction.atomic():
    #         # form.data.update_by = self.request.user
    #         # form.instance.update_by = self.request.user
    #         self.object = form.save()
    #     return super(Update, self).form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy('customer:list')


class MainDetail(PermissionRequiredMixin,DetailView):

    permission_required = view(__file__)
    login_url = '/'


    def dispatch(self, request, *args, **kwargs):
        print('Detail View by: {0}'.format(request.user.username))
        path = inspect.getfile(self.__class__)
        print('File path: {0}'.format(path.replace(settings.BASE_DIR, '')))
        print('Fun called: {0}'.format(self.__class__.__name__))
    #     if (check_acc(request,'view') and owner(request,kwargs['pk'],c=True)) or check_app(request,'checker'):
        return super(MainDetail, self).dispatch(request, *args, **kwargs)
    #     else:
    #         return access_denial(request)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     quotes = quote.objects.all().filter(cus=self.kwargs['pk'])
    #     context['quotes']=quotes
    #     # print(context)
    #     return context



# Create your models here.
class BaseModel(models.Model):

    update_date = models.DateTimeField(auto_now = True,null=True)
    update_by = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    create_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        managed = False