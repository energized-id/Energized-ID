from .imports import *
import json
from .databaseFunctions import *
from .badgeTemplating import badgeTemplatingEngine
from django.http import JsonResponse
from django.http import Http404
import urllib.parse

AdminItems = [
    {"model":"BadgeTemplate", "title":"Badge Templates", "description":"Add or modify badge templates", "icon":"fas fa-id-badge", "url":"LibreBadge:modeladmin"},
    {"model":"AlertMessage", "title":"Alert Messages", "description":"Add or modify alert messages", "icon":"fas fa-exclamation-triangle", "url":"LibreBadge:modeladmin"}
]

@login_required
def applicationadmin(request):
    return render(request, 'LibreBadge/applicationadmin/home.html',
    context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all, "AdminItems":AdminItems, })

@login_required
def modeladmin(request,slug):
    AdminItem = {}
    for item in AdminItems:
        if item.get('model') == slug:
            AdminItem = item
    if not AdminItem:
        raise Http404
    fields = []
    for field in eval(AdminItem.get('model') + '._meta.get_fields()'):
        fields.append(field.name)
    results = []
    for value in eval(AdminItem.get('model') + '.objects.values()'):
        fieldTypes = []
        for field in eval(AdminItem.get('model') + '._meta.get_fields()'):
            fieldTypes.append(field.get_internal_type())
        values = []
        for item in list(value.values()):
            values.append(item)
        results.append(list(zip(values, fieldTypes)))
    return render(request, 'LibreBadge/applicationadmin/modeladmin.html',
    context = {"slug":slug, "fields":fields, "results":results, "BadgeTemplate":BadgeTemplate.objects.all, "AlertMessage":AlertMessage.objects.all,"title":AdminItem.get('title')})

@login_required
def itemadmin(request,modelslug,itemslug):
    AdminItem = {}
    for item in AdminItems:
        if item.get('model') == modelslug:
            AdminItem = item
    if not AdminItem:
        raise Http404('A record with the requested model name does not exist')
    values = []
    try:
        for value in list(eval(AdminItem.get('model')+ ".objects.filter(pk=" + itemslug + ").values_list()"))[0]:
            values.append(value)
    except:
        raise Http404('A record with the requested primary key does not exist')
    fields = []
    fieldTypes = []
    fieldChoices = []
    for field in eval(AdminItem.get('model') + '._meta.get_fields()'):
        fields.append(field.name)
        fieldTypes.append(field.get_internal_type())
        fieldChoices.append(eval(AdminItem.get('model') + "._meta.get_field('" + field.name +"').choices"))
    results = zip(fields, fieldTypes, fieldChoices, values)
    if request.method == 'POST':
        for field in fields:
            print(eval('request.POST.get("' + field + '")'))
    return render(request, 'LibreBadge/applicationadmin/itemadmin.html',
    context = {"results":results, "BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"title":AdminItem.get('title')})