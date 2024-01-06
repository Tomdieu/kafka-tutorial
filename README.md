# Kafka Tutorial

In this repository, we will learn how to use Apache Kafka Producer and Consumer.

## Kafka Installation

Clone the GitHub repository

```bash
git clone https://github.com/Tomdieu/kafka-tutorial.git
```

- Install `docker`
- Install `docker-compose`
- Install kafka by running the following command
    ```bash
    docker-compose up -d
    ```
- Check if the kafka is running
    ```bash
    docker-compose ps
    ```
## Run

- Run the producer
    ```bash
    python main.py <topic>
    ```

- Run the consumer
    ```bash
    python consumer.py <topic1> <topic2>
    ```
