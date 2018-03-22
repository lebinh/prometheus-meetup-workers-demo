.PHONY: server prometheus targets clean

server:
	FLASK_APP=server.py flask run --host 127.0.0.1 --port 8000 --with-threads 2> /dev/null

prometheus:
	prometheus --web.listen-address=127.0.0.1:9090

targets:
	python gen-targets.py > targets.json

clean:
	rm -rf data
	rm -f *.pyc
