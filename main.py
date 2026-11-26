from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import supabase

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

@app.get("/productos")
def listar():
    return supabase.table("productos").select("*").execute().data

@app.post("/productos")
def crear(item: dict):
    return supabase.table("productos").insert(item).execute().data
@app.put("/productos/{id}")
def actualizar(id: int, item: dict):
    return supabase.table("productos").update(item).eq("id", id).execute().data

@app.delete("/productos/{id}")
def eliminar(id: int):
    return supabase.table("productos").delete().eq("id", id).execute().data
    @app.put("/productos/{id}")
def actualizar(id: int, item: dict):
    return supabase.table("productos").update(item).eq("id", id).execute().data

@app.delete("/productos/{id}")
def eliminar(id: int):
    return supabase.table("productos").delete().eq("id", id).execute().data