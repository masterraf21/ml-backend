
dev:
	python server.py

deploy:
	docker compose up -d

down:
	docker compose down

stop:
	docker compose stop