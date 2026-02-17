from concurrent.futures import ThreadPoolExecutor
from rules import score_text
from db import store_result

def process_chunk(chunk):
    score = score_text(chunk)
    store_result(chunk, score)
    return score

def run_parallel(chunks):
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(process_chunk, chunks))
