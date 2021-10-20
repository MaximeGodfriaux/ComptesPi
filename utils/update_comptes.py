from apply_change_data import apply_change_data
from create_pages import create_pages
from load_data import load_data


def main():
    data = load_data()
    new_data = apply_change_data(data)
    create_pages(new_data)


if __name__ == '__main__':
    main()
