PYTHON ?= python3
IMAGE ?= planmytrip-demo
.PHONY: help demo check build run
help:
	@echo "make demo/check: offline example; make build/run: containerized example"
demo:
	$(PYTHON) demo.py
check: demo
build:
	docker build -f Dockerfile -t $(IMAGE) .
run:
	docker run --rm --network none $(IMAGE)
