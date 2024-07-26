Section 5: Protocols and Real-Time Data (MQTT, gRPC, Redis)

Task 7: MQTT Protocol

    Problem: Write a Python script to publish and subscribe to an MQTT topic. The topic is restaurant/orders.
    Instructions:
    Use the paho-mqtt library.
    Implement the publisher and subscriber functions.
    Evaluation Criteria: Correct use of the MQTT protocol and proper message handling.

Task 8: gRPC Service

    Problem: Create a simple gRPC service in Python that defines a RestaurantService with a method GetRestaurant that takes a RestaurantID and returns restaurant details.

    Instructions:
    Define the service in a .proto file.
    Implement the server and client in Python.

    Evaluation Criteria: Correct service definition, server implementation, and client interaction.

Task 9: Redis Caching

    Problem: Write a Python script to cache restaurant details using Redis. If the details are not in the cache, fetch from a mock database and store them in Redis.
    
    Instructions:
    Use the redis-py library.
    Implement caching logic with expiration.

    Evaluation Criteria: Proper use of Redis for caching and efficient data retrieval.
