import os

from lxml import etree

path_to_file = 'dataXML/UserInfo.xml'


# Прочитать из XML
def load_xml_files():
    try:
        list_fio = [[], []]
        for event, elem in etree.iterparse(path_to_file):
            if elem.tag == "FIO":
                list_fio[0].append(elem.text)
            if elem.tag == "Date":
                list_fio[1].append(elem.text)
        if len(list_fio) > 0:
            return list_fio
    except:
        os.makedirs('dataXML', exist_ok=True)
        root = etree.Element("root")
        etree.SubElement(root, "FIOs")
        etree.SubElement(root, "Dates")
        tree = etree.ElementTree(root)
        tree.write(path_to_file, pretty_print=True, encoding="utf-8", xml_declaration=True)


# Открыть проводник
# def set_path(name_doc):
#     ftypes = [('Документы по' + name_doc, '*.xlsx'), ('Документы', '*.xls'), ('Все файлы', '*')]
#     dlg = filedialog.Open(filetypes=ftypes)
#     fl = dlg.show()
#     if fl != '':
#         return fl
#     return ''


# Запись путей к файлу для парсинга в XML
def write_to_xml(path_deals, path_trans):
    if path_deals != '':
        tree = etree.parse(path_to_file)
        condition_elem = tree.find("FIOs")
        etree.SubElement(condition_elem, 'FIO').text = path_deals
        tree.write(path_to_file, pretty_print=True, encoding='utf-8', xml_declaration=True)
    if path_trans != '':
        tree = etree.parse(path_to_file)
        condition_elem = tree.find("Dates")
        etree.SubElement(condition_elem, 'Date').text = path_trans
        tree.write(path_to_file, pretty_print=True, encoding='utf-8', xml_declaration=True)
    load_xml_files()
