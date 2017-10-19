import xml.etree.ElementTree as ET
from jinja2 import Template


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
        'name': original_dictionary.get('name')
    }
    
def make_class_name(original_dictionary):
    return remove_last_s(original_dictionary.get('tableName'))
    
changeSets = root.findall(
    element_str_formater('changeSet', namespace),
    namespace
)

def get_all():
    for changeSet in changeSets:
        for element in changeSet:
            if 'createTable' in element.tag:
                
                columns = element.findall(
                    element_str_formater('column', namespace),
                    namespace
                )
                return {
                    'class_name': make_class_name(element.attrib),
                    'attributes': tuple(
                        make_attribute(column.attrib) for column in columns
                    )
                }
                


with open('template') as file:
    template = Template(file.read())
    with open('teste.java', 'w') as file_to_write:
        teste = get_all()
        template_rendered = template.render(class_name=teste.get('class_name'), attributes=teste.get('attributes'))
        file_to_write.write(template_rendered)