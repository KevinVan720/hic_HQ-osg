Phyiscs
=============================================
This programs solves the linear evolution equation of heavy quarks in a quark-gluon plasma.
Heavy quarks scatter with medium particle via pertrubative matrix-elements.
Between scatterings, heavy quarks undergo diffusive motion with empricical transport coefficient parametring the missing interaction in the above scattering picture.

---------------------------------------------
The linearized Boltzmann equation
---------------------------------------------
The scattering dynamics is governed by the linearized Boltzmann equation,

.. math::
  \partial_t f_Q - \vec{v}\cdot\nabla f_Q  = C_i^{2\leftrightarrow 2}[f_Q] + C_i^{2\leftrightarrow 3}[f_Q]

The collison terms includes both elastic processes and inelastic processes.
The inelastic processes contains not only the induced gluon radiation but also its reverse process, namely meidum gluon absorption.
Therefore the model respect detailed balance and reaches the correct thermal equilibrium.
The corresponding collision integrals are,

.. math::
  C_i^{2 \leftrightarrow 2}[f] &=& \frac{d_i/\nu_i}{2E_1} \int d \Gamma_2 d \Gamma_3 d \Gamma_4 
  \\&& \{f_Q(p_3)f_i(p_4)-f_Q(p_1)f_i(p_2)\}  
  \\&& {(2\pi)}^4\delta^{(4)}(p_{12}-p_{34})  |M_{22,i}|^2 
  \\
  C_i^{2 \leftrightarrow 3}[f] &=& \frac{d_i/\nu_i}{2E_1} \int d \Gamma_2 d \Gamma_3 d \Gamma_4 d \Gamma_k 
  \\&& \{f_Q(p_3)f_i(p_4)f_g(k)-f_Q(p_1)f_i(p_2)\} 
  \\&& {(2\pi)}^4\delta^{(4)}(p_{123} - p_{4k})|M_{23,i}|^2.

Here, :math:`d\Gamma = dp^3/(2\pi)^3/2E` is the Lorentz-invariant momentum phase-space element.
:math:`d, \nu` counts the degeneracy of the incoming medium parton and the symmetry factor of the process repectively. 
The distribution function of light partons :math:`f_i, i=q, \bar{q}, g` are obtained from hydrodynamic calculation. 
Neglecting off-equilibrium correction, there are,

.. math::
  f_{i} = e^{-p\cdot u/T},

where :math:`T(t, \vec{x})` and :math:`u^\mu(t, \vec{x})` are temperatures and four-velocity of the local fluid cell.
To solve the equation in a Monte Carlo approach, we approximate the distribution function of the heavy quark by an enumble of particles.
Then, evolve each particle in a split-step manner, first determine the collision probablity :math:`P=R\Delta t` within a given time step :math:`\Delta t`, provided the collision rate :math:`R`,

.. math::
  R = (2\pi)^3\frac{\delta \int C[f_Q]d\Gamma_Q}{\delta f_Q(p)}
 
If a collision happens according to the probablity `P`, then the details of initial and final states are obtained by sampling the phase space :math:`d\Gamma` s accoding to the differential rate.

----------------------------------------------
Langevin equation
----------------------------------------------
The diffusive motion is solved by the Langevin equation,

.. math::
  \Delta\vec{x} &=& = \vec{p}/E\Delta t\\
  \Delta\vec{p} &=& -\eta_D\vec{p}\Delta t + \vec{\xi}(t)\sqrt{\Delta t}	\\
  \langle \xi_i \xi_j \rangle &=& \hat{p}_i\hat{p}_j\kappa_L + \left(\delta_{ij}-\hat{p}_i\hat{p}_j\right)\kappa_T
  
The heavy quark receives a drag force with drag coefficient :math:`\eta_D` and a random force with equal-time correlator given by the longitudinal and transverse momentum diffusion coefficient.
In the isotropic case :math:`\kappa_L=\kappa_T=\kappa`, the drag coefficient and the momtentum diffusion coefficient has to satisfy the Einstein relation (in the Ito scheme) to reach the correct thermal equilibrium,

.. math::
  \eta_D = \frac{\kappa}{2ET} - \frac{d\kappa}{dp^2}

---------------------------------------------
LPM effect and implementation
---------------------------------------------

Heavy quark experience a single or multiple scatterings may radiate gluons. 
The radiated gluon has a finite formation time :math:`\tau_k \sim 2(1-x)k/({k^2}_\perp+x^2 M^2+(1-x)m_g^2)`. 
During the formation time of the gluon, multiple scatterings lead to destructive intereference that suppresses the gluon radiation spectrum, know as the Landau-Pomeranchuk-Migdal (LPM) effect.

An rigrous treatment of the interference effect is difficult in a Boltzmann equation. 
In this work, we do this effecitvely by modifying the phase space of the radiated gluon by,

.. math::
  \int \frac{d k^3}{(2\pi)^3 2k} \rightarrow \int \frac{d k^3}{(2\pi)^3 2k} 2(1-\cos(\Delta t/\tau_f)),

where :math:`\Delta t` is the time elaspe from the last radiation/absorption.
In the limit of :math:`k_\perp \gg q_\perp` , this perscription goes to the higher-twist formula for meidum induced gluon radiation.









