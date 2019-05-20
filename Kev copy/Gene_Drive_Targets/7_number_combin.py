import pandas as pd
import xlsxwriter

with xlsxwriter.Workbook('Upregulated_Genes.xlsx', {'nan_inf_to_errors': True}) as workbook:
    #Read sheets: SF_BF, SS_SB, SS_BB, SF_SB, SB_BB, BS_BB, BF_BB
    for sheet in [0, 2, 4, 9, 10]:
        df = pd.read_excel('//Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/GOOD/Identified_Genes.xlsx', sheet_name=sheet)
        worksheet = workbook.add_worksheet()
        keys = df.keys()
        index = 1

        for key in range(len(keys)-1):
            worksheet.write( 0, key, keys[key])

        for row in range(len(df['log2(fold_change)'])):
            num = df['log2(fold_change)'][row]

            #Read through column and any cell that is not a number gets ignored and the next line is read
            try:
                int_num = float(num)
            except:
                continue

            if (int_num > 1):


                for col in range(14):

                    worksheet.write( index, col, df[keys[col]][row] )
                index += 1


            else:
                continue
        worksheet.write( 0, 15, index-1)
        print("Sheet " + str(sheet) + " done")
