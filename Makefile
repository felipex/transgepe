build:
	docker build -t streamlit .

run2:
	docker run --rm -p 8501:8501 \
		--expose 8501 \
		--mount type=bind,source=$(PWD)/app,target=/app \
		--name streamlit \
		streamlit
run:
	docker run --rm -p 8501:8501 \
		--expose 8501 \
		--name streamlit \
		streamlit

