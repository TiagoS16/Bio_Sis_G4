from cobra.io import read_sbml_model
import cobra
from mewpy.simulation import get_simulator

#b)
model = cobra.io.sbml.read_sbml_model('iJN746.xml')
print(model.summary()) #products excreted
print('-------------')
opt_model= model.optimize()
obj_model= opt_model.objective_value
print(obj_model)
print('-------------')

model_1 = read_sbml_model('iJN746.xml')
envcond = {'EX_glc__D_e': (-6.3, 100000.0), 'EX_o2_e':(-15.34, 1000)}
simul = get_simulator(model_1, envcond=envcond)
result= simul.simulate(method='FBA')
print(result) #specific growth rate
print('----------------')

#c)
yo= simul.essential_reactions
yoo= simul.essential_genes
print('Reações essenciais:', '\n', simul.essential_reactions)
print('------------')
print('Genes essenciais:', '\n', simul.essential_genes)


yo_1= ''
for i in yo:
    j= i + ', '
    yo_1 += j
print('------------------')
yoo_1= ''
for o in yoo:
    k= o + ', '
    yoo_1 += k

print(yo_1)
print('----------')
print(yoo_1)
