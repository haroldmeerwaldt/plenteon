def serve_dev() -> None:
    """Dev entrypoint: serve the public website with autoreload."""
    import uvicorn
    uvicorn.run("public_website.main:app", reload=True)
