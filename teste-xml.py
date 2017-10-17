import xml.etree.ElementTree as ET


tree = ET.parse(open('example.xml'))
root = tree.getroot()

namespace = {'dbchangelog': 'http://www.liquibase.org/xml/ns/dbchangelog'}

def element_str_formater(string, namespace = None):
    if namespace:
        return '{}:{string}'.format(next(iter(namespace)), string=string)
    return '{string}'.format(string=string)

def remove_last_s(string):
    if 's' in string[-1]:
        return string[:-1]
    return string

changeSets = root.findall(element_str_formater('changeSet', namespace), namespace)

with open('teste.java', 'w') as file:
    for changeSet in changeSets:
        for element in changeSet:
            if 'createTable' in element.tag:
                file.write('public class {}'.format(remove_last_s(element.attrib.get('tableName').title())))
                print(element.attrib)
                for column in element:
                    print()