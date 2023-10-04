# dsp-at2-24993747
# Currency Converter Streamlit WebApp

## Author
Name: Shivam Arora
Student ID: 24993747

## Description

The Currency Converter application seamlessly integrates with the renowned open-source API, Frankfurter. This API serves as a reliable source of currency conversion rates between two selected countries. By leveraging the power of Frankfurter, our app effortlessly retrieves the necessary data by passing user-selected parameters chosen from a predefined set of options.

Once the user makes their selections, the app performs further computations by invoking specific functions. This process results in the presentation of not only the current conversion rates but also the converted amount, along with the inverted rate for added convenience.

One exceptional feature that sets our app apart is its ability to perform currency conversions based on historical data. Users have the option to input any date from the past, allowing them to check historical conversion rates. The app then takes this historical data into account when computing the converted amount, providing users with a comprehensive view of currency trends over time.

One of the challenges I encountered was effectively harnessing the capabilities of the API to suit our specific requirements. This API offers a range of functionalities, including providing rates and converted amounts based on the data passed to it. To optimize our application, I leveraged the API's full potential, thereby minimizing the need for additional external calculations. This strategic utilization allowed us to streamline the currency conversion process and deliver a more efficient user experience.

This application possesses significant growth potential in the future. I have ambitious plans to enhance its capabilities, making it even more valuable to users. Some of the upcoming features include the integration of visualizations to illustrate currency conversion rate trends. Additionally, I am considering implementing a regression model to predict future rates, a feature that will be rigorously validated with our extensive data.

To boost user engagement and interaction, we are exploring the concept of a gamified version of the app. In this version, users can choose between selecting currencies from an existing list of countries or interactively selecting them on a world map. This interactive and user-friendly approach will not only make the app more enjoyable but also encourage users to return and explore its features repeatedly. Our vision is to create an evolving and enriching experience for all our users.

## How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>
Sure, here are the instructions in a point format:

1. **IDE and Python Setup**:
   - Make sure you have an IDE (e.g., Visual Studio Code) and Python installed (Python 3.8 or above).

2. **Folder Extraction**:
   - Extract the contents of the provided zip folder.
   - Open the extracted folder in your chosen IDE (Visual Studio Code is recommended for a smoother experience).

3. **Library Installation**:
   - Install the required libraries using the provided `requirements.txt` file.
   - Open a terminal/command prompt and run the following command:
     ```
     pip3 install -r requirements.txt
     ```

Python 3.9.13
Streamlit, version 1.27.0
All other packages used are inbuilt in python.

## How to Run the Program

1. **Running the App**:
   - Create or open a terminal within your IDE.
   - Run the app using one of these commands:
     ```
     streamlit run .\.venv\app.py
     ```
     or
     ```
     streamlit run /path/to/app.py
     ```

2. **Accessing the Web App**:
   - Open your web browser and navigate to the app's URL to start using the web application.

## Project Structure
The main folder named currency converter has 4 major files and other libraries installed. The four major python files ehich have our code are:

app.py:

app.py serves as the central hub of our application. It orchestrates all other components and functions. This file contains the primary user interface (UI) code that makes our web app accessible and engaging for users. It leverages functions from other files to present the web app's interface.

api.py:

In api.py, we have encapsulated the logic for making API requests. It includes a function responsible for calling various APIs and retrieving data. This data, irrespective of the source API, becomes accessible for further processing. Other functions across the application utilize this data for various computations.

frankfurter.py:

frankfurter.py plays a pivotal role in our application, offering three significant functions. It relies on the methods provided in api.py to fetch data. This file provides valuable functionalities such as obtaining the list of currencies, retrieving the latest conversion rates for selected countries, and even accessing historical exchange rates.

currency.py:

Within currency.py, we focus on formatting data for presentation in the web app. This file is responsible for rounding off currency rates and constructing informative statements. It plays a vital role in generating the content users see on the web app, including conversion rates, amounts, currency values, and relevant dates.

## Citations
https://github.com/hakanensari/frankfurter.git
