## Usage
How to launch our app.  
```
Step 1. Install docker desktop on your computer
Step 2. open terminal from directory
Step 3. create in the same directory .env with OPENAI_API_KEY=TOKEN and replace TOKEN with your GPT token
Step 4. Log in docker using command "docker login" in terminal (you shall create account before and log in in docker desktop application)
Step 5. in terminal run command: "docker pull dkddjdjjfjdj/anki-deck"
Step 6. launch any vpn. It won't work without it because OpenAi restricted access to Russia 
Step 7. then in terminal run command: "docker run --env-file .env -p 8000:8000 dkddjdjjfjdj/anki-deck"
Step 8. in browser open application by going on this link: "localhost:8000/anki_deck/"
Link to the Docker Hub: "https://hub.docker.com/repository/docker/dkddjdjjfjdj/anki-deck/general"
``` 
