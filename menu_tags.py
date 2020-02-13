from django import template
# from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from menus.models import MenuItem


register = template.Library()

menu_items = MenuItem.objects.all()


@register.inclusion_tag('menus/menu_tree.html', takes_context=True)
def draw_menu(context, menu_name):
    # menu = get_object_or_404(MenuItem, name=menu_name, parent=None)
    menu = False
    for item in menu_items:
        if item.name == menu_name and item.parent == None:
            menu = item
            break
    if not menu:
        raise Http404('No matches the given query')

    local_context = {'menu_item': menu}
    requested_url = context['request'].path
    try:
        active_menu_item = MenuItem.objects.get(explicit_url=requested_url)
    except ObjectDoesNotExist:
        pass
    else:
        unwrapped_menu_item_ids = \
            active_menu_item.get_elder_ids() + [active_menu_item.id]
        local_context['unwrapped_menu_item_ids'] = unwrapped_menu_item_ids
    return local_context


@register.inclusion_tag('menus/menu_tree.html', takes_context=True)
def draw_menu_item_children(context, menu_item_id):
    # menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    menu_item = False
    for item in menu_items:
        if item.pk == menu_item_id:
            menu_item = item
            break
    if not menu_item:
        raise Http404('No matches the given query')

    local_context = {'menu_item': menu_item}
    if 'unwrapped_menu_item_ids' in context:
        local_context['unwrapped_menu_item_ids'] = \
            context['unwrapped_menu_item_ids']
    return local_context
