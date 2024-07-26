### **Coding Test for Full Stack Developer Role at VenturesSky**

**Section 1: Backend Development (Python & Django)**

**Task 1: Django Model and API Endpoint**

* **Problem**: Create a Django model for a `Restaurant` with fields `name`, `address`, `phone_number`, and `rating`. Implement a RESTful API endpoint to create and list `Restaurant` instances.  
* **Instructions**:  
  * Define the model in `models.py`.  
  * Create a serializer for the model.  
  * Implement the API views and URL routing.  
* **Evaluation Criteria**: Correct model definition, functional API endpoint, and proper use of Django REST framework.

**Task 2: Data Processing with Python**

* **Problem**: Write a Python function that takes a list of orders (each order contains `item_name`, `quantity`, and `price_per_item`) and returns the total revenue.  
* **Instructions**:  
  * Define the function with appropriate parameters.  
  * Ensure it handles edge cases (e.g., empty list, invalid input).  
* **Evaluation Criteria**: Correct computation, efficient code, and handling of edge cases.

#### **Section 2: Frontend Development (React)**

**Task 3: React Component**

* **Problem**: Create a React component that fetches and displays a list of restaurants from an API endpoint.  
* **Instructions**:  
  * Use functional components and hooks (e.g., `useState`, `useEffect`).  
  * Display the restaurant name and rating in a list format.  
  * Handle loading and error states.  
* **Evaluation Criteria**: Proper use of hooks, clean and functional component, and correct handling of states.

**Task 4: Interactive Form**

* **Problem**: Create a React form to add a new restaurant with fields `name`, `address`, `phone_number`, and `rating`. On form submission, send a POST request to the API to create the restaurant.  
* **Instructions**:  
  * Use controlled components for form handling.  
  * Validate form inputs (e.g., required fields, valid rating range).  
  * Show a success message on successful submission.  
* **Evaluation Criteria**: Form handling, validation, and API interaction.

#### **Section 3: Mobile Development (Flutter)**

**Task 5: Flutter App**

* **Problem**: Create a simple Flutter app with a screen that lists restaurants. Each item should display the restaurant's name and rating.  
* **Instructions**:  
  * Use a `ListView` to display the list.  
  * Fetch data from a mock API endpoint.  
  * Handle loading and error states.  
* **Evaluation Criteria**: Proper use of Flutter widgets, API fetching, and state management.

#### **Section 4: Database Management (PostgreSQL)**

**Task 6: SQL Query**

* **Problem**: Given a PostgreSQL database with a `restaurants` table, write an SQL query to find the top 5 highest-rated restaurants.  
* **Instructions**:  
  * Write the SQL query to retrieve the necessary information.  
  * Ensure the query is optimised for performance.  
* **Evaluation Criteria**: Correctness and efficiency of the query.

#### **Section 5: Protocols and Real-Time Data (MQTT, gRPC, Redis)**

**Task 7: MQTT Protocol**

* **Problem**: Write a Python script to publish and subscribe to an MQTT topic. The topic is `restaurant/orders`.  
* **Instructions**:  
  * Use the `paho-mqtt` library.  
  * Implement the publisher and subscriber functions.  
* **Evaluation Criteria**: Correct use of the MQTT protocol and proper message handling.

**Task 8: gRPC Service**

* **Problem**: Create a simple gRPC service in Python that defines a `RestaurantService` with a method `GetRestaurant` that takes a `RestaurantID` and returns restaurant details.  
* **Instructions**:  
  * Define the service in a `.proto` file.  
  * Implement the server and client in Python.  
* **Evaluation Criteria**: Correct service definition, server implementation, and client interaction.

**Task 9: Redis Caching**

* **Problem**: Write a Python script to cache restaurant details using Redis. If the details are not in the cache, fetch from a mock database and store them in Redis.  
* **Instructions**:  
  * Use the `redis-py` library.  
  * Implement caching logic with expiration.  
* **Evaluation Criteria**: Proper use of Redis for caching and efficient data retrieval.

