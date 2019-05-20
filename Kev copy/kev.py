import pandas as pd
import xlsxwriter

with xlsxwriter.Workbook('Identified_Genes.xlsx', {'nan_inf_to_errors': True}) as workbook:
    for sheet in range(15):
        df = pd.read_excel('/Users/kevinvela/Desktop/Kev/habtewold_cuffdiff_all.xlsx', sheet_name=sheet)
        worksheet = workbook.add_worksheet()
        keys = df.keys()
        index = 1

        for key in range(len(keys)-1):
            worksheet.write( 0, key, keys[key])

        for row in range(len(df['p_value'])):
            num = df['p_value'][row]

            if (num > 0 and num < 0.05):

                for col in range(14):

                    worksheet.write( index, col, df[keys[col]][row] )
                index += 1

            else:
                continue
        worksheet.write( 0, 15, index)
        print("Sheet " + str(sheet) + " done")
