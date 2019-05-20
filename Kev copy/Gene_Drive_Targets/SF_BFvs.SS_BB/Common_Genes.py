import pandas as pd
import xlsxwriter

with xlsxwriter.Workbook('Common_Genes.xlsx', {'nan_inf_to_errors': True}) as workbook:

    #Find genes that are in common between SF_BF vs. SS_BB
        sheet_0 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=0)
        sheet_2 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheent_name=2)

        worksheet = workbook.add_worksheet()
        keys = sheet_0.keys()
        gene_id = []
        index = 1

        gene_id0 = list(sheet_0['gene_id'])
        gene_id2 = list(sheet_2['gene_id'])

        for key in range(13):
            worksheet.write( 0, key, keys[key])

        #Print everything in the gene_id column that is common to both SF_BF and SS_BB
        for row in range(len(gene_id0)):
            gene = gene_id0[row]

            if gene in gene_id2:
                gene_id.append(gene)

                for col in range(14):
                        worksheet.write( index, col, sheet_0[keys[col]][row] )
                index += 1
            else:
                continue

        worksheet.write( 0, 14, index-1)
        print("Program Done")
