# Heavy-ion collisions on the OSG -- heavy quark sector

Workflow for heavy-ion collisions: heavy quark sector (hic_HQ).
- This simulation is based on heavy quark improved Langevin dynamics, coupled with a event-by-event hydrodynamical model to describe the evolution of Quark-Gluon Plasma (QGP) that's created in ultra-relativistic heavy-ion collisions. 
    - Most of the medium evolution workflow are inherited from work done by Jonah Bernhard heavy-ion collision simulations [hic-eventgen](https://github.com/Duke-QCD/hic-eventgen.git). 
    - The improved Langevin dynamics of heavy quarks is based on work done by ShanshanCao
- The purpose of this simulation is to analyze the heavy quark transport/diffusion coefficient in QGP medium using a state-of-art Bayesian inference.
- This repository includes script to run the events locally, on HTC: Open Science Grid, HPC: NERSC and Cloud computing: Chameleon. To check the `container` option (which is recommended as easy port and easy reproduce), please check other repository [hic-HQ](https://github.com/Yingru/hic_HQ).


## 1. Physics Models
To clone the repository and use the freestreaming version
```
git clone --recursive https://github.com/Yingru/hic_HQ-osg.git
git checkout freestreaming
git submodule init
git submoudle update
```

Updated Freestreaming version:
The heavy quark evolution in heavy-ion collisions is seperated in the following stages:
 - trento -- initial condition (generating initial energy/entropy density, and binary collision density)
 - freestream -- pre-equilibirum stage evolution (ideal hardon gas)
 - VISHNU -- OSU hydro, a 2+1D hydrodynamics 
 - diffusion -- improved Langevin diffusion model for describing heavy quark in-medium propagation
 - frzout -- particlization of soft sectors from hydrodynamical description to miscroscopic description
 - fragPLUSrecomb -- hadronization model for heavy quarks hadronize into heavy hadrons
 - UrQMD -- hadronic stage afterbuner and rescattering

## 2. Installation
- Locally
- Open Science Grid
- NERSC
- Chameleon


## 3. Run events
The pipeline of event run can be found in the python script [run-events_cD.py](https://github.com/Yingru/hic_HQ-osg/blob/master/models/run-events_cD.py)

To run one event, you can either install the **run-events_cD.py** in the **/bin**, or just execute it as a normal python script. 
[args.conf] contains the arguments that are passed to the event-run. 
The particle lists are saved as a plain **.dat** file, and the processed event information is saved as **.hdf5** file.
Arguments:
- `qhat_args` 
- `diffusion_args`
- `trento_args`
- `vishnu_args`

:warning: additional arguments can be passed to `trento`, 'vishnew`, 'diffusion`. Please check each submodules documents for additional information of the arguments



