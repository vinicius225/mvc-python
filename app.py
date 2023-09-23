from fastapi import FastAPI
import uvicorn

from Controllers.usuarios_controller import rotas as rota_usuario

app = FastAPI()



app.include_router(rota_usuario, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)