from django.contrib import messages
from django.shortcuts import render

import django_tables2 as tables
from django_tables2 import SingleTableView
from django_tables2.config import RequestConfig

from django.views.generic.edit import FormView

from .forms import SearchForm
from .models import Entry


class EntryTable(tables.Table):
    class Meta:
        model = Entry
        exclude = ('id', )


class TableView(SingleTableView, FormView):
    table_class = EntryTable
    template_name = 'table/table.html'
    model = Entry
    form_class = SearchForm
    extra_context = {'form': SearchForm}

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            ffield = form['filter_field'].data.strip()
            condition = form['condition_field'].data.strip()
            number = form['number_field'].data
            if ffield != 'title':
                try:
                    number = int(number)
                except ValueError:
                    messages.error(request, 'Некорректное значение в поле '
                                            '"Значение для фильтрации"')
                    context = {'table': EntryTable(Entry.objects.all()), 'form': form, }
                    return render(request, self.template_name, context=context)
            filters = {
                'amount': {
                    'lte': Entry.objects.filter(amount__lte=number).defer('id'),
                    'gte': Entry.objects.filter(amount__gte=number),
                    'exact': Entry.objects.filter(amount__exact=number),
                    'contains': Entry.objects.filter(amount__contains=number),
                },
                'distance': {
                    'lte': Entry.objects.filter(distance__lte=number),
                    'gte': Entry.objects.filter(distance__gte=number),
                    'exact': Entry.objects.filter(distance__exact=number),
                    'contains': Entry.objects.filter(distance__contains=number),
                },
                'title': {
                    'lte': Entry.objects.filter(title__lte=number),
                    'gte': Entry.objects.filter(title__gte=number),
                    'exact': Entry.objects.filter(title__exact=number),
                    'contains': Entry.objects.filter(title__contains=number),
                }

            }
            entries = filters[ffield][condition]
            table = EntryTable(entries)
            return render(request, self.template_name, context={'table': table, 'form': form})
        context = {'table': EntryTable(Entry.objects.all()), 'form': form}
        return render(request, self.template_name, context)
