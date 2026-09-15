---
title: Enterprise asset extraction based on knowledge graph and agentic Coding
project_id: code-intelligence
lang: en
permalink: /projects/code-intelligence/
translation: /zh/projects/code-intelligence/
description: An ongoing research pipeline that connects business functions, rules, APIs, code, and tests in
  an enterprise knowledge graph, providing traceable context for coding agents.
---

## Overview
Enterprise applications contain reusable knowledge across requirements, business rules, interfaces, source code, and tests. A coding agent needs to understand how these pieces fit together before it can reliably reuse an existing capability. This ongoing collaboration with **Hunan University and China Unicom** studies how to turn scattered software assets into a structured, retrievable knowledge base.

## From software assets to a knowledge graph
The current design starts with an application's business modules and builds a **function inventory** from requirements and design documents, OpenAPI / Swagger definitions, database schemas, frontend pages, backend code, and test cases. Each function is linked to its inputs, outputs, rules, and implementation resources.

We organize these records using nine entity types: **Module, Function, Capability, Business Rule, API, Data Object, UI Component, Code Entity, and Test Case**. Normalization and deduplication help identify shared services and reusable capabilities across modules. A Neo4j property graph then connects the entities into a traceable chain from a business requirement to its implementation and tests.

Relationships are grounded first in explicit evidence, such as interface definitions and code calls. LLM assistance is reserved for interpreting relationships expressed implicitly in natural-language documents. This makes the provenance of retrieved context part of the design.

## A concrete reuse scenario
The proposal uses an office-automation application as an illustrative case, covering leave requests, expense reimbursement, and access permissions. Starting from an expense-approval function, an agent could retrieve its approval rules, API, data model, page component, service method, and associated tests. Shared approval, permission, and notification capabilities could then provide context for implementing a new procurement workflow.

## Research direction and current stage
Since July 2026, I have also been investigating repository-level retrieval and code completion with **RepoBench** and **CodeScaleBench**, studying approaches including **UnixCoder, RepoHyper, and RepoSkein**. This complements the enterprise-asset work by examining which repository context is useful for downstream coding tasks.

The knowledge-graph pipeline is an evolving research design. The next step is to evaluate whether its retrieved evidence supports more faithful code generation, modification, and test construction in the target application scenarios.
