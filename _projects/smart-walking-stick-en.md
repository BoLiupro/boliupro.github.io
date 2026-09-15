---
title: Walking Stick with Heart Attack Detection
project_id: smart-walking-stick
lang: en
permalink: /projects/smart-walking-stick/
translation: /zh/projects/smart-walking-stick/
description: An Arduino-based wristband and walking-stick prototype combining optical pulse sensing, Bluetooth
  communication, and GSM text alerts for abnormal heart-rate readings.
---

## Overview
This undergraduate team project explored how a connected walking stick and wrist-worn sensor could support everyday health awareness. The prototype brings together **pulse measurement, short-range wireless communication, and text-message alerts** in an embedded system. I participated as a team member in its development.

## Hardware and interaction flow
A **MAX30102 optical pulse sensor** captures the pulse signal, which an Arduino processes into heart-rate readings. Paired **HC-05 Bluetooth modules** transfer these readings between the wristband-side and walking-stick-side Arduino boards. A **SIM900A GSM module** provides the text-message alert channel when the prototype detects an abnormal reading.

The modular design allowed the team to test sensing, board-to-board communication, and messaging separately before integrating the complete flow. The accompanying report documents the circuit, communication setup, and program implementation; the video demonstrates the assembled prototype.

## Prototype evaluation
The project demonstrated pulse acquisition, Bluetooth transmission, and SMS alerts. Evaluation focused on reading stability, the time needed to obtain a stable value, connection behavior, and data transmission between the boards.

The report also records practical limitations: pulse readings needed better speed and accuracy, alerts were limited to one recipient, and GPS positioning was not implemented. The demonstrated outcome is a student heart-rate monitoring and alert prototype; clinical heart-attack detection was not validated.

## What I learned
The project connected hardware integration with human-centered design: a useful wearable system depends on reliable sensing and communication as well as a clear response when an alert is raised. It was an early opportunity to work across sensors, microcontrollers, and a physical assistive device.
