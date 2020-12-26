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
print('Reações essenciais:', '\n', simul.essential_reactions)
print('------------')
print('Genes essenciais:', '\n', simul.essential_genes)

