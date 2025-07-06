
The system is deployed as follows:

  Frontend: Runs in the user's browser, served via a static web server.
  Backend: FastAPI application running on a server (Dockerized for portability).
  Database: SQLite file stored on the backend server.
  NLP/ML Models: Packaged with the backend, can be containerized for scalability.
  This setup allows easy deployment on the customer’s side, either on-premises or in the cloud.
