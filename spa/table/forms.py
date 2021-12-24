from django import forms

SEARCH_FIELDS = (
    ('title', 'Название'),
    ('amount', 'Количество'),
    ('distance', 'Расстояние')
)

CONDITIONS = (
    ('exact', 'Равно'),
    ('contains', 'Включает'),
    ('gte', 'Больше'),
    ('lte', 'Меньше')
)


class SearchForm(forms.Form):
    filter_field = forms.CharField(label='Фильтрация по выбранному полю',
                                   widget=forms.Select(choices=SEARCH_FIELDS))
    condition_field = forms.CharField(label='Условие фильтрации',
                                      widget=forms.Select(choices=CONDITIONS))
    number_field = forms.CharField(label='Значение для фильтрации')
