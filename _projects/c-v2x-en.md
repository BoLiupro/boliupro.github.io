---
title: Research on C-V2X synchronous positioning based on weak GNSS signal scenario
project_id: c-v2x
lang: en
permalink: /projects/c-v2x/
translation: /zh/projects/c-v2x/
description: A MATLAB simulation study of synchronized roadside units and sensor fusion for vehicle positioning
  when GNSS signals weaken, with comparisons of estimation error and convergence.
---

## Overview
GNSS signals can weaken or disappear as a vehicle enters a tunnel or travels through an obstructed environment. My undergraduate thesis at **Fuzhou University**, advised by **Qinqin Chai**, investigated how roadside infrastructure and complementary sensors could support vehicle positioning in these conditions.

## Synchronization and sensor fusion
The study models roadside units (RSUs) as positioning infrastructure. A master RSU establishes synchronization, with synchronization and cascading links connecting the other units. Position-reference signals provide a common basis for vehicle measurements, as illustrated in the system diagram above.

The MATLAB implementation combines RSU-related measurements with **inertial navigation and auxiliary laser ranging**. Weighted least squares and Kalman filtering support position estimation and the integration of information from different sources.

## Simulation and evaluation
Experiments examine positioning error and convergence as a vehicle enters a tunnel under different motion conditions. The code includes single-point positioning, C-V2X positioning, Kalman fusion, inertial measurements, roadside-unit modeling, noise generation, and repeated-experiment evaluation.

The results characterize performance under the thesis's simulated trajectories and noise assumptions. They provide evidence about the behavior of the estimation pipeline in simulation; field deployment and real-road validation remain further work.

## Engineering outcomes
The project produced a MATLAB simulation codebase and a thesis documenting system assumptions, modeling, and experiments. It also identifies future directions such as stronger treatment of environmental effects and nonlinear motion, and discusses GRU-assisted localization as a possible extension. Source code and the full thesis are available through the buttons above.
