from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.clients.router import router as clients_router
from app.clients.database import create_clients_table  # 从 database.py 导入

# FastAPI 实例
app = FastAPI()

# 设置 API 路由
app.include_router(clients_router)

# 配置 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源
    allow_methods=["*"],  # 允许所有方法（包括 OPTIONS）
    allow_headers=["*"],  # 允许所有头信息
)

# 在启动时创建客户端表
@app.on_event("startup")
async def startup_event():
    create_clients_table()

if __name__ == "__main__":
    create_clients_table()
