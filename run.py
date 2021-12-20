import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.main.configs.http_server_config:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        debug=True
    )
