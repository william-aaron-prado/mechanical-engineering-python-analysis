# Mechanical Engineering Python Analysis

## Objective

Develop simple Python tools to perform basic engineering calculations
and investigate how selected parameters affect stress and factor of safety.

## Tools Used

- Python
- VS Code
- Matplotlib

## Features

- Lead-screw cross-sectional area calculation
- Simplified axial stress calculation
- Factor of safety calculation
- Parameter study
- Graphical visualization of results

## Engineering Calculations

### Cross-sectional Area

Area = (pi)(r^2)

### Normal Stress

stress=Force/Area

### Factor of Safety

Material strength/applied stress

## Assumptions

- Static loading
- Solid circular section for the simplified lead-screw calculation
- Thread geometry is not explicitly modeled
- Material strength is treated as an assumed educational value
- Friction, torsion, thread shear, stress concentrations, and buckling
  are not included

## Parameter Study

Briefly explain what parameters were varied and what was observed.

![Parameter Study](PARAMETER%20STUDY.png)

## Sample Output

Briefly describe the Day 46 calculator output.

## Results

Summarize the main engineering observation from the parameter study.

## Limitations

This is a basic educational analysis and is not a professional
safety assessment or substitute for detailed mechanical design validation.

## Files

- `day46_lead screw analysis calculator.py` — lead-screw analysis calculator
- `day47_parameter_study.py` — parameter-study script
- `PARAMETER STUDY.png` — generated parameter-study visualization
