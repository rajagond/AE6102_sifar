# AE6102_sifar
Spring 2023 - Project

##### Title
3D Visualization and Analysis of Seismic Volumes

##### Team Name

Sifar

##### Team Members

|    Name     | Roll Number | Contact              |
| :---------: | ----------- | -------------------- |
| [Adarsh Raj](https://github.com/adarsh0raj)   | 190050004   | 190050004@iitb.ac.in |
| [Koustav Sen](https://github.com/koustav1908) | 190050062   | 190050062@iitb.ac.in |
| [Raja Gond](https://github.com/rajagond)      | 190050096   | 190050096@iitb.ac.in |

##### Abstract
The project aims to provide a comprehensive and interactive visual representation of subsurface geology by creating three-dimensional images of seismic volumes in **MayaVI** library. The project will facilitate a better understanding of subsurface geology by allowing users to interact with the data in a more intuitive and efficient manner utilizing **TraitsUI** library. Visualization of seismic volumes is a very crucial component of interpretation workflows, be it to pick salt domes, interpret horizons, identify fault planes, or classify rock facies.

##### Outline

The project will involve the following steps:

- Collecting seismic data and processing it to generate seismic volumes.
- Converting the seismic volumes into 3D models (numpy arrays) using a specialized python module *segyio*.
- Developing an interactive user interface that allows the user to visualize and manipulate the 3D models, using **TraitsUI**.
- Adding functionalities for analysis using *matplotlib* and **mayaVI** to be able to identify fault planes, classification of rock structures, etc.
- Adding features such as colouring, slicing, and annotation to enhance the interpretability of the data.
- Experiments with popular datasets and demonstration of results of our application corresponding to multiple use cases.

##### Documents

| S.No | Name                                                         | Date of Submission   |
| ---- | ------------------------------------------------------------ | -------------------- |
| 1    | [Project - Grading & Guidelines (2022-2)](docs/Project_Grading_Guidelines_(2022-2).pdf) |                      |
| 2    | [Project Proposal (draft)](docs/project_proposal_draft.pdf)  | 18/02/2023 23:59 IST |
| 3    | [Project Proposal (final)](docs/project_proposal_final.pdf)  | 20/03/2023 09:00 IST |
| 4    | [Project Update-01](docs/project_update1.pdf)                    | 20/03/2023 09:00 IST |
| 5    | [Project Update-02](docs/project_update2.pdf)                    | 03/04/2023 09:00 IST |
| 6    | [Project Update-03](docs/project_update3.pdf)                    | 14/04/2023 23:59 IST |
| 7    | [Final Report Submission](docs/ae6102_project_report.pdf)                    | 03/05/2023 09:00 IST |

##### Datasets

| S.No | Name                                                         | Description                                                  |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [3D seismic data NZPM](https://public.3.basecamp.com/p/JyT276MM7krjYrMoLqLQ6xST) | Seismic data is publicly available and provided by New Zealand Petroleum and Minerals (NZPM)                    |
| 2    | [3D seismic data Netherlands F3 Block](https://github.com/olivesgatech/facies_classification_benchmark#dataset) |  Developed by the OLIVES lab at Georgia Tech                    |
| 3    | [3D seismic data US](https://pubs.usgs.gov/of/2009/1151/data/seismics/segy/) | 3D seismic data provided by the USGS      |

##### Setup
- Clone the repository
    - `git clone https://github.com/rajagond/AE6102_sifar.git`
- On **Ubuntu 22.04** with **python 3.10**, `libxcb-xinerama0` need to be installed with `apt`
    - `sudo apt install python3.10`
    - `sudo apt install python3-pip`
    - `sudo apt install libxcb-xinerama0`
    - `sudo apt-get install texlive-full` (for sphinx documentation in pdf format)
- Install Required Packages
    - `pip install -r requirements.txt`

- Virtual Environment
    - `python3.10 -m venv venv`
    - `source venv/bin/activate`
    - `pip3 install -r requirements.txt`

- Documentation Generation (Sphinx)
    - `sphinx-build --version`
    - `sphinx-quickstart docs`
    - `sphinx-build -b html docs/source/ docs/build/html`
    - `google-chrome docs/build/html/index.html`
    - `cd docs`
    - `make clean html` or `make clean latexpdf`
  
##### References
- https://wiki.seg.org/wiki/Open_data
- http://article.nadiapub.com/IJSIP/vol9_no5/39.pdf
- https://github.com/equinor/segyio