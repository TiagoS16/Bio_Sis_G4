from cobra.io import read_sbml_model
import pandas
from time import time

import cobra.test
from cobra.flux_analysis import (
    single_gene_deletion, single_reaction_deletion, double_gene_deletion,
    double_reaction_deletion)

handle = open('1gene_deletions.txt', 'r')
result = handle.readlines()
genes = list(map(lambda x:x.strip(),result))


model = read_sbml_model('iML1515.xml')
model.solver = 'cplex'
model.reactions.EX_glc__D_e.bounds = (-15.0, 100000.0)
model.reactions.EX_o2_e.bounds = (-20,1000)

model_bounds = {r.id:(r.lower_bound, r.upper_bound) for r in model.reactions}

def restore_bounds():
    for r in model.reactions:
        r.lower_bound, r.upper_bound = model_bounds[r.id]

print('complete model: ', model.optimize())
for i in genes:
    restore_bounds()
    model.genes.get_by_id(i).knock_out()
    print(i, 'knocked out: ', model.optimize())


'''
deletion_results = single_gene_deletion(model)
deletions = open('del_five_gene_list.txt', 'w')
for i in deletion_results:
    deletions.write(str(i) + '\n')
deletions.close()
'''