---
title: Agentic Mobility Generation
project_id: motion
lang: en
permalink: /projects/motion/
translation: /zh/projects/motion/
description: A multi-agent system that reasons over evolving user–location graphs to generate community-consistent
  human mobility.
---

## Overview
MOTION treats mobility generation as the evolution of user–location interaction graphs. The system connects individual travel decisions with the community structures that emerge from many people moving through the same city.

## Motivation
Matching individual trajectory statistics does not necessarily preserve community organization. People’s destinations also reflect shared preferences, recurring interactions, and collective rhythms. MOTION makes these structures part of the generation process.

## Method
1. **Community priors.** Detect communities in historical mobility graphs and extract community-conditioned interaction patterns.
2. **User Agents.** Plan mobility, retrieve destination candidates, and reason about individual movements.
3. **Location Agents.** Infer likely arrivals from the perspective of a place and its surrounding community.
4. **Manager Agent.** Coordinate individual and location views, diagnose structural deviations, and send targeted reflection signals to revise decisions.

## Results
The manuscript evaluates the framework on two real-world datasets, examining both mobility realism and community consistency. The related paper contains the experimental comparisons and ablation studies.
