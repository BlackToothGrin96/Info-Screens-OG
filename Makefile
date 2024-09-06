# ==============================
# DEVELOPMENT
# ==============================
# Terminal Command: make dev-build
# If you want to build (or rebuild) the images while pulling from any cached images, then run this command first,
# then run `make dev-run` to start the newly built development containers.
dev-build:
	docker compose -f docker-compose.dev.yml build

# Terminal Command: make dev-build-no-cache
# If you want to rebuild the images and only pull images from Docker Hub (as opposed to pulling images from your cache), 
# then run this command first, then run `make dev-run` to start the newly built development containers.
dev-build-no-cache:
	docker compose -f docker-compose.dev.yml build --no-cache

# Terminal Command: make dev-run
# Start the development containers with full log outputs. If no containers exist, then this command will create new containers.
# The `-f` flag specifies the filename that should be used in the docker compose command.
# To understand how to pass environment variables to docker-compose through the commandline, see this Stackoverflow answer https://stackoverflow.com/a/50991623 along with the comments below it.
# IMPORTANT NOTE ABOUT ENV VARIABLES IN DOCKER COMPOSE: The frontend code is bundled with the Vite bundler. In order to make environment variables available in the frontend code, you have to prefix the environment variable name with "VITE_".
dev-run:
	docker compose -f docker-compose.dev.yml up

# If you have local versions of the `/client/node_modules` and `/client/.svelte-kit` directories (i.e. versions of those directories that were created outside of Docker), then you might have to delete them before running this app inside of Docker containers for development.
dev-run-rm:
	sudo rm -rf client/node_modules client/.svelte-kit && docker compose -f docker-compose.dev.yml up -d

# Terminal Command: make dev-run-daemon
# The `-d` flag will run the app in daemon mode (i.e., in the background).
dev-run-daemon:
	docker compose -f docker-compose.dev.yml up -d

# Terminal Command: make dev-stop
# This will stop and delete any running containers. It deletes containers and networks, but not volumes and images.
dev-stop:
	docker compose -f docker-compose.dev.yml down


# ==============================
# PRODUCTION
# ==============================
# Terminal Command: make prod-build
# If you want to rebuild the images while pulling from any cached images, then run this command first,
# then run `make prod-run` to start the newly built development containers.
prod-build:
	docker compose build

# Terminal Command: make prod-build-no-cache
# If you want to rebuild the images without using the cache, then run this command first,
# then run `make prod` to start the newly built production containers.
prod-build-no-cache:
	docker compose build --no-cache

# Terminal Command: make prod-run
# Start the production containers with full log outputs. If no containers exist, then this command will create new containers.
prod-run:
	docker compose up

# Terminal Command: make prod-run-daemon
# The `-d` flag runs the app in daemon mode (i.e., in the background).
prod-run-daemon:
	docker compose up -d

# Terminal Command: make prod-stop
# This will stop and delete any running containers. It deletes containers and networks, but not volumes and images.
prod-stop:
	docker compose down


# # ==============================
# # TEST
# # ==============================
# # Terminal Command: make run-test
# run-test:
# 	docker-compose -f docker-compose.test.yml up


# # ==============================
# # STAGING
# # ==============================
# # Terminal Command: make run-staging
# run-staging:
# 	docker-compose -f docker-compose.staging.yml up
