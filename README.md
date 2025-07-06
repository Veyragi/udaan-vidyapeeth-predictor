# udaan-vidyapeeth-predictor
🎓 Udaan Vidyapeeth College Predictor (Python & Gemini)
This project is a college admission predictor built using Python. It leverages the Gemini API to provide intelligent insights and predictions based on historical data from CSAB (Central Seat Allocation Board) rounds 1 and 2, as provided by Udaan Vidyapeeth.

🎯 Objective
To accurately predict potential college admissions for students based on their rank, category, and other preferences.

To analyze and identify admission trends from CSAB Round 1 and Round 2 data.

To utilize the Gemini API for processing user queries and generating personalized college recommendations.

To create a user-friendly application that simplifies the college selection process for aspiring engineering students.

🧰 Tools & Technologies Used
Programming Language: Python

Key Libraries: Pandas (for data manipulation), NumPy (for numerical operations), Scikit-learn (for modeling, optional).

AI/API: Google Gemini API (for intelligent search and summarization).

Data Source: CSAB Round 1 & 2 Datasets (.csv/.xlsx).

Development Environment: Jupyter Notebook / VS Code.

📂 Project Structure
Component

Description

college_predictor.py

Main Python script containing the prediction logic and app interface.

cleaned_csab_data.csv

The processed and cleaned dataset used for the prediction model.

requirements.txt

A list of all necessary Python libraries to run the project.

Project_Report.pdf

A detailed document explaining the project's methodology, findings, and process.

README.md

You are here! The summary and guide for this project.

🧠 Key Features & Insights
Rank-Based Prediction: Provides a list of "Safe," "Moderate," and "Ambitious" college choices based on a student's JEE Main rank.

Gemini-Powered Search: Allows users to ask natural language questions (e.g., "Find top NITs for Computer Science under 10000 rank").

CSAB Round Analysis: The model accounts for the shifts in closing ranks between the first and second rounds of CSAB counseling.

Multi-Filter Support: Users can filter predictions based on state, branch preference, and college type (NIT, IIIT, GFTI).

📝 Future Scope & Recommendations
Expand Dataset: Incorporate data from previous years (e.g., 2021, 2022) to identify long-term admission trends.

Web Application: Deploy the predictor as an interactive web application using Streamlit or Flask for easy public access.

Personalized Advice: Enhance the Gemini integration to generate personalized counseling advice for students based on their predicted results.

Visualization: Add data visualizations to show rank trends for popular colleges and branches over the years.

Created by Abhishek Yadav
📧 abhiishekyadav.c@gmail.com
🌐 [LinkedIn](www.linkedin.com/in/Abhiishek-Yadav)
