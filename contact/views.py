from django.shortcuts import render
from django.views.generic import DetailView, ListView, FormView, CreateView
from  .models import Message
from .forms import MessageForm, ContactForm
from django.urls import reverse_lazy


# class MessageDetailView(DetailView):
#     model = Message

######################################################################
# class MessageAddView(FormView):
#     form_class = MessageForm
#     template_name = 'contact/message_form.html'
#     success_url = reverse_lazy('shelf:books')
#
#     def form_valid(self, form):
#         form.save()
#         return super(MessageAddView, self). form_valid(form)

##############################################################################

# class MessageCreateView(CreateView):
#     model = Message
#     fields = '__all__'
#     def get_success_url(self):
#         return reverse_lazy('shelf:books')

###########################################################

class MessageAddView(FormView):
    form_class = ContactForm
    template_name = 'contact/message_form.html'
    success_url = reverse_lazy('shelf:books')

    def form_valid(self, form):
       # print(form.cleaned_data)
        Message.objects.create(**form.cleaned_data)
        return super(MessageAddView, self).form_valid(form)

#####################################################################