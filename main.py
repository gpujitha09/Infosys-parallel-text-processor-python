from chunker import chunk_text
from processor import run_parallel
from db import init_db

def load_text():
    with open("data/reviews.txt", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    init_db()
    text = load_text()
    chunks = list(chunk_text(text))
    results = run_parallel(chunks)
    print("Total chunks processed:", len(results))
