from django.shortcuts import render

from menu_app.models import MenuModel, PageModel

# Create your views here.


def pageVeiws(request):
    menu_list = MenuModel.objects.all()
    # GET ALL THE ACTIVE PAGES
    page_active_list = PageModel.objects.filter(active=True)
    if len(page_active_list) == 0:
        return render(request, template_name="404/index.html")
    # CREATE THE REFERENCES LIST FROM THE ACTIVE PAGE
    refer_list = []

    for i in range(0, len(list(page_active_list))):
        refer = list(page_active_list)[i].links

        if "404" not in refer:
            refer_list.append(refer)

    # THE PAGE TEMPLATE WILL DEFINE
    for view_lpage in page_active_list:
        item_list = (view_lpage.links).split("/")[0]
        if len(item_list) > 1 and item_list in request.path:
            return render(
                request,
                template_name=view_lpage.template,
                context={"texts": view_lpage.text},
            )
    return render(request, "404/index.html")
