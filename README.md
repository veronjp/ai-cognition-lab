# ai-cognition-lab

## Purpose

This repository documents my progression as a psychology researcher-builder exploring the intersection of artificial intelligence and human cognition.

My initial focus is on learning, decision-making, and metacognition.

## Current Project: Metacognitive Accuracy

### Research Question
Does using AI change how accurately people estimate their own performance?

### Objective
Explore how estimated performance compares with actual performance, and how this accuracy may change before and after AI use.

### Current Progress
- Created a basic Python program to calculate estimation errors.
- Tested three outcomes: Improved, Deteriorated, and No change.
- Established a Git and GitHub workflow for tracking development.

### Research Status
Early prototype. No human-participant data has been collected, and the program does not yet test whether AI causes changes in metacognitive accuracy.

## How to Run

### Requirements
- Python 3 installed
- A terminal or VS Code

### Instructions
1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

   ```bash
   py metacognition_check.py```
   5. The program displays one of three outcomes:
   - Improved
   - Deteriorated
   - No change

For macOS or Linux, use `python3 metacognition_check.py` instead.

## Project Structure

- `README.md` — Project documentation
- `metacognition_check.py` — Python program calculating changes in estimation accuracy

## Limitations

- Uses manually entered example values.
- Evaluates one set of scores at a time.
- Does not collect human-participant data.
- Does not establish whether AI causes changes in metacognitive accuracy.
- Measures absolute estimation error, not subjective confidence.