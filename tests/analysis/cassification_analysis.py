from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def classify_logs(logs: str) -> str:
    summary = summarizer(logs, max_length=512, min_length=50, do_sample=False)
    summarized_logs = summary[0]['summary_text']

    results = classifier(summarized_logs)[0]
    return results['label']
