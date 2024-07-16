<h1>CryptoStalker</h1>

<p>This Cryptocurrency Price Tracking Web App aims to provide users with real-time information about cryptocurrency prices. Leveraging the Django framework, the application will fetch data from a public API and present it in an intuitive and accessible manner.</p>

<h3>Features and Functionalities to be Implemented:</h3>
<pre>
1. Real-time Price Tracking:
•	Display real-time prices of cryptocurrencies fetched from a public API.
•	Update prices dynamically refreshing the page.<br>
2. Cryptocurrency Listings and Details:
•	Provide a comprehensive list of cryptocurrencies with their current prices.
•	Include detailed information such as market cap, volume, circulating supply, and price charts.<br>
3. Search  Options:
•	Enable users to search for specific cryptocurrencies by name or symbol.<br>
4. Responsive Web Design:
•	Ensure the app is responsive and accessible across different devices (desktops, tablets, smartphones).
•	Optimize user experience with a clean and intuitive interface.<br>
5. API Integration:
•	Utilize a public API CoinGecko to fetch cryptocurrency data.
6. Data Visualization with Chart.js
Purpose: Enhance the app's capability to represent cryptocurrency price data through interactive charts visually.
</pre>

<h3>Technologies and Tools Used:</h3>
<pre>• Django Framework: Backend development framework for 
building scalable web applications in Python.
• Python: Programming language used for backend logic 
and integration with APIs.
• HTML/CSS/JavaScript: Frontend technologies for 
creating the user interface and enhancing interactivity.
• Bootstrap or other CSS frameworks: To ensure 
responsive design and consistent styling.
• Public API : External data source for fetching real-time 
cryptocurrency prices and additional information.</pre>

<h3>Components of the Application:</h3>
<pre>1. Front-end Interface:
• Description: This component includes the user interface 
(UI) that users interact with.
• Technologies: HTML, CSS, JavaScript, Bootstrap (or 
another CSS framework).
• Functionality: Displays cryptocurrency prices, charts, 
search/filter options, and user authentication forms.<br>
2. Back-end Server (Django):
• Description: Handles the application's logic, data processing, and
business rules.
• Technologies: Django framework (Python), PostgreSQL 
(or another database).<br>
• Functionality: Manages user authentication, interacts 
with the database to store and retrieve data, and integrates 
with external APIs for real-time cryptocurrency prices.<br>
3. API Integration:
• Description: Integrates with a public API CoinGecko to 
fetch real-time cryptocurrency data.
• Technologies: Python libraries (e.g., requests for API 
calls).
• Functionality: Retrieves up-to-date cryptocurrency prices 
and additional information such as market cap, volume, 
and historical data. Handles API requests and responses 
securely and efficiently.
</pre>


<h3>Explanation of How Different Parts of the System Interact:
</h3>
<pre>1. User Interaction Flow:
• Users interact with the front-end interface to view 
cryptocurrency prices, search for specific 
cryptocurrencies, and perform actions like registration and 
login.
• Front-end sends requests to the Django backend for data 
retrieval and processing.
• Front-end to Backend Communication:
• Front-end communicates with the Django backend through 
HTTP requests (GET, POST) for retrieving data (e.g., 
cryptocurrency prices ) and submitting user actions (e.g.
search).<br>
2. Backend Processing:
• Django backend processes requests from the front-end, 
interacts with the database to fetch or update data (e.g., 
user profiles, cryptocurrency prices), and integrates with 
the API for real-time data retrieval.<br>
3. API Integration:
• Backend interacts with the chosen API (e.g., CoinGecko 
API) to fetch real-time cryptocurrency prices and other 
relevant data.
• It handles authentication (if required), constructs API 
requests, parses responses, and updates the database 
with fetched data.
</pre>

<h3>Some Screenshots of the Project:</h3>
<pre>
![Screenshot 2024-07-15 225529](https://github.com/user-attachments/assets/a88136fe-6f15-4065-976e-c2044b9a2576)
  
</pre>
