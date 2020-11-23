import xlrd


# Função que captura os dados de uma planilha em um arquivo excel
def get_excel_data(path, sheet, row, column):
    if path is None or path == '':
        assert IOError('Arquivo não encontrado!')
    else:
        workbook = xlrd.open_workbook(path)
        worksheet = workbook.sheet_by_name(sheet)
        return worksheet.cell(row, column).value
