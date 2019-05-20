import pandas as pd
import xlsxwriter

with xlsxwriter.Workbook('SF_BF_vs.SS_BB.xlsx', {'nan_inf_to_errors': True}) as workbook:

    #Find genes that are unique to SS_BB and to SF_BF
    sheet_0 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=0)
    sheet_2 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=2)
    worksheet = workbook.add_worksheet()
    keys = sheet_0.keys()
    unique_genes = []
    index = 1

    gene_id0 = list(sheet_0['gene_id'])
    gene_id2 = list(sheet_2['gene_id'])

    for key in range(13):
        worksheet.write( 0, key, keys[key])

    #Print everything in the gene_id column but ignore duplicates.
    for row in range(len(gene_id0)):
        string = sheet_0['gene_id'][row]

        if string not in gene_id2:
            #unique_genes.append(sheet_0)
            for col in range(14):
                worksheet.write( index, col, sheet_0[keys[col]][row] )
            index += 1

        else:
            continue

    for row in range(len(gene_id2)):
        string = sheet_2['gene_id'][row]

        if string not in gene_id0:
            #unique_genes.append(sheet_0)
            for col in range(14):
                worksheet.write( index, col, sheet_2[keys[col]][row] )
            index += 1

        else:
            continue

    worksheet.write( 0, 14, index)
    print("Program Done")
