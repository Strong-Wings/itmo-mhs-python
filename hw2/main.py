from latex_generator_skryzhankov import create_table, create_document, create_image


def main():
    table_tex = create_table([
        ["City", "Population", "Country"],
        ["Moscow", "13 274 000", "Russia"],
        ["Saint Petersburg", "5 653 000", "Russia"],
        ["London", "9 648 000", "UK"],
        ["New York", "8 804 000", "USA"],
        ["Tokyo", "14 253 000", "Japan"],
    ])
    image_tex = create_image('city.png')
    doc_tex = create_document([table_tex, image_tex], 'article', ['graphicx'])
    with open('artifacts/doc.tex', 'w') as f:
        f.write(doc_tex)


if __name__ == "__main__":
    main()
