from openpyxl import Workbook
from reportlab.platypus import SimpleDocTemplate, Table


# ================= EXCEL =================

def export_excel(filename, headers, data):

    wb = Workbook()

    sheet = wb.active

    sheet.title = "Report"


    sheet.append(headers)


    for row in data:

        sheet.append(row)


    wb.save(filename)




# ================= PDF =================

def export_pdf(filename, headers, data):

    pdf = SimpleDocTemplate(filename)


    table_data = []

    table_data.append(headers)


    for row in data:

        table_data.append(row)



    table = Table(table_data)


    pdf.build([table])