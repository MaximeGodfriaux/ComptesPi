

def create_main_page(new_data):
    """This function creates the main html page

    Args:
        new_data (dictionnary): dictionnary containing all the new sheets
    """
    with open("source_html/index.html", "r", encoding='utf-8') as f:
        page = f.read()

    for name in ['compte', 'cash', 'materiel', 'by_activity']:
        total_value = new_data[name].iloc[-1]['Montant']
        page = page.replace(f'${name}', total_value)

    page_file = open("index.html", "w")
    page_file.write(page)
    page_file.close()


def create_sub_pages(new_data):
    """This function creates the sub pages

    Args:
        new_data (dictionnary): dictionnary containing all the new sheets
    """
    for name in new_data:
        with open("source_html/page.html", "r", encoding='utf-8') as f:
            page = f.read()
        page_file = open(f"page_{name}.html", "w")
        page_file.write(page)
        page_file.close()


def create_pages(new_data):
    """This function create all html pages

    Args:
        new_data (dictionnary): dictionnary containing all the new sheets
    """
    create_main_page(new_data)
    create_sub_pages(new_data)