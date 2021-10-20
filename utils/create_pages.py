

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
    name_to_fr = {
        'compte': 'Compte',
        'cash': 'Cash',
        'materiel': 'Matériel',
        'by_activity': 'Tri par Activité'
    }

    for name in new_data:
        with open("source_html/page.html", "r", encoding='utf-8') as f:
            page = f.read()

        page = page.replace('$1', name_to_fr[name])
        table = new_data[name].to_html(index=False)
        page = page.replace('$2', table)

        page = add_color_to_values(page)        

        page_file = open(f"page_{name}.html", "w")
        page_file.write(page)
        page_file.close()


def add_color_to_values(page):
    """This function add colors to values in subpages

    Args:
        page (str): HTML page in str format

    Returns:
        str: modified HTML page
    """
    new_page = ''

    for line in page.splitlines():

        if '€</td>' in line:

            if '-' in line:
                color = '#FA413B'  # Red

            else:
                color = '#34FF27'  # Greend

            line = line.replace('<td>', f'<td style="color:{color}"">')

        new_page += line + '\n'

    return new_page


def create_pages(new_data):
    """This function create all html pages

    Args:
        new_data (dictionnary): dictionnary containing all the new sheets
    """
    create_main_page(new_data)
    create_sub_pages(new_data)