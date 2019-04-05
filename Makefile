TAG ?= $(shell git rev-parse HEAD)
REF ?= $(shell git branch | grep \* | cut -d ' ' -f2)
DOCKER_HUB_ORG ?= jakubborys
CONTEXT ?= docker-for-desktop
ENV_NAME ?= bob

run:
	nameko run --config config.yaml products.service

migrations:
	alembic upgrade head

# docker

build:
	docker build -t $(DOCKER_HUB_ORG)/brigade-tutorial-app:$(TAG) .;

push:
	docker push $(DOCKER_HUB_ORG)/brigade-tutorial-app:$(TAG)

# kubernetes

deploy:
	helm upgrade $(ENV_NAME)-products charts/products --install \
	--namespace=$(ENV_NAME) --kube-context=$(CONTEXT) \
	--set image.tag=$(TAG)

# brigade

run-brigade:
	echo '{"name": "$(ENV_NAME)"}' > payload.json
	brig run kooba/brigade-tutorial-app -c $(TAG) -r $(REF) -f brigade.js \
	-p payload.json --kube-context $(CONTEXT) --namespace brigade
