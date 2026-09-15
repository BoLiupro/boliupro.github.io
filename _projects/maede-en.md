---
title: 'MAEDE: Graph Diffusion for Mobility'
project_id: maede
lang: en
permalink: /projects/maede/
translation: /zh/projects/maede/
description: Probabilistic forecasts of regional private-car activity, guided by temporal structure and urban context.
---

## Overview
MAEDE forecasts Arrive–Stay–Leave activity at the regional level. A conditional graph diffusion model captures uncertainty, while multiple temporal granularities guide the generation of coherent activity patterns.

## Method
- **Urban context:** satellite imagery and LLM-generated descriptions are aligned through contrastive learning.
- **Temporal structure:** multi-granularity guidance combines long-term trends with short-term fluctuations.
- **Probabilistic forecasting:** the diffusion process models the joint distribution of regional activity.

## Results
The published study reports improvements of over **6.8% in RMSE** and **14.8% in CRPS** against the compared baselines. Cross-city evaluations examine generalization across urban environments.

The code repository contains the representation, self-guidance, and diffusion components needed to explore the method.
