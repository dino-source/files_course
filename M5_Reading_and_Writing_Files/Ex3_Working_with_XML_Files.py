import xml.etree.ElementTree as et


def parse_xml_et(fn):
    tree = et.parse(fn)
    root = tree.getroot()
    print("Domains for: " + root.attrib["name"])
    for child in root:
        print("\t" + child.attrib["name"], child.tag)


def add_xml_element_et(fn, el, attr, val):
    tree = et.parse(fn)
    root = tree.getroot()
    child = et.Element(el)
    child.attrib[attr] = val
    root.append(child)
    tree.write(fn)


def change_xml_element_et(fn, el, attr, oldval, newval):
    tree = et.parse(fn)
    root = tree.getroot()
    child = root.find("./" + el + "[@" + attr + "='" + oldval + "']")
    child.attrib[attr] = newval
    tree.write(fn)


# parse_xml_et("./author.xml")
# add_xml_element_et("./author.xml", "domain", "name", "Java")
change_xml_element_et("./author.xml", "domain", "name", "Java", "Kotlin")
