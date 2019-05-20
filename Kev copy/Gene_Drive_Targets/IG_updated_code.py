import pandas as pd
import xlsxwriter

with xlsxwriter.Workbook('IG_update.xlsx', {'nan_inf_to_errors': True}) as workbook:
    worksheet = workbook.add_worksheet()
    gene_id = []
    index = 1
#Find all genes in the Identified_Genes file. Leave out duplicates.
    for sheet in range(15):
        df = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/GOOD/Identified_Genes.xlsx', sheet_name=sheet)
        keys = df.keys()

        if sheet == 0:
            for key in range(13):
                worksheet.write( 0, key, keys[key])

        for row in range(len(df['gene_id'])):
            gene = df['gene_id'][row]

            if gene not in gene_id:
                gene_id.append(gene)

                for col in range(14):

                    worksheet.write( index, col, df[keys[col]][row] )
                index += 1

            else:
                continue

    worksheet.write( 0, 15, index)
    print('Program Done')
