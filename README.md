<h1>ProjectStats – Descriptive Statistics Automation Tool</h1>

### A lightweight desktop app to automate statistical analysis from Excel using Python and VBA.



## Overview

**ProjectStats** simplifies the process of running **descriptive statistics** directly from Excel by combining the flexibility of **Python** with the accessibility of **VBA**. It is designed for analysts and business professionals who want fast, reliable insights without having to code manually.

Built as a functional prototype for automating **data workflows**, this tool is modular, extendable, and ideal for repeated processes in finance, operations, and research.



## Workflow Overview

1. **Import data** from Excel (via macro interface)  
2. **Format and validate** the dataset  
3. **Define variables and type of analysis**  
4. **Run Python logic in the background**  
5. **Display results** back in Excel for review and export  



## Tech Stack

- **Python 3.10+** – core analysis engine  
- **VBA for Excel** – user interface and automation layer  
- **pandas, numpy** – data processing  
- **openpyxl** – Excel file handling from Python  
- **matplotlib** – for data visualizations  



## System Requirements

- Operating System: **Windows 10 / 11**  
- **Microsoft Excel 2016 or later**  
- **Python installed locally**, accessible via system path  
- **Macros enabled** in Excel (`.xlsm` support)  
- Optional: Command line access (for debugging or development use)



## Getting Started

1. Clone or download this repository  
2. Ensure [**uv**](https://github.com/astral-sh/uv) is installed:  
   `curl -Ls https://astral.sh/uv/install.sh | sh`  
3. Run the following inside the project folder:
   ```bash
   uv venv
   uv pip install -r pyproject.toml



## Features

- One-click descriptive statistics from Excel  
- Key metrics: mean, median, standard deviation, IQR, min, max  
- Results displayed directly inside Excel  
- Modular backend, extendable for more advanced statistical analysis  
- Built for business analysts, students, and data-savvy professionals



## Screenshots

<p align="center">
Launch the utility:<br/>
<img src="https://i.imgur.com/EgUOLx8.png" alt="Launch Screenshot"/>
</p>

<p align="center">
Read Data (xlx or csv files):<br/>
<img src="https://i.imgur.com/TMLXVMJ.png" alt="Launch Screenshot"/>
</p>

<p align="center">
Select the headers to be analized:<br/>
<img src="https://i.imgur.com/TBKEBy2.png" alt="Launch Screenshot"/>
</p>

<p align="center">
View the results (use Print to get pdf format):<br/>
<img src="https://i.imgur.com/GR2ODX3.png" alt="Launch Screenshot"/>
</p>






## Roadmap of new features

- [ ] Integrate panel data regression analysis (fixed/random effects)
- [ ] Include a settings window for custom analysis modes



## Author

**José C. Narvaez**  
[LinkedIn](https://www.linkedin.com/in/jcnarvaez2/)  
jcnarvaezpro@gmail.com

---

## License

This project is licensed under the [MIT License](LICENSE).
