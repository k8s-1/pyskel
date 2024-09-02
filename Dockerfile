# Install venv
# Only run when pyproject.toml changes
FROM python:3.12-slim AS build-reqs
WORKDIR /app
COPY pyproject.toml pyproject.toml
RUN python -m venv /venv
RUN /venv/bin/pip install .

# Build binary
FROM build-reqs AS build-app
COPY src src
RUN /venv/bin/pip install .

# Execute binary
FROM python:3.12-slim
COPY --from=build-app /venv /venv
ENTRYPOINT ["/venv/bin/pyskel"]
