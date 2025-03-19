from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db_connection import Database
from pydantic import BaseModel

app = FastAPI()
db = Database()  # Singleton instance

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await db.get_pool()  # Initialize the pool on startup


@app.on_event("shutdown")
async def shutdown():
    if hasattr(db, '_pool'):
        await db._pool.close()  # Close pool on shutdown


@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        result = db.fetch("SELECT * FROM movies;")
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500