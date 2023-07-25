import cobra
import gurobipy

model = cobra.io.load_json_model("/Users/aj/Desktop/Ecoli_TAL_variant.json")

model.solver = 'gurobi'

solution = model.optimize()


# EXPLORATORY ANALYSIS 

# # Print the objective value (e.g., growth rate)
# print("Objective value:", solution.objective_value)

# for reaction in model.reactions:
#     print(reaction.id, solution.fluxes[reaction.id])

# for reaction in model.reactions:
#     print("ID:", reaction.id)
#     print("Name:", reaction.name)
#     print("Reaction:", reaction.reaction)
#     print()

# for metabolite in model.metabolites:
#     if "isoflavanone" in metabolite.name:
#         print("ID:", metabolite.id)
#         print("Name:", metabolite.name)
#         print()

# print(len(model.metabolites))

# def lookupmetid(metabolite_id):
#     # Get the metabolite from the model
#     metabolite = model.metabolites.get_by_id(metabolite_id)

#     # Print the id of the metabolite
#     print(metabolite_id)

#     # Print the name of the metabolite
#     print(metabolite.name)

#     # Print all the reactions that involve this metabolite
#     for reaction in metabolite.reactions:
#         print(reaction.id, ":", reaction.reaction)
    
#     print(" ")
# def optimize(optreactid, solreactid):
#     # Set the objective to the reaction id desired
#     model.objective = 'TAL'

#     # Optimize the model
#     solution = model.optimize()

#     # Print the optimal flux distribution
#     print(solution.fluxes)
#     print(solution.fluxes['HID'])

# lookupmetid('tyr__L_c')
# lookupmetid('cmt_c')
# lookupmetid('cmr_c')
# lookupmetid('ilg_c')
# lookupmetid('lrg_c')
# lookupmetid('thi_c')
# lookupmetid('dzn_c')

# optimize('HID', 'HID')




# for gene in model.genes:
#     if "" in gene.name:
#         print("ID:", gene.id)
#         print("Name:", gene.name)
#         print()


# print(len(model.reactions))


knockoutlist = []

# Set the objective to the reaction producing daidzein
# replace 'daidzein_reaction' with the ID of the reaction producing daidzein
model.objective = 'HID'


#####################################################################################################################################################################

# FLUX VARIABILITY ANALYSIS TO SELECT RELEVENT GENES TO CUT DOWN ON COMPUTING TIME

# def main():

#     # Run FVA
#     fva_result = cobra.flux_analysis.flux_variability_analysis(model)

#     # Identify reactions with variable fluxes
#     variable_reactions = fva_result.loc[(fva_result['minimum'] != fva_result['maximum'])].index.tolist()

#     # Get the associated genes
#     variable_genes = set()
#     for reaction_id in variable_reactions:
#         reaction = model.reactions.get_by_id(reaction_id)
#         for gene in reaction.genes:
#             variable_genes.add(gene.id)

#     # Print the list of genes
#     print(variable_genes)


variable_genes = ['b1101', 'b2296', 'b1107', 'b3196', 'b2663', 'b2235', 'b3265', 'b2926', 'b2943', 'b0928', 'b1602', 'b2280', 'b0684', 'b3731', 'b1319', 'b3875', 'b2465', 'b0431', 'b2415', 'b3089', 'b3831', 'b4151', 'b4036', 'b3733', 'b0721', 'b3919', 'b1723', 'b0030', 'b3612', 'b2458', 'b1849', 'b2379', 'b3430', 'b2750', 'b0474', 'b0123', 'b3429', 'b2290', 'b3059', 'b0185', 'b3735', 'b0207', 'b4077', 'b4153', 'b0114', 'b0875', 'b3380', 'b1781', 'b0429', 'b3390', 'b0040', 'b4067', 'b2779', 'b4090', 'b2937', 'b0241', 'b4111', 'b3290', 'b0842', 'b0512', 'b3001', 'b3432', 'b3747', 'b0767', 'b3035', 'b2796', 'b3281', 'b4208', 'b1207', 'b2964', 'b2497', 'b1033', 'b0957', 'b2920', 'b1761', 'b3781', 'b0729', 'b2518', 'b1015', 'b1773', 'b2975', 'b0126', 'b4054', 'b4069', 'b4152', 'b3770', 'b2329', 'b1801', 'b1291', 'b2388', 'b2316', 'b0432', 'b0724', 'b0008', 'b3737', 'b3116', 'b1363', 'b4238', 'b4395', 'b4025', 'b0728', 'b1006', 'b1300', 'b2265', 'b3956', 'b2215', 'b4154', 'b3603', 'b0070', 'b0469', 'b3553', 'b2288', 'b2282', 'b2935', 'b1621', 'b2297', 'b0339', 'b4383', 'b0755', 'b4267', 'b3266', 'b3115', 'b3428', 'b0593', 'b3849', 'b2464', 'b0394', 'b3350', 'b2279', 'b1216', 'b0508', 'b0516', 'b0116', 'b0212', 'b1131', 'b2416', 'b2287', 'b3256', 'b1492', 'b3255', 'b2407', 'b2281', 'b4237', 'b1692', 'b1603', 'b3572', 'b2417', 'b1276', 's0001', 'b3736', 'b0722', 'b3125', 'b0677', 'b4015', 'b2286', 'b0388', 'b0343', 'b2097', 'b2234', 'b2276', 'b1779', 'b3565', 'b4094', 'b1819', 'b1852', 'b2277', 'b1818', 'b2285', 'b0723', 'b0007', 'b3738', 'b2599', 'b3916', 'b1651', 'b0509', 'b2170', 'b0047', 'b0430', 'b3386', 'b1817', 'b1250', 'b1377', 'b2393', 'b2912', 'b4301', 'b2133', 'b2284', 'b2501', 'b0115', 'b2551', 'b2029', 'b0110', 'b3806', 'b3821', 'b3732', 'b2278', 'b0929', 'b2914', 'b3012', 'b3945', 'b3124', 'b3417', 'b2600', 'b0118', 'b0908', 'b3739', 'b3734', 'b1528', 'b3431', 'b2582', 'b3653', 'b2895', 'b2283', 'b3924', 'b3161', 'b2406', 'b2925']
for gene in variable_genes:
    print(gene)


# Optimize the model without any knockouts and store the original objective value
original_solution = model.optimize()
original_production = original_solution.objective_value

print(len(model.genes))

# Iterate through each gene
for gene in model.genes:
    # Knock out the gene
    gene.knock_out()

    # Optimize the model with the gene knocked out
    knockout_solution = model.optimize()
    
    print("gene knockout result:")
    print(f"{gene.id}:{knockout_solution.objective_value}")
    print("")
    # If daidzein production increased, print the gene
    if knockout_solution.objective_value > original_production:
        original_production = knockout_solution.objective_value
        print(f"Knocking out gene {gene.id} increased daidzein production to {knockout_solution.objective_value}")
        knockoutlist.append(gene.id)

    
    # Reset the gene knockout (important!)
    model = model.copy()

# After looping through all genes, you can analyze the output to see which knockouts increased production

print(knockoutlist)



# pathwayreactionlist = ["DZR","HID","IFS","CHI","CHR","4CL"]
# # Define the reaction ID you are looking for
# for reaction_id in pathwayreactionlist:

#     # Get the reaction from the model
#     reaction = model.reactions.get_by_id(reaction_id)

#     # Print all the genes that are associated with this reaction
#     print(f"Genes associated with reaction {reaction_id}:")
#     for gene in reaction.genes:
#         print(gene.id, ":", gene.name)



# Set the objective to maximize daidzein production
# Replace 'daidzein_reaction' with the ID of the reaction producing daidzein


# model.objective = 'HID'

# # Optimize the model without any knockouts and store the original objective value
# original_solution = model.optimize()
# original_production = original_solution.objective_value

# # Iterate through each reaction
# for reaction in model.reactions:
#     # Knock out the reaction by setting its bounds to 0
#     reaction.lower_bound = 0
#     reaction.upper_bound = 0
    
#     # Optimize the model with the reaction knocked out
#     knockout_solution = model.optimize()
    
#     # If daidzein production increased, print the reaction
#     if knockout_solution.objective_value > original_production:
#         original_production = knockout_solution.objective_value
#         print(f"Knocking out reaction {reaction.id} increased daidzein production to {knockout_solution.objective_value}")
    
#     # Reset the reaction knockout by reloading the model (important!)
#     model = cobra.io.load_json_model("/Users/aj/Desktop/Ecoli_TAL_variant.json")
#     model.objective = 'HID'


####################################################################################################################################################

# all of this produces results:

# (base) amb:iGEM-yale-2023 aj$ python3 FBA.py
# Set parameter Username
# Academic license - for non-commercial use only - expires 2024-03-26

# List of relevent genes to be processed
# b1101
# b2296
# b1107
# b3196
# b2663
# b2235
# b3265
# b2926
# b2943
# b0928
# b1602
# b2280
# b0684
# b3731
# b1319
# b3875
# b2465
# b0431
# b2415
# b3089
# b3831
# b4151
# b4036
# b3733
# b0721
# b3919
# b1723
# b0030
# b3612
# b2458
# b1849
# b2379
# b3430
# b2750
# b0474
# b0123
# b3429
# b2290
# b3059
# b0185
# b3735
# b0207
# b4077
# b4153
# b0114
# b0875
# b3380
# b1781
# b0429
# b3390
# b0040
# b4067
# b2779
# b4090
# b2937
# b0241
# b4111
# b3290
# b0842
# b0512
# b3001
# b3432
# b3747
# b0767
# b3035
# b2796
# b3281
# b4208
# b1207
# b2964
# b2497
# b1033
# b0957
# b2920
# b1761
# b3781
# b0729
# b2518
# b1015
# b1773
# b2975
# b0126
# b4054
# b4069
# b4152
# b3770
# b2329
# b1801
# b1291
# b2388
# b2316
# b0432
# b0724
# b0008
# b3737
# b3116
# b1363
# b4238
# b4395
# b4025
# b0728
# b1006
# b1300
# b2265
# b3956
# b2215
# b4154
# b3603
# b0070
# b0469
# b3553
# b2288
# b2282
# b2935
# b1621
# b2297
# b0339
# b4383
# b0755
# b4267
# b3266
# b3115
# b3428
# b0593
# b3849
# b2464
# b0394
# b3350
# b2279
# b1216
# b0508
# b0516
# b0116
# b0212
# b1131
# b2416
# b2287
# b3256
# b1492
# b3255
# b2407
# b2281
# b4237
# b1692
# b1603
# b3572
# b2417
# b1276
# s0001
# b3736
# b0722
# b3125
# b0677
# b4015
# b2286
# b0388
# b0343
# b2097
# b2234
# b2276
# b1779
# b3565
# b4094
# b1819
# b1852
# b2277
# b1818
# b2285
# b0723
# b0007
# b3738
# b2599
# b3916
# b1651
# b0509
# b2170
# b0047
# b0430
# b3386
# b1817
# b1250
# b1377
# b2393
# b2912
# b4301
# b2133
# b2284
# b2501
# b0115
# b2551
# b2029
# b0110
# b3806
# b3821
# b3732
# b2278
# b0929
# b2914
# b3012
# b3945
# b3124
# b3417
# b2600
# b0118
# b0908
# b3739
# b3734
# b1528
# b3431
# b2582
# b3653
# b2895
# b2283
# b3924
# b3161
# b2406
# b2925
# 1367
# gene knockout result:
# b1377:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmprb7yo1ly.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b2215:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmp4q5t3i8a.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b0929:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmpel_1m26v.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b0241:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmp7h7j34mf.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b4034:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmpaaztdnlf.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b4033:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmp6p97c9tv.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b4032:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmpw34k2013.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b4035:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmpo7a3nnz6.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b4036:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmp4qlut0s1.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b4213:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmps0ckemvk.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b2835:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmpi295i1uk.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b2836:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmpal83_mdc.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b3553:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmpz7p3yazg.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b1134:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmp6kxjfy0h.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b0446:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmp0520yl18.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b1009:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmp6kxyx2ge.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b0954:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmp35ipmzrv.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b0180:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmp2k5idgjq.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b0347:3.05606936416185

# Read LP format model from file /var/folders/6v/hyhcb5812t3db6vvj6md0fxh0000gn/T/tmpcwwpj6pv.lp
# Reading time = 0.01 seconds
# : 1816 rows, 5190 columns, 20462 nonzeros
# gene knockout result:
# b3580:3.05606936416185

# and so on with no change in values based on knockouts

