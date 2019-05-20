import pandas as pd
import xlsxwriter

with xlsxwriter.Workbook('Heatmap_GEA_genes.xlsx', {'nan_inf_to_errors': True}) as workbook:
    # for sheet:
        df = pd.read_excel('//Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Pairs_Found.xlsx')
        worksheet = workbook.add_worksheet()
        keys = df.keys()
        gene_id = []
        index = 1

        for key in range(14):
            worksheet.write( 0, key, keys[key])

        #Print everything in the gene_id column but ignore duplicates.
        for row in range(len(df['gene_id'])):
            str = df['gene_id'][row]

            if str not in gene_id:
                gene_id.append(str)

                for col in range(14):

                    worksheet.write( index, col, df[keys[col]][row] )
                index += 1

            else:
                continue
        worksheet.write( 0, 15, index)
        print("GEA_gene_id_sheet_done")
