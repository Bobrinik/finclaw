include .env
export

COMMIT_HASH := $(shell git rev-parse --short HEAD)


.PHONY: docker
docker: build ## Build docker image
	COMMIT_HASH=$(COMMIT_HASH) docker compose build
	docker tag $(IMAGE):$(COMMIT_HASH) $(IMAGE):latest

.PHONY: up
up:
	COMMIT_HASH=$(COMMIT_HASH) docker compose build

.PHONY: push
push: # pushing docker images
	docker push $(IMAGE):$(COMMIT_HASH)
	docker push $(IMAGE):latest

.PHONY: build
build: clean ## Build python package
	poetry build --format sdist

.PHONY: clean
clean: ## Remove python artifacts
	rm -rf dist/