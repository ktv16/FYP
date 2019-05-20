import pandas as pd
import xlsxwriter

def map_nums_to_sheet_names(my_num):

    switcher={
         1:   "SF_BF",
         2:   "SF_SS",
         3:   "SS_SB",
         4:   "SS_BS",
         5:   "SS_BB",
         6:   "SF_SB",
         7:   "SF_BS",
         8:   "SF_BB",
         9:   "SB_BS",
         10:  "SB_BB",
         11:  "BS_BB",
         12:  "BF_SS",
         13:  "BF_SB",
         14:  "BF_BS",
         15:  "BF_BB"
    }
    return switcher.get(my_num, "error_sheet")

with xlsxwriter.Workbook('Pairs_Found.xlsx', {'nan_inf_to_errors': True}) as workbook:
# Create new worksheet and print keys at the top
    worksheet = workbook.add_worksheet()
    d = pd.read_excel('/Users/kevinvela/Desktop/Kev/Identified_Genes.xlsx', sheet_name=1)
    keyss = d.keys()
    for key in range(len(keyss)-1):
        worksheet.write( 0, key, keyss[key])
    for key in range(len(keyss)-1):
        worksheet.write( 0, key+15, keyss[key])

# We create an index to count a new row for every new pair
    index = 1
    for sheet in range(15):
        df = pd.read_excel('/Users/kevinvela/Desktop/Kev/Identified_Genes.xlsx', sheet_name=sheet)

        for sheet2 in range(15):
#if sheet is same skip
            if(sheet == sheet2):
                continue

            df2 = pd.read_excel('/Users/kevinvela/Desktop/Kev/Identified_Genes.xlsx', sheet_name=sheet2)
            keys = df.keys()
            keys2 = df2.keys()



# Now we look for pairs
            for row1 in range(len(df['gene_id'])):
                for row2 in range(len(df2['gene_id'])):
                    gene_id1 = df['gene_id'][row1]
                    gene_id2 = df2['gene_id'][row2]

                    if (gene_id1 == gene_id2):
                        for col1 in range(14):
                            worksheet.write( index, col1, df[keys[col1]][row1] )
                        sheet_name = map_nums_to_sheet_names(sheet+1)
                        worksheet.write(index, 14, sheet_name)

                        for col2 in range(14):
                            worksheet.write( index, col2+16, df2[keys2[col2]][row2] )
                        sheet_name2 = map_nums_to_sheet_names(sheet2+1)
                        worksheet.write(index, 30, sheet_name2)

                        # increment index once a new pair is printed onto output file
                        index += 1

                    else:
                        continue

        print("Sheet " + str(sheet) + " done")
