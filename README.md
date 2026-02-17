# Python Parallel Text Handling Processor – Milestone 1

## Project Objective
This project implements a structured text processing pipeline using Python.
The goal is to process large text files in parallel and store analysis results in SQLite.

## Text Type
Product Reviews

## Processing Goal
Perform simple rule-based sentiment scoring using positive and negative word counts.

## Input
A large .txt file containing multiple product reviews.

## Output
Chunk-wise sentiment scores stored in an SQLite database.

## Pipeline Flow
1. Read text file  
2. Break text into chunks  
3. Process chunks in parallel  
4. Apply rule-based sentiment scoring  
5. Store results in SQLite  
6. Display processing summary  

## Architecture
- main.py → Entry point that connects the full pipeline  
- chunker.py → Breaks large text into chunks  
- processor.py → Runs parallel processing on chunks  
- rules.py → Implements rule-based scoring logic  
- db.py → Handles SQLite database storage  

## Milestone 1 Scope
- Defined text type and processing goal  
- Implemented file-based text input  
- Implemented chunking logic for large text  
- Applied parallel processing to actual text chunks  
- Implemented rule-based scoring  
- Stored chunk-wise results in SQLite  
- Connected all modules into one pipeline  

## How to Run
```bash
python src/main.py
