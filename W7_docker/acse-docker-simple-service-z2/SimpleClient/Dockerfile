# Java build phase
FROM gradle:4.6-jdk8-alpine AS build
COPY --chown=gradle:gradle . /usr/local/src/SimpleClient
WORKDIR /usr/local/src/SimpleClient
RUN gradle war

# Assemble final image
FROM jboss/wildfly:12.0.0.Final
COPY --from=build /usr/local/src/SimpleClient/build/libs/SimpleClient*.war /opt/jboss/wildfly/standalone/deployments/
RUN /opt/jboss/wildfly/bin/add-user.sh admin "docker#admin" --silent
EXPOSE 8080 9990
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
