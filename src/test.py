from lxml import etree
import HTMLParser
from src import common_params
html_parser = HTMLParser.HTMLParser()

root = etree.Element('xml')
to_user_name = etree.SubElement(root, 'ToUserName' )
xml_content='<![CDATA[toUser]]>'
to_user_name.text=xml_content

xml=etree.tostring(root,pretty_print=True)

print html_parser.unescape(xml)