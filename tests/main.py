import sys

from analysis.cassification_analysis import classify_logs
from analysis.llama_analysis import llama_analysis
from analysis.utils import get_logs_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(sys.argv)
        print("Usage: python3 analyze_logs.py <log_file_path>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = get_logs_text(log_file_path)

    classification = classify_logs(logs)
    llama_text = llama_analysis(logs, classification)
    print(llama_text)
