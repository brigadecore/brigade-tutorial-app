TAG ?= $(shell git rev-parse HEAD)
DOCKER_HUB_ORG ?= jakubborys

run:
	nameko run --config config.yaml products.service

migrations:
	alembic upgrade head

# docker

build:
	docker build -t $(DOCKER_HUB_ORG)/brigade-tutorial-app:$(TAG) .;

push:
	docker push $(DOCKER_HUB_ORG)/brigade-tutorial-app:$(TAG)
