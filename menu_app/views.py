"""
menu_app/views.py
This module is used to create the menu for the website
"""
from django.shortcuts import render

from menu_app.models import MenuLinksModel, MenuModel, PageModel, SubPageModel


# Create your views here.
def create_menu() -> [{str: dict}]:
    """
    This function is used to create the menu for the website
    :param page_list: List of the pages that are active
    :return: The menu as a string
    """
    menu_list = MenuLinksModel.objects.all()
    sub_pages_list = SubPageModel.objects.all()
    sub_pages_active_list = [item for item in sub_pages_list
                             if str(True) in str(item.active)]
    # GET ALL THE ACTIVE PAGES
    page_active_list = \
        [item for item in menu_list if str(True) in str(item.pages.active)]
    # CREATES THE LIST FROM OBJECTS OF MODEL PAGE AND MENU'S LEVELS
    list_direct = [{"pages": item.pages, "level": item.menu}
                   for item in page_active_list]
    # ADD THE SUB-PAGES TO THE LIST
    # new 'list_direct' list
    list_direct_new = []
    for item in list_direct:
        item["sub_page"] = []
        for view in sub_pages_active_list:
            if item["pages"].text == view.parent_page.text:
                item["sub_page"].append(view)
        if item in list_direct_new:
            continue
        list_direct_new.append(item)
    # CLEAR THE OLD LIST FROM 'list_direct'
    list_direct.clear()

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
        refer_list = []
        sub_page_html = '<div class="dropdown-menu">'
        for view in list_direct_new:
            if item.level in view["level"].level and len(view["sub_page"]) == 0:
                refer_list.append( f"""<li class="nav-item"><a class="nav-link"\
href="{view["pages"].links}">{view["pages"].text}</a></li>""")
            elif item.level in view["level"].level \
                and len(view["sub_page"]) > 0:
                for sub_item in view["sub_page"]:
                    sub_page_html += f"""\
<a class="dropdown-item" href="{sub_item.links}">\
{sub_item.text}</a>"""
                sub_page_html += "</div>"
                refer_list.append(f"""<li class="nav-item dropdown">\
<a class="nav-link dropdown-toggle" role="button" data-toggle="dropdown"\
 aria-expanded="false"\
href="{view["pages"].links}">{view["pages"].text}</a>{sub_page_html}</li>""")

        common_refer_list.append({item.level: refer_list})
    # GET UNIQUE VALUES FOR THE LEVELS
    new_common_refer_list = []
    for item in common_refer_list:
        if item in new_common_refer_list:
            continue
        new_common_refer_list.append(item)

    return new_common_refer_list


def page_veiws(request) -> type(render):
    """
    This function is used to render the page based on the request path
    :param request: The request from the client
    :return: The page as a html
    """
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
            res = item_list.split("/")
            if len(res) < 3:
                item_list = res[0]
            else:
                item_list = res[1]
        """
        "texts" - title of pages.\
"menu" - list of dictionary from {< level_name >: \
[< string of html-referances >]}.
        """
        if (len(item_list) > 1 or '/' == item_list ) \
            and item_list in request.path and len(request.path) == 1:
            return render(
                request,
                template_name=view_lpage.template,
                context={"texts": view_lpage.text,
                         "menu": common_refer_list,
                         },
            )
        elif  (len(item_list) > 1 or '/' != item_list ) \
            and item_list in request.path and len(request.path) > 1:
            return render(
                request,
                template_name=view_lpage.template,
                context={"texts": view_lpage.text,
                         "menu": common_refer_list,
                         },
            )
    return render(request, "404/index.html")
