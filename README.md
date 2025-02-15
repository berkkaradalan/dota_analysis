# Dota Analysis Backend

This is the backend service for the Dota Analysis project, which provides data analysis and statistics for Dota 2. The backend is built with Python (FastAPI) and connects to a MongoDB database. It leverages caching to speed up responses for frequent requests, and it uses Docker for containerization. The service interacts with the OpenDota API for fetching real-time data and stores the results in its own database for quicker subsequent access.

### Live Demo
https://dotaanalysisfrontend-production.up.railway.app

## Features

- **MongoDB Integration**: The backend connects to a MongoDB database to store and retrieve game-related data.
- **Caching**: Once data is fetched from the OpenDota API, it is stored in MongoDB to speed up future requests for the same data.
- **Logging**: The backend has logging functionality to track events, errors, and API requests.

## Endpoints

The backend provides the following endpoints to fetch Dota 2 related data:

### `/hero/{hero_id}`
Fetches information about a specific Dota 2 hero by `hero_id`. 

### `/favorites/{steam_id}`
Retrieves a user's favorite heroes/items using the `steam_id`.

### `/user/{steam_id}`
Fetches general information about a user using the `steam_id`.

### `/user/winlose/{steam_id}`
Returns the win/loss statistics for a user by their `steam_id`.

### `/match/{steam_id}`
Fetches recent match data for a user using the `steam_id`.

### `/match/detailed/{match_id}`
Retrieves detailed information for a specific match using the `match_id`.

### `/game/item/{item_id}`
Fetches information about a specific game item using the `item_id`.

### `/game/ability/{ability_id}`
Retrieves information about a specific game ability by `ability_id`.

### `/game/mod/{mod_id}`
Fetches information about a game mode using the `mod_id`.

## Workflow

1. When a request is made to any of the above endpoints, the backend first checks its MongoDB database for the requested data.
2. If the data exists, it is returned immediately from MongoDB.
3. If the data does not exist, the backend queries the OpenDota API for the data and stores it in MongoDB for future use.
4. Subsequent requests for the same data are served directly from MongoDB, providing faster response times.

## Using Docker

### Example Build
```bash
docker build -t dota-analysis-backend .
```
### Example Run
```bash
docker run -d -p 8000:8000 -e MONGODB_URL="mongodb+srv://localhost" -e PORT="8080" -e URL="0.0.0.0" --name dota_analysis_backend --network dota_network data_analysis_backend
```