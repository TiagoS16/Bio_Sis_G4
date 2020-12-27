from cobra.io import read_sbml_model

model = read_sbml_model('iML1515.xml')
envcond = {'EX_o2_e': (-20.0, 100000.0), 'EX_glc__D_e': (-15.0,100000.0)}

PRODUCT_ID = 'EX_for_e'
BIOMASS_ID = 'BIOMASS_Ec_iML1515_core_75p37M'

from mewpy.optimization.evaluation import BPCY, TargetFlux
evaluator_1 = BPCY(BIOMASS_ID, PRODUCT_ID, method='pFBA')
evaluator_2 = TargetFlux(PRODUCT_ID)

from mewpy.problems import GKOProblem
problem = GKOProblem(model, fevaluation=[evaluator_1, evaluator_2], envcond=envcond, candidate_max_size=1)

from mewpy.optimization import EA
mutante = EA(problem, max_generations=25, visualizer=True)
mutante_run= mutante.run()
print(mutante_run)
gene_list = open('1_GKO_list.txt', 'w')
for i in mutante_run:
    gene_list.write(str(i) + '\n')

from mewpy.utils.constants import ModelConstants
ModelConstants.RESET_SOLVER = True
