#!/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree
from prueba import *

root = etree.Element("root")
doc = etree.SubElement(root, "doc")

etree.SubElement(doc, "field1", name="clo").text = Modulo['Type']['Time']['Text']
etree.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = etree.ElementTree(root)
tree.write("filename.xml")
