# Heavy quark evolution in Heavy-ion Collisions
Workflow for running event-by-event heavy quark transport model on heavy-ion collisions, coupled with an event-by-event soft sector simulation (`trento` + `vishnew hydro` + `UrQMD`).

An improved Langenvin based transport model (collisional + radiative energy loss), where the diffusion coefficients is parametrized as an empirical format, whose parameters will be contraint by a Bayesian comparison between models' calculation and the experimental observation on $D$-meson $R_{\rm AA}$ and $v_2$.

Most of the workflow are inherited from J.Bernhard [heavy-ion collision simulations](https://github.com/jbernhard/heavy-ion-collisions-osg). The improved Langevin model is initially developed by S.Cao and further adapted/modified.

## 1. Physics models:
### 1.1 Initial condition: 
- `trento`: an parametric initial condition for depositing entropy/energy density on the position space. More information please check [Duke-QCD/trento](https://github.com/Duke-QCD/trento)
- `FONLL`: Fixed order plus next-to-leading log QCD calculation of heavy quark production in momentum space. Check [FONLL official website](http://www.lpthe.jussieu.fr/~cacciari/fonll/fonllform.html)

## 1.2 Medium evolution


## 2. To run locally
> require dependencies: `C++11, python3, boost-1.54+ , gsl, cmake-2.8+, hdf5 (C++, fortran, python3)


## 3. To run in high throughout computing system [OSG](http://opensciencegrid.org/)

## 4. To run in cloud computing system
- recommend use `container`
- please check [hic_HQ](https://github.com/Yingru/hic_HQ) for running with a container

## 5. To run in traditional HPC [NERSC]
still developping
