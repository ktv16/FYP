import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles
plt.figure(figsize=(6,6))

#Venn Diagram for SS_BB vs. BS_BB
df1 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=2)
df2 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=4)

list_1 = df1['gene_id'] #Reads SS_BB (sheet_name=2)
list_2 = df2['gene_id'] #Reads BS_BB (sheet_name=4)
print(list_1)

overlaps = list(set(list_1) & set(list_2)) #SS_BB(sheet_name=2) vs. BS_BB(sheet_name=4) overlaps

calc = len(list_1) - len(overlaps)
calc2 = len(list_2) - len(overlaps)

v = venn2(subsets = (calc, calc2, len(overlaps)), set_labels = ('SS_BB Total Genes: 150', 'BS_BB Total Genes: 465'))
v.get_patch_by_id('A').set_color('green')
v.get_patch_by_id('B').set_color('blue')
v.get_patch_by_id('C').set_color('cadetblue')

c = venn2_circles(subsets = (calc, calc2, len(overlaps)), linestyle = 'solid')

plt.title('SS_BB vs. BS_BB')
plt.show()


# #Venn diagram for SS_SB vs. SS_BB
# plt.figure(figsize=(6,6))
# df3 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=1)
# df1 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=2)
#
# list_4 = df3['gene_id'] #Reads SS_SB (sheet_name=1)
# list_3 = df1['gene_id'] #Reads SS_BB (sheet_name=2)
#
# overlaps2 = list(set(list_4) & set(list_3)) #SS_SB(sheet_name=1) vs. SS_BB(sheet_name=2) overlaps
#
# calc = len(list_4) - len(overlaps2)
# calc2 = len(list_3) - len(overlaps2)
#
# v = venn2(subsets = (calc, calc2, len(overlaps2)), set_labels = ('SS_SB Total Genes: 148', 'SS_BB Total Genes: 150'))
#
# c = venn2_circles(subsets = (calc, calc2, len(overlaps2)), linestyle = 'solid')
#
# plt.title('SS_SB vs. SS_BB')
# plt.show()


#Venn diagram for SS_SB vs. BS_BB
# plt.figure(figsize=(6,6))
# df3 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=1)
# df2 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=4)
#
# list_5 = df3['gene_id'] #Reads SS_SB (sheet_name=1)
# list_6 = df2['gene_id'] #Reads BS_BB (sheet_name=4)
#
# overlaps3 = list(set(list_5) & set(list_6)) #SS_SB(sheet_name=1) vs. BS_BB(sheet_name=4) overlaps
#
# calc = len(list_5) - len(overlaps3)
# calc2 = len(list_6) - len(overlaps3)
#
# v = venn2(subsets = (calc, calc2, len(overlaps3)), set_labels = ('SS_SB Total Genes: 148', 'BS_BB Total Genes: 465'))
# v.get_patch_by_id('B').set_color('blue')
# v.get_patch_by_id('C').set_color('magenta')
#
# c = venn2_circles(subsets = (calc, calc2, len(overlaps3)), linestyle = 'solid')
#
# plt.title('SS_SB vs. BS_BB')
# plt.show()

# #Venn diagram for SF_BF vs. SS_BB
# plt.figure(figsize=(6,6))
# df0 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=0)
# df1 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=2)
#
# list_7 = df0['gene_id'] #Reads SF_BF (sheet_name=0)
# list_8 = df1['gene_id'] #Reads SS_BB (sheet_name=2)
#
# overlaps4 = list(set(list_7) & set(list_8)) #SS_SB(sheet_name=1) vs. SS_BB(sheet_name=2) overlaps
#
# calc = len(list_7) - len(overlaps4)
# calc2 = len(list_8) - len(overlaps4)
#
# v = venn2(subsets = (calc, calc2, len(overlaps4)), set_labels = ('SF_BF Total Genes: 248', 'SS_BB Total Genes: 150'))
# v.get_patch_by_id('A').set_color('yellow')
#
# c = venn2_circles(subsets = (calc, calc2, len(overlaps4)), linestyle = 'solid')
#
# plt.title('SF_BF vs. SS_BB')
# plt.show()

# #Venn diagram for SF_BF vs. SS_SB
# plt.figure(figsize=(6,6))
# df0 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=0)
# df3 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name=1)
# # #
# list_x = df0['gene_id'] #Reads SF_BF (sheet_name=0)
# list_y = df3['gene_id'] #Reads SS_SB (sheet_name=1)
#
# overlaps_z = list(set(list_x) & set(list_y)) #SS_SB(sheet_name=1) vs. SS_BB(sheet_name=2) overlaps
#
# calc = len(list_x) - len(overlaps_z)
# calc2 = len(list_y) - len(overlaps_z)
#
# v = venn2(subsets = (calc, calc2, len(overlaps_z)), set_labels = ('SF_BF Total Genes: 248', 'SS_SB Total Genes: 148'))
# v.get_patch_by_id('A').set_color('yellow')
# v.get_patch_by_id('B').set_color('red')
#
# c = venn2_circles(subsets = (calc, calc2, len(overlaps_z)), linestyle = 'solid')
#
# plt.title('SF_BF vs. SS_SB')
# plt.show()


# #3 set Venn diagram for SS_SB vs. SS_BB vs. BS_BB
# import pandas as pd
# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib_venn import venn3, venn3_circles
# plt.figure(figsize=(8,7))
#
# #Read the data frame three times and assign variable to different sheets
# df = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name = 1)
# df1 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name = 2)
# df2 = pd.read_excel('/Users/kevinvela/Dropbox/Imperial_College_London/Year_3/FYP/Dissertation/Kev/Gene_Drive_Targets/Upregulated_Genes.xlsx', sheet_name = 4)
#
# list_1 = df['gene_id'] #Reads SS_SB sheet
# list_2 = df1['gene_id'] #Reads SS_BB sheet
# list_4 = df2['gene_id'] #Reads BS_BB sheet
#
# overlaps = list(set(list_1) & set(list_2)) #SS-SB vs.SS_BB overlaps
# overlaps2 = list(set(list_1) & set(list_4)) #SS_SB vs. BS_BB overlaps
# overlaps3 = list(set(list_2) & set(list_4)) #SS_BB vs. BS_BB overlaps
# overlaps4 = list(set(list_1) & set(list_2) & set(list_4))#SS_SB vs. SS_BB vs.BS_BB overlaps
#
# calc = len(list_1) - len(overlaps) - len(overlaps2) + len(overlaps4)
# calc2 = len(list_2) - len(overlaps) - len(overlaps3) + len(overlaps4)
# calc4 = len(list_4) - len(overlaps2) - len(overlaps3) + len(overlaps4)
#
# v = venn3(subsets = (calc, calc2, len(overlaps), calc4, len(overlaps2), len(overlaps3), len(overlaps4)), set_labels = ('SS_SB Total Genes: 148', 'SS_BB Total Genes: 150', 'BS_BB Total Genes: 465',))
#
# c = venn3_circles(subsets = (calc, calc2, len(overlaps), calc4, len(overlaps2), len(overlaps3), len(overlaps4)), linestyle = 'solid')
#
# plt.title('SS_SB vs. SS_BB vs. BS_BB')
# plt.show()
