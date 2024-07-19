<h1 align="center" style="border-bottom: none">
    <b>
        <a href="https://www.google.com"> Smart Grid Management </a><br>
    </b>
    ⭐️Machine Learning and Clean Energy⭐️ <br>
</h1>

# [`Website link`](http://www.google.com)  [`Demo video link `](http://www.google.com) [`Other links `](http://www.google.com) 


<div style="display: flex; flex-wrap: wrap;">
    <img src="https://raw.githubusercontent.com/Aakash-shetty/smart-grid-management/main/Images/Solar-Power-Monitoring-Control.jpg" alt="Image 0" style="width: 50%; margin: 10px;">
    <img src="https://raw.githubusercontent.com/Aakash-shetty/smart-grid-management/main/Images/img1.png" alt="Image 1" style="width: 50%; margin: 10px;">
    <img src="https://raw.githubusercontent.com/Aakash-shetty/smart-grid-management/main/Images/img2.png" alt="Image 2" style="width: 50%; margin: 10px;">
    <img src="https://raw.githubusercontent.com/Aakash-shetty/smart-grid-management/main/Images/img3.png" alt="Image 3" style="width: 50%; margin: 10px;">  
</div>

## Problem statement 
The world is confronted with an escalating energy crisis, characterized by surging demand, dwindling supply, and mounting environmental apprehensions. Conventional energy grids, burdened by inefficiencies and incapacity, struggle to address the exigencies of the modern era.
## About the project
Our solution advocates for the implementation of an AI-powered (Machine Learning based) system tailored for smart grid management. By harnessing the capabilities of machine learning, optimization algorithms, and big data analytics, we aim to revolutionize energy distribution processes and mitigate the carbon footprint. 
**Machine Learning for Demand Prediction**: Leveraging predictive models to anticipate energy demands accurately.
**Optimization Algorithms for Real-Time Distribution**: Employing algorithms to optimize energy allocation in real-time scenarios for efficient energy distribution.
**Big Data Analytics for Renewable Energy Integration**: Utilizing advanced analytics to seamlessly integrate renewable energy sources into the grid.
## Essence of this project ##
few images 
as shown in the images there is a lot of empowerment in the energy sector thus raising the installation quantity of the solar pv cells (Utility level, commercial level, industrial level) which is a major problem solver (energy crises) but it comes at a cost.
the cost of integration challenges , management challenges , security, advancement, etc...
Here are the solutions to mitigate these problems to implement the smart grid management system
**1.Integration Challenges**: The solar PV cells power generation was a intermitent power generation which means it is not a constant power generation(consistently). So integrating the solar power into the existing online grid is a tedious and very difficult task involving heavy engineering. So instead of directly exporting the power we propose a intermediate phase where the generated power was stored and made synchronize with the grids current wave phases. The intermediate phase is the heart of integrating the renewable energy and traditional grid, so it should definitely have the major data corresponds to making inttelligent decisions. So given the machine Learning predicted output of total power generation of the day  by our Machine Learning model, the intermediate phase will efficiently integrate with having knowledge of past exported amount, present exporting amount and future generation amount of electricity.                                                            
**2.Distribution Challenges**: The adoption of renewable energy, espically solar pv will iteslf decrease the amount of energy losses happening at the transformers and many other converters by directly generating the power we want at the intermedaite phase of integration. By using the proper distribution algorithms we can also decrese the transmission losses and can acheive the optimal distribution also meeting the energy demand of the world in a more efficient mannar.        
**3.Management challenges**:There is an incresing demand for electricity and the generation of the electricity by fossile fuels was decresing and the renewable energy resources were increasing, but the integration of these two energies and management of such a heavy demand supply was very difficult. Adopting these changes within a short period of time is difficult and the adoption over a large network of well established traditional grid was very difficult
## Technical implemntaion:  
The whole proble of smart grid management was divided into 3 subparts
- Future prediction of solar power generation using Machine Learning techniques
- Efficient energy distributio using Intelligent Distribution Algorithms
- User Interface to manage and visualize the Intelligent Decisions of the grid


## Techstacks used 
`sci-kit learn` , `streamlit` , `python` 

## How to run locally 
If you want you can run this program in the python virtual environment
```
python -m venv myenv
myenv\Scrits\activate.bat
```
- step 1 : clone the repo and istall 
```
pip install scikit-learn
pip install joblib
pip install streamlit
```
or 
` pip install -r requirements.txt`

-running the code 
`streamlit run app.py`

# What's next ?
As of now only the Machine Learning was implemented in this project and an extensive research on SGMS (Smart Grid Management System) was ongoing. We will very soon implement the intelligent algrithms to distribute the energy efficiently by minimising the losses.
There is already a intemediate phase of energy integration exists , we should be minimizing the cost and engineering before our next update.

## Declaration
We confirm that the project showcased here was either developed entirely during the hackathon or underwent significant updates within the hackathon timeframe. We understand that if any plagiarism from online sources is detected, our project will be disqualified, and our participation in the hackathon will be revoked.
