def greet(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        cleaned = "world"
    return f"Hello, {cleaned}!"
