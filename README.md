# Activation-Mechanism-of-CDK-Family-Using-Their-Concestor

## A brief description on of included files
### input files
Input topologies with five different crystal structures as templates: (The naming is from their corresponding PDB ID)
```
- CDK2/inputFiles/1FIN.prmtop 
- CDK2/inputFiles/3PXF.prmtop 
- CDK2/inputFiles/3PXR.prmtop 
- CDK2/inputFiles/4GCJ.prmtop
- CDK2/inputFiles/5A14.prmtop 
- CMGI/inputFiles/CMGI-1FIN.prmtop 
- CMGI/inputFiles/CMGI-3PXF.prmtop 
- CMGI/inputFiles/CMGI-3PXR.prmtop 
- CMGI/inputFiles/CMGI-4GCJ.prmtop
- CMGI/inputFiles/CMGI-5A14.prmtop 
```
Input coordinates with five different crystal structures as templates:
- CDK2/inputFiles/1FIN.rst
- CDK2/inputFiles/3PXF.rst
- CDK2/inputFiles/3PXR.rst
- CDK2/inputFiles/4GCJ.rst
- CDK2/inputFiles/5A14.rst
- CMGI/inputFiles/CMGI-1FIN.rst
- CMGI/inputFiles/CMGI-3PXF.rst
- CMGI/inputFiles/CMGI-3PXR.rst
- CMGI/inputFiles/CMGI-4GCJ.rst
- CMGI/inputFiles/CMGI-5A14.rst

Parameter files used for the accellerated MD simulations with AMBER:
- CDK2/inputFiles/aMD-1FIN.in
- CDK2/inputFiles/aMD-3PXF.in
- CDK2/inputFiles/aMD-3PXR.in
- CDK2/inputFiles/aMD-4GCJ.in
- CDK2/inputFiles/aMD-5A14.in
- CMGI/inputFiles/aMD-CMGI-1FIN.in
- CMGI/inputFiles/aMD-CMGI-3PXF.in
- CMGI/inputFiles/aMD-CMGI-3PXR.in
- CMGI/inputFiles/aMD-CMGI-4GCJ.in
- CMGI/inputFiles/aMD-CMGI-5A14.in

Parameter files used for the MD simulations with AMBER:
- CDK2/inputFiles/MD.in
- CMGI/inputFiles/MD.in

Scripts needed for adaptive samplings:
- CDK2/inputFiles/CDK2_adaptiveSampling.py
- CMGI/inputFiles/CMGI_adaptiveSampling.py

### result files

## Software used
- AMBER14, which can be obtained from http://ambermd.org/ 
- Python 3.6.7, which can be obtained from https://www.anaconda.com/distribution/
- msmbuilder-3.8.0, which can be accessed using the command line ```conda install -c omnia msmbuilder``` or from http://msmbuilder.org
- mdtraj-1.9.1, which can be accessed using the command line ```conda install -c conda-forge mdtraj``` or from http://mdtraj.org
- matplotlib-2.2.2, which can be obtained from https://matplotlib.org/users/installing.html



