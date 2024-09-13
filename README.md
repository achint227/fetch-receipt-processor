# Receipt Processor

A webservice that fulfils the documented API provided in [api.yml](./api.yml) file.

## Description

This project is a FastAPI application that processes receipts. It includes endpoints for submitting receipts for processing and retrieving points awarded for receipts.

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/achint227/fetch-receipt-processor.git
    cd fetch-receipt-processor
    ```

2. Ensure you have Docker and Docker Compose installed on your machine.

3. Build and start the Docker containers:
    ```sh
    docker-compose up
    ```

4. The API should be running on `http://127.0.0.1:8000`.

5. To view the automatically generated API documentation, navigate to:
    - Swagger UI: `http://127.0.0.1:8000/docs`
    - ReDoc: `http://127.0.0.1:8000/redoc`

    The documentation also supports testing the endpoints


## Conclusion

This project was created with the help of [fastapi-code-generator](https://github.com/koxudaxi/fastapi-code-generator) and the API definitions file. This approach has several advantages:

- **Speed**: Quickly generate boilerplate code, saving time on initial setup.
- **Consistency**: Ensures that the generated code adheres to a consistent structure and style.
- **Accuracy**: Reduces the likelihood of human error.
- **Documentation**: Automatically generated interactive API documentation with Swagger UI and ReDoc.

### Future Improvements

- **Database Integration**: Add support for persistence. Currently the data is stored in an ephemeral in-memory hashmap aka dictionary.
- **Async Processing**: Implement asynchronous processing using a message queue (e.g., RabbitMQ, Kafka) to process receipts.

