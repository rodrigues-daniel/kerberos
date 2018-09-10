from django.contrib.admin.filters import AllValuesFieldListFilter

class DropdownFilter(AllValuesFieldListFilter):
    template = 'admin/permissoes/dropdown_filter.html'
