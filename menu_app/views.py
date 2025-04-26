"""
menu_app/views.py
This module is used to create the menu for the website
"""
from django.shortcuts import render

from menu_app.models import MenuLinksModel, MenuModel, PageModel


# Create your views here.
def create_menu() -> [{str: dict}]:
    """
    This function is used to create the menu for the website
    :param page_list: List of the pages that are active
    :return: The menu as a string
    """
    menu_list = MenuLinksModel.objects.all()
    # GET ALL THE ACTIVE PAGES
    page_active_list = \
        [item for item in menu_list if str(True) in str(item.pages.active)]
    # CREATES THE LIST FROM OBJECTS OF MODEL PAGE AND MENU'S LEVELS
    list_direct = [{"pages": item.pages, "level": item.menu}
                   for item in page_active_list]
    # CREATE THE LIST OF LEVELS for ITERATOR

    def list_iteration(page_list):
        """
        This function is used to iterate the list from levels menu
        :param page_list: str[] of levels. menu
        :return:
        """
        level_list = [item.menu for item in page_list]
        for item in level_list:
            yield item

    common_refer_list = []
    # GET RESULT FROM ITERATOR
    level_object = list_iteration(menu_list)
    for item in level_object:
        # CREATE THE HTML/STRING OF THE MENU BASED
        refer_list = \
            [f"""<li class="nav-item"><a class="nav-link" \
            href="{view["pages"].links}">{view["pages"].text}</a></li>
        """ for view in list_direct if item.level in view["level"].level]
        # CLEARN THE STRING
        new_refer_list = [item.replace("\n        ", "") for item in refer_list]
        common_refer_list.append({item.level: new_refer_list})
    # GET UNIQUE VALUES FOR THE LEVELS
    # key. It is the name of the menu levels
    k = ""
    for item in common_refer_list:
        if k in item:
            continue
        k = list(item.keys())[0]
        common_refer_list.remove(item)
    return common_refer_list


def page_veiws(request) -> type(render):
    """
    This function is used to render the page based on the request path
    :param request: The request from the client
    :return: The page as a html
    """
    # menu_list = MenuLinksModel.objects.all()
    # GET list of LINKS MENU
    common_refer_list = create_menu()
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
        item_list = (view_lpage.links)
        if '/' != item_list:
            item_list = item_list.split("/")[0]
        """
        "texts" - title of pages.
        "menu" - list of dictionary from {< level_name >: \
[< string of html-referances >]}.
        """
        if (len(item_list) > 1 or '/' == item_list ) \
            and item_list in request.path:
            return render(
                request,
                template_name=view_lpage.template,
                context={"texts": view_lpage.text,
                         "menu": common_refer_list,
                         },
            )
    return render(request, "404/index.html")
