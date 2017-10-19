import xml.etree.cElementTree as ET
from jinja2 import Template

namespace = {'dbchangelog': 'http://www.liquibase.org/xml/ns/dbchangelog'}

def element_str_formater(string, namespace = None):
    if namespace:
        return '{}:{string}'.format(next(iter(namespace)), string=string)
    return '{string}'.format(string=string)

def remove_last_s(string):
    if string.endswith('s'):
        return string[:-1]
    return string

def verify_types(string):
    types_sql_java = {
        'integer': 'Long',
        'bool': 'boolean',
        'numeric': 'BigDecimal',
        'char': 'String',
        'int': 'Long'
    }
    
    for key, value in types_sql_java.items():
        if key in string:
            return value

    raise ValueError('Undefined Type')
    
def make_attribute(original_dictionary):
    return {
        'type': verify_types(original_dictionary.get('type')),
        'name': to_camel_case(original_dictionary.get('name'))
    }
    
def make_class_name(original_dictionary):
    return remove_last_s(original_dictionary.get('tableName'))

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def get_all(changeSets):
    for changeSet in changeSets:
        for element in changeSet:
            if 'createTable' in element.tag:
                
                columns = element.findall(
                    element_str_formater('column', namespace),
                    namespace
                )
                return {
                    'class_name': to_camel_case(make_class_name(element.attrib)),
                    'attributes': tuple(
                        make_attribute(column.attrib) for column in columns
                    )
                }

def main():
    tree = ET.parse(open('example.xml'))
    root = tree.getroot()
    changeSets = root.findall(
        element_str_formater('changeSet', namespace),
        namespace
    )
    with open('template') as file:
        template = Template(file.read())
        teste = get_all(changeSets)
        file_name_to_write = '{class_name}.java'.format(class_name=teste.get('class_name').title())
        with open(file_name_to_write, 'w') as file_to_write:
            template_rendered = template.render(class_name=teste.get('class_name'), attributes=teste.get('attributes'))
            file_to_write.write(template_rendered)

if __name__ == '__main__':
    main()