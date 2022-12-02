# DE-IMVO
This project is an implementation of [Study on the optimization of urban emergency supplies distribution paths for epidemic outbreaks](https://www.researchgate.net/publication/361476290_Study_on_the_optimization_of_urban_emergency_supplies_distribution_paths_for_epidemic_outbreaks)

The paper proposes Multiverse Optimizer algorithm using Differential Evolution for optimizing Urban Emergency Supplies Distribution Paths for Epidemic Outbreaks.

Refer Report for details of algorithm.

## Structure of Code:

Proposal, Report and Reseach paper are provided in the repository.

SourceCode folder contains python files which implements the algorithm.

initialParams.py initializes parameters for algorithm.

constraints.py contains function which checks whether given constraints are satisfied.

initialMultiverse.py initializes input to algorithm.

functionValue.py contains the objective function for optimization.

deimvo.py implements the proposed algorithm and gives results.

Clone this repository or download zip file to your system and run following commands in terminal for inference:

1. cd SourceCode
2. python deimvo.py
