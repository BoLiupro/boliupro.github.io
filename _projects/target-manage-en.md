---
title: Target Characteristic Extraction and Management Software
project_id: target-manage
lang: en
permalink: /projects/target-manage/
translation: /zh/projects/target-manage/
description: A remote sensing software system integrating satellite imagery, extracted characteristics, searchable records, and structured exports.
---

## Overview
Remote sensing workflows bring together imagery from different sensors, associated metadata, and derived characteristics. This project integrates these resources in a browser-based application, connecting image preview and characteristic extraction with searchable records, data maintenance, and standardized exports.

The software supports optical, infrared, hyperspectral, and radar imagery. Its interface brings processing requests, source images, selected image regions, and their resulting records into a shared workflow.

## Main capabilities
- **Request management:** search processing requests and review their status, creation time, and failure information.
- **Image and record review:** preview imagery and inspect the characteristics associated with a selected region, alongside its source-image metadata.
- **Data maintenance:** add, update, query, and remove records, with combined search criteria and paginated results.
- **Structured export:** organize extracted characteristics and associated visual outputs in a consistent format for downstream data exchange.

## Software architecture
The system separates the application, core services, and data layers. A **Vue 3** interface provides request and characteristic management. **Spring Boot** coordinates the application services, while **Python** services handle image preparation and characteristic processing. **Redis** supports session authentication, and a **Kingbase** database stores the managed records.

This separation connects interactive data review with the processing services and persistent storage. The implementation also includes input validation, confirmation for consequential operations, error reporting, and configurable deployment settings.

## Testing and delivery
The November 2025 development summary reports **41 test cases** covering interfaces, functional cooperation, and business data flows, with all cases passing after testing and regression checks. It also records successful inspection on **November 2, 2025** and deployment on **Kylin V10**.

The documented deliverables include the software, requirements and design specifications, a user manual, and test documentation. These are project-level results reported in the supplied development summary.
