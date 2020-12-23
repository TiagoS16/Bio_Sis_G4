from cobra.io import read_sbml_model
import cobra
model = read_sbml_model('iML1515.xml')
print(model.summary())

#envcond = {'EX_O2_e'  : (-5.0, 100000.0),
           #'EX_GLC_e' : (-10.0,100000.0)}

