FROM python:3.12-slim
WORKDIR /demo
COPY demo.py ./
USER 65534:65534
CMD ["python", "demo.py"]
