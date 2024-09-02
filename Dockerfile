# Create a virtual environment and install dependencies
# * Only re-execute this step when pyproject.toml changes
FROM python:3.12 AS build-reqs
WORKDIR /app
COPY pyproject.toml pyproject.toml
RUN python -m venv /venv
RUN /venv/bin/pip install .

# Build binary for the package and install code
FROM build-reqs AS build-app
COPY src src
RUN /venv/bin/pip install .

# Copy the virtualenv into a distroless image
# * These are small images that only contain the runtime dependencies
FROM gcr.io/distroless/python3-debian11
COPY --from=build-app /venv /venv
ENTRYPOINT ["/venv/bin/pyskel"]
