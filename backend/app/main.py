from fastapi import FastAPI
app=FastAPI(title="Rayyan Anwar | Multimodal AI Research Lab")
@app.get("/health")
def health(): return {"status":"ok","author":"Rayyan Anwar"}
