from .models import Category

def menu_links(request):
    """
    This is for all category list for template Directly.
    """
    categories = Category.objects.all()
    return {
        'categories': categories
    }