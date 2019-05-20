#Find common genes between three sets of sheets: SS_SB vs. SS_BB vs. BS_BB
#Want to find pairs between two sheets, then compare a third sheet to the list made to see if there are any in common.
import pandas as pd
import xlsxwriter

with xlsxwriter.Workbook('Venn3_overlap_genes.xlsx', {'nan_inf_to_errors': True}) as workbook:
# Create new worksheet and print keys at the top. Same format as Pairs Found excel file.

    df1 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=1)
    df2 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=2)
    df4 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=4)

    worksheet = workbook.add_worksheet()
    keys = df1.keys()
    overlaps = []
    overlaps2 = []
    index = 1

    gene_id1 = list(df1['gene_id']) #Reads SS_SB (sheet_name=1)
    gene_id2 = list(df2['gene_id']) #Reads SS_BB (sheet_name=2)
    gene_id4 = list(df4['gene_id']) #Reads SS_BB (sheet_name=4)

    for key in range(13):
        worksheet.write( 0, key, keys[key])
    # We create an index to count a new row for every new pair

    for row in range(len(gene_id1)):
        gene = gene_id1[row]

        if gene in gene_id2:
            overlaps.append(gene)

        else:
            continue

    for row in range(len(gene_id4)):
        gene_4 = gene_id4[row]

        if gene_4 in overlaps:
            overlaps2.append(gene_4)

            for col in range(14):
                    worksheet.write(index, col, df4[keys[col]][row])
            index += 1
        else:
            continue

    worksheet.write(0, 14, index-1)
    print("Program Done")


    # for set_1.intersection(set_2):

# Now we look for pairs
        #     for row1 in range(len(df['gene_id'])):
        #         for row2 in range(len(df2['gene_id'])):
        #             gene_id1 = df1['gene_id'][row1]
        #             gene_id2 = df2['gene_id'][row2]
        #
        #             if (gene_id1 == gene_id2):
        #                 for col1 in range(14):
        #                     worksheet.write( index, col1, df[keys[col1]][row1] )
        #                 sheet_name = map_nums_to_sheet_names(sheet+1)
        #                 worksheet.write(index, 14, sheet_name)
        #
        #                 for col2 in range(14):
        #                     worksheet.write( index, col2+16, df2[keys2[col2]][row2] )
        #                 sheet_name2 = map_nums_to_sheet_names(sheet2+1)
        #                 worksheet.write(index, 30, sheet_name2)
        #
        #                 # increment index once a new pair is printed onto output file
        #                 index += 1
        #
        #         else:
        #             continue
        #
        # print("Sheet " + str(sheet) + " done")
