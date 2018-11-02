import xml.dom.minidom
def main():
    doc=xml.dom.minidom.parse("sample1xml.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    skills=doc.getElementsByTagName("skill")
    print("%d skill :" % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))
    newskill=doc.createElement("skill")
    newskill.setAttribute("name","stats")
    doc.firstChild.appendChild(newskill) 
    skills=doc.getElementsByTagName("skill")
    print("%d skill :" % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

main()    