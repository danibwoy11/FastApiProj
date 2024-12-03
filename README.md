
Sepsis Prediction API
This project is a FastAPI-based application for predicting the likelihood of sepsis using pre-trained machine learning models. The API supports multiple models and accepts data in CSV format to generate predictions.
________________________________________
Table of Contents
1.	Features
2.	Requirements
3.	Installation
4.	Usage
________________________________________
Features
o	Predict sepsis likelihood using machine learning models: 

o	Logistic Regression

o	Random Forest

o	K-Nearest Neighbors

o	Accepts data in CSV format.

o	Provides clear error messages for invalid inputs.

________________________________________
Requirements
o	Python 3.8 or higher

o	Required libraries: 

o	FastAPI

o	Uvicorn

o	Pandas

o	Numpy

o	Joblib
________________________________________
Installation
1.	Clone the repository:
2.	git clone (https://github.com/danibwoy11/FastApiProj.git)
3.	cd sepsis-prediction-api
4.	Create and activate a virtual environment:
5.	python -m venv env
6.	source env/bin/activate  # For Linux/macOS
7.	env\Scripts\activate     # For Windows
8.	Install dependencies:
9.	pip install -r requirements.txt
10.	Ensure the models folder contains the necessary .pkl files:
    
	models/

	├── Logistic Regression_pipline.pkl

	├── Random Forest_pipline.pkl

	├── K-Nearest Neighbors_pipline.pkl

________________________________________
Usage
1.	Start the API server in your IDE of choice:
2.	uvicorn mainapi:app –reload
 ![image](https://github.com/user-attachments/assets/2f67db8f-9fd6-4f8d-a2e1-6617057ffb51)

3.	Open your browser and navigate to:
4.	http://127.0.0.1:8000
5.	To access the prediction options add a (/docs) to the url above in your browser
 ![image](https://github.com/user-attachments/assets/9ffbb076-f32a-450f-98d6-5c25da47d7d0)
6.	It should show a result page like this
   ![image](https://github.com/user-attachments/assets/96fdff67-1b43-447f-bfab-6c812ff84fba)
7.	Open up the drop-down menu of the Post section
   

8.	Click the try it out to start the process
   ![image](https://github.com/user-attachments/assets/8487e5d5-211e-4956-a5f1-416d59c9ffb7)

   ![image](https://github.com/user-attachments/assets/8c918590-07a6-483c-b16f-98a3f1205762)

10.	Under model pick any of the three models being ‘knn’, 'random_forest' or 'logistic_regression' for example using knn
    ![image](https://github.com/user-attachments/assets/5e379b4e-03a4-4f56-ac9a-27a679cb5483)

11.	In the file section the csv file you want to predict
12.	Now click execute to start your predictions, your result should be a json file that can be downloaded,
    the 0's represents No sepsis and the 1's represents sepsis
    ![image](https://github.com/user-attachments/assets/b03db564-4ffb-4edb-b56b-fb785848f6d5)
 
13.	To start a new one click on reset beside  the cancel option
    ![image](https://github.com/user-attachments/assets/11a2f142-c010-452a-ab53-71ebd459defb)


________________________________________

