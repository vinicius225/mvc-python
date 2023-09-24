from fastapi import FastAPI
import uvicorn

from Controllers.usuarios_controller import rotas as rota_usuario
from Controllers.seguranca_controller import rotas as rota_seguranca

app = FastAPI(
    title="API do EPD",
    description="Documentação da API usando Swagger",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json"  #
)



app.include_router(rota_usuario, prefix="/api")
app.include_router(rota_seguranca, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)