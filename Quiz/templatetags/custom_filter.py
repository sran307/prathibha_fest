from django import template # type: ignore
from datetime import datetime
from prathibha_fest.settings import MEDIA_URL
import os
from pathlib import Path


register = template.Library()



@register.filter
def filenameonly(file_url):
 if file_url:
        return os.path.basename(file_url.name)
 return ""




@register.filter
def testfilter(data):
    return f"fs-{data}"