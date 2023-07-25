# FBA-igem2023

Project Overview: Pathway Optimization using Flux Balance Analysis

## Introduction

This repository offers an in-depth narrative of a research project focused on optimizing the biosynthetic pathway from p-coumaric acid to daidzein. The endeavor utilizes Flux Balance Analysis (FBA) models and CobraPy solver, illustrating the journey from initial obstacles through adaptive problem-solving, to significant discoveries that inform subsequent work.

## Initial Hurdles and Strategic Shift

The project's commencement was marked by a series of complexities while employing the traditional CobraPy solver. The occurrence of inconsistent values in knockout analysis and confounding results from identical analyses led to a decision to transition to the Gurobi solver. Through Linux terminal commands, the Gurobi solver was integrated into the existing setup, significantly improving the stability and consistency of the analysis results based on control tests.

## Flux Variability Analysis and Model Verification

The extensive time and computing power requirements of a full genome knockout analysis led to the application of flux variability analysis (FVA). This shift allowed the identification and concentration on relevant genes impacting the biosynthetic pathway. To ensure the credibility of this model and chosen method of analysis, sanity checks were performed. Key genes directly involved in the p-coumaric acid to daidzein pathway were knocked out, and the anticipated changes in flux for the targeted enzymes confirmed the model was working.

## Identifying Shortcomings and Adapting Strategies

Despite the improvements made, limitations surfaced while attempting gene knockout analyses on the adjusted model. The flux of target enzymes remained unaffected even when relevant genes were knocked out. This observation indicated potential inadequacies in the baseline model or perhaps a compensating multi-tiered system that prevented major changes form the loss of a single gene to the target pathway. Thus, since the only way forward that I could think of was dynamic FBA, wet lab experimentation of enzyme fluxes for critical data was deemed an unwise use of their limited time and the FBA project was put aside. The FBA and gene knockout analysis did however produce promising results when the target was set to other pathways within E Coli, indicating potential utilization as an IGEM software development.

The identified challenges motivated a pivot from the FBA tools towards enhancing the Wiki and developing predictive machine learning models to support IHP components of the project.
