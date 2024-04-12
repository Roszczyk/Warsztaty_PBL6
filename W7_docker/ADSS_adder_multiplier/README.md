# Wildfly example

## Using Docker

1. Start simple client and server:
    ```sh
    $ docker-compose up --build
    ```
2. Open web browser: http://localhost:8080/SimpleClient/
3. Start adder service directly, e.g. http://localhost:8081/AddServer/?first=41&second=1
4. Stop simple client and server:
    ```sh
    $ docker-compose down -v
    ```

## Build WAR files directly

```sh
$ ./gradlew assemble
$ ls Simple*/build/libs/*
SimpleClient/build/libs/SimpleClient.war AddServer/build/libs/AddServer.war
```
