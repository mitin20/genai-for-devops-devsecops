# init docker
```
colima start --cpu 4 --memory 8 --mount $HOME:w || colima kubernetes stop
```

# run OpenHands
```
docker pull docker.all-hands.dev/all-hands-ai/runtime:0.26-nikolaik

sudo docker run -it --rm \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.26-nikolaik \
    -e LOG_ALL_EVENTS=true \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.openhands-state:/.openhands-state \
    -p 3001:3000 \
    --add-host host.docker.internal:host-gateway \
    --name openhands-app \
    docker.all-hands.dev/all-hands-ai/openhands:0.26
```
# open console
```
open http://localhost:3001
```

## running with local models
# go to advance and set
custom_model ollama/llama3.2
base_url = 'http://localhost:11434/v1',
api_key='ollama', # required, but unused

# OR Start Ollama (in a separate terminal)
```
ollama serve
```

# Pull your desired model (example with Mistral)
```
ollama pull mistral
```

# run OpenHands with Ollama
```
docker pull docker.all-hands.dev/all-hands-ai/runtime:0.12-nikolaik
sudo docker run -it --privileged --rm --pull=always \
    -e LLM_API_KEY="ollama" \
    -e LLM_BASE_URL="http://127.0.0.1:11434" \
    -e LLM_OLLAMA_BASE_URL="http://127.0.0.1:11434" \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.12-nikolaik \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -p 3001:3000 \
    --add-host host.docker.internal:host-gateway \
    --name openhands-app \
    docker.all-hands.dev/all-hands-ai/openhands:0.12
```

## colima guys
## First, get Colima's IP address
COLIMA_IP=$(colima list --json | jq -r '.[0].address')
OR
COLIMA_IP=$(docker network inspect bridge -f '{{range .IPAM.Config}}{{.Gateway}}{{end}}')
echo "Colima IP: ${COLIMA_IP}"

#chown -R $USER:$USER /etc/hosts
echo "127.0.0.1   host.docker.internal " >> /etc/hosts

## Then run OpenHands with the correct IP
ex

    --add-host=host.docker.internal:${COLIMA_IP} \

sudo docker run -it --privileged --rm --pull=always \
    -e LLM_API_KEY="ollama" \
    -e LLM_BASE_URL="http://host.docker.internal:11434" \
    -e LLM_OLLAMA_BASE_URL="http://host.docker.internal:11434" \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.12-nikolaik \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -p 3001:3000 \
    --add-host host.docker.internal:${COLIMA_IP} \
    --name openhands-app \
    docker.all-hands.dev/all-hands-ai/openhands:0.12



# prompt test
give me a node hello world app running locally on port 8081 using a docker-compose manifest and include: unit tests, and a github action to run code and docker image scans using  free tools

# useful docker commands
docker kill $(docker ps -q)
docker system prune        
docker system prune --volumes
docker container prune
docker network prune

# clean up
rm -rf ~/.openhands-state