import xmltodict
from pprint import pprint

"""
XML (eXtensible Markup Language) — це формат текстових файлів для збереження та передачі структурованих даних.
Він виглядає як HTML, але не для відображення сторінок, а для зберігання даних у структурі “дерева”
- Передача даних між системами
- Конфігураційні файли Налаштування тестів, середовищ, даних часто описуються через XML (testng.xml в Java, Jenkins-пайплайни)
- Репорти тестування
- Тестові дані
"""
#------------ read xml from file
# with open("xmlfile.xml", "r") as xml_file:
#     xml_string = xml_file.read()
#     print(xml_string)

# parse xml string to dict
xml_string: str = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:myg="http://www.mygemini.com/schemas/mygemini"
                  xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <soapenv:Header>
        <wsse:Security>
            <wsse:UsernameToken>
                <wsse:Username>******</wsse:Username>
                <wsse:Password>******</wsse:Password>
                <wsse:Nonce>******</wsse:Nonce>
            </wsse:UsernameToken>
        </wsse:Security>
    </soapenv:Header>
    <soapenv:Body>
        <myg:GetAccountMovementsRequestIo>
            <myg:accountMovementFilterIo>
                <myg:pager>
                    <myg:pageIndex>0</myg:pageIndex>
                    <myg:pageSize>700</myg:pageSize>
                </myg:pager>
                <myg:accountNumber>GE16TB7739436090000001</myg:accountNumber>
                <myg:accountCurrencyCode>GEL</myg:accountCurrencyCode>
                <myg:periodFrom>2025-03-19T00:00:00</myg:periodFrom>
                <myg:periodTo>2025-03-20T23:00:00</myg:periodTo>
            </myg:accountMovementFilterIo>
        </myg:GetAccountMovementsRequestIo>
    </soapenv:Body>
</soapenv:Envelope>"""

# convert xml string to dict
xml_converted: dict = xmltodict.parse(xml_string)
# pprint(xml_converted)


xml_converted['soapenv:Envelope']['@xmlns:myg'] = "https://hillel.com.ua"

# convert dict to xml object
final_xml_file: str = xmltodict.unparse(xml_converted, pretty=True)
print(final_xml_file)