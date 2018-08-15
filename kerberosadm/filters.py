from django.contrib.admin.filters import AllValuesFieldListFilter

class DropdownFilter(AllValuesFieldListFilter):
    template = 'admin/kerberosadm/dropdown_filter.html'
