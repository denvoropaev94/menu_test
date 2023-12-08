from .models import MenuItem


def menu_processor(request):
    menu_items = MenuItem.objects.all()
    for item in menu_items:
        if item.url == request.current_url:
            item.is_active = True
        else:
            item.is_active = False
    return {'menu_items': menu_items}
