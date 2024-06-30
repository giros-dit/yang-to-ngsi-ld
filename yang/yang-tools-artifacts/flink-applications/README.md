# Testers for Apache Flink applications

For testing Apache Flink streaming applications is not needed to deploy a dedicated Flink cluster. Instead, the applications can be debugged directly on top of the localhost JVM.

This section provides guidelines to run simple _testers_ to be able to test these applications based on [Apache Flink](https://flink.apache.org/), incorporating the utility of deploying [Apache Kafka](https://kafka.apache.org/) as a Docker service from which to read and write the input and output data of the application, as well as the possibility of passing input arguments for the applications from the programming IDE (in this specific case for [Visual Studio Code (VSC)](https://code.visualstudio.com/)).

## Requirements

- Docker (_Tested with version 25.0.4_)
- Docker Compose (_Tested with version v2.24.7_)

## Deploy the tester scenario

To deploy the Docker Compose scenario with Apache Kafka, execute the following command:
```bash
$ docker compose up
```

In case you are interested in running the scenario in background, use the following command:
```bash
$ docker compose up -d
```

Tear the scenario down as follows:
```bash
$ docker compose down
```

## Building the Java projects

Build and compile the Java project of each application:
```bash
$ cd <json/xml>/<application_name>
$ mvn generate-sources
$ mvn clean install
$ mvn install
```

## Kafka service name resolution on localhost

There is a [Kafka issue](https://stackoverflow.com/questions/35861501/kafka-in-docker-not-working) related to the Docker service name resolution from outside.  Applications reading or writing from Kafka running on localhost (e.g., Apache Flink applications) try to access the service using the name `kafka`. An easier solution is configuring the Kafka Docker service to advertise on `kafka` host name  (i.e., configure `KAFKA_ADVERTISED_HOST_NAME=kafka` environment variable in the Kafka Docker service definition) and, because it's exposed on the host machine on `localhost:9092`, adding an entry in `/etc/hosts` for `kafka` to resolve to localhost.

- Kafka Docker service definition on the [docker-compose.yml](docker-compose.yml) file:
```bash
  kafka:
    image: wurstmeister/kafka:latest
    hostname: kafka
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: kafka
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_PORT: 9092
      KAFKA_LOG_DIRS: "/tmp/kafka-logs"
      KAFKA_CREATE_TOPICS: "network-flows:1:1,netflow-driver-output:1:1,netflow-bidiagg-output:1:1,netflow-kpisagg-output:1:1"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    depends_on:
      - zookeeper
    logging:
      driver: none
```

- Kafka service name resolution in `/etc/hosts` file on localhost:
```bash
127.0.0.1	localhost kafka
```

By doing this Kafka can be accessed from both other Docker containers and from localhost.

In Windows10 the process will be the same, but the `hosts` file is normally in:
```
C:\Windows\System32\drivers\etc\hosts
```

## Running and debugging Java applications with input arguments on Visual Studio Code

The Visual Studio Code (VSC) IDE includes different options and settings to run and debug the code. For Java applications, it allows customizing particular [launch configuration options](https://code.visualstudio.com/docs/java/java-debugging#_configuration-options) easily with a JSON file template, such as to define arguments and environmental variables. To do that, from the application workspace location (e.g., [`./json/netflow-driver`](json/netflow-driver/)) you must select the `Add Configuration...` option on the `Run` section of the `VSC` toolbox and select Java as debugger. This action will create a `launch.json` file located in a `.vscode` folder in your workspace. 

The following sample `launch.json` file is an example for the NetFlow Driver Apache Flink Java application:
```bash
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "type": "java",
            "name": "Current File",
            "request": "launch",
            "mainClass": "${file}"
        },
        {
            "type": "java",
            "name": "NetflowDriver",
            "request": "launch",
            "mainClass": "tid.NetflowDriver",
            "projectName": "netflow-driver"
        }
    ]
}
```

In the `configurations` field, you can include different extra configurations for your application. For example,  the `args` option allows specifying the command-line arguments passed to the program. The following  sample `launch.json` file includes the arguments needed to run the NetFlow Driver Apache Flink Java application:
```bash
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "type": "java",
            "name": "Current File",
            "request": "launch",
            "mainClass": "${file}"
        },
        {
            "type": "java",
            "name": "NetflowDriver",
            "request": "launch",
            "mainClass": "tid.NetflowDriver",
            "projectName": "netflow-driver",
            "args": [
                "kafka:9092",
                "network-flows",
                "netflow-driver-output"
            ]
        }
    ]
}
```

The resulting configuration file of the NetFlow Driver Apache Flink Java application for JSON data format is available [here](json/netflow-driver/.vscode/launch.json). For the rest of the Apache Flink Java application, the same procedure is followed.