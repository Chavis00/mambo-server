FROM openjdk:17-alpine

# Create workDir
RUN mkdir code
WORKDIR code

# Copy Code
COPY . .
EXPOSE 25565
ENTRYPOINT java -Xmx5120M -Xms5120M -jar server.jar nogui
#CMD ["java". "-Xmx5120M", "-Xms5120M", "-jar", "server.jar", "nogui"]

