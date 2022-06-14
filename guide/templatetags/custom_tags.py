from django import template
import os

register = template.Library()

@register.filter
def filename(value):
    return os.path.basename(value.file.name)

@register.filter
def readfile(text):
    with text.open() as f:
        lines = f.readlines()
        data = ""
        for line in lines:
            line = line.decode('utf-8')
            if line.startswith("\\t"):
                line += ("\\t")
            print(line)
            data += line
        return data


#
# register.filter('text_break', text_break)