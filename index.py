from openpyxl import load_workbook
import xml.etree.cElementTree as ET

def indent(elem, level=0):
  i = "\n" + level*"  "
  if len(elem):
    if not elem.text or not elem.text.strip():
      elem.text = i + "  "
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
    for elem in elem:
      indent(elem, level+1)
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
  else:
    if level and (not elem.tail or not elem.tail.strip()):
      elem.tail = i

def buildTree():
	root = ET.Element("root")
	doc = ET.SubElement(root, "doc")

	ET.SubElement(doc, "field1", name="blah").text = "some value1"
	ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

	indent(root)

	tree = ET.ElementTree(root)
  	tree.write("filename.xml", xml_declaration=True, encoding='utf-8', method="xml")
 
'''
main function, so this program can be called by python program.py
'''
if __name__ == "__main__":
  buildTree()


# wb = load_workbook('proba.xlsx')
# for sheet in wb.worksheets:
# 	print "header"
# 	for cell in list(sheet.rows)[0]:
# 		print cell.value

# 	if sheet.max_row > 1:
# 		for row in sheet.rows[1:]:
# 			for cell in row:
# 				print cell.value
