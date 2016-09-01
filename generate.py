import jinja2
import os
import json

data = json.load(open('data.json'))

env = jinja2.environment.Environment()
env.loader = jinja2.FileSystemLoader('.')

for filename in os.listdir('.'):
    if filename.endswith('.template.html'):
        output_filename = filename[:-len('.template.html')] + '.html'
        html = env.get_template(filename).render(data)
        open(output_filename, 'w').write(html.encode('utf-8'))
