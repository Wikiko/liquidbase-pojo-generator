from jinja2 import Template

with open('template') as file:
    template = Template(file.read())
    
    print(template.render(
        class_name='person', attributes=[
            {'name': 'idade', 'type': 'Long'}, 
            {'name': 'quantidade', 'type': 'BigDecimal'}
        ]
    ))