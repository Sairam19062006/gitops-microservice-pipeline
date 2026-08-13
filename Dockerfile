# Multi-stage build for security & performance
FROM python:3.11-slim AS base
WORKDIR /app
COPY app.py .

FROM python:3.11-slim AS runtime
WORKDIR /app
COPY --from=base /app/app.py .

# Run as non-root user for security best practices
USER 10001
EXPOSE 8080

CMD ["python", "-u", "app.py"]
