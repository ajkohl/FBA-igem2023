# FBA-igem2023

Project Overview: Pathway Optimization using Flux Balance Analysis

Introduction

This repository offers an in-depth narrative of a research project focused on optimizing the biosynthetic pathway from p-coumaric acid to daidzein. The endeavor utilizes Flux Balance Analysis (FBA) models and CobraPy solver, illustrating the journey from initial obstacles through adaptive problem-solving, to significant discoveries that inform subsequent work.

Initial Hurdles and Strategic Shift

The project's commencement was marked by a series of complexities while employing the traditional CobraPy solver. The occurrence of inconsistent values in knockout analysis and confounding results from identical analyses led to a decision to transition to the Gurobi solver. Through Linux terminal commands, the Gurobi solver was integrated into the existing setup, significantly improving the stability and consistency of the analysis results.

Flux Variability Analysis and Model Verification

The shortcomings of a full genome knockout analysis led to the application of flux variability analysis (FVA). This shift allowed the identification and concentration on relevant genes impacting the biosynthetic pathway. To ensure the credibility of this model and chosen method of analysis, sanity checks were performed. Key genes directly involved in the p-coumaric acid to daidzein pathway were knocked out, and the anticipated changes in flux for the targeted enzymes confirmed the model's accuracy and reliability.

Identifying Shortcomings and Adapting Strategies

Despite the improvements made, limitations surfaced while attempting gene knockout analyses on the adjusted model. The flux of target enzymes remained unaffected even when relevant genes were knocked out. This observation indicated potential inadequacies in the baseline model. Thus, it was concluded that a more dynamic FBA and wet lab experimental testing of different reactions would be indispensable to acquire the comprehensive data required to complete the baseline model and accomplish the project's objectives.

The identified challenges motivated a pivot from the FBA tools towards enhancing biological databases such as Wiki and developing machine learning models to address specific components of the project.

Conclusion

This project highlights the dynamic nature of scientific exploration. Overcoming challenges, applying strategic changes, conducting targeted analyses, validating models, and continually adapting based on the findings are integral parts of this journey. It demonstrates the need for an all-encompassing approach in systems biology, combining rigorous data analysis with experimental testing, and the integration of diverse biological knowledge. The progress thus far has been promising, and there is great anticipation for the forthcoming work's outcomes.
