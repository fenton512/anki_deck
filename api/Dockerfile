FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir openai==1.93.0 gtts "uvicorn[standard]"
RUN python -m spacy download en_core_web_sm
EXPOSE 8000
CMD ["uvicorn", "fast_api:app", "--host", "0.0.0.0", "--port", "8000"]