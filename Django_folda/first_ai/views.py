from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

class index(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('predict:top_page'))

index = index.as_view()
