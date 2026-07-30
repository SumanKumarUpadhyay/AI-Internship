"""
Hugging Face Hub Exploration
------------------------------
Demonstrates 5 core NLP tasks using Hugging Face `transformers` pipelines:
  1. Sentiment Analysis
  2. Question Answering (QA)
  3. Text Generation
  4. Text Summarization
  5. Named Entity Recognition (NER) -- bonus, matches this week's learning objective

REQUIREMENTS (run this on your own machine with internet access):
    pip install transformers torch

NOTE: The first time each pipeline runs, it downloads the model files from
huggingface.co (a few hundred MB each), so the first run will take a
couple of minutes and needs an active internet connection.
"""

from transformers import pipeline


def run_sentiment_analysis():
    print("\n--- 1. Sentiment Analysis ---")
    classifier = pipeline("sentiment-analysis")
    result = classifier("Movie was amazing")
    print(f"Input : Movie was amazing")
    print(f"Output: {result}")


def run_question_answering():
    print("--- 2. Question Answering ---")
    qa = pipeline("question-answering")
    context = (
        "Hugging Face is a company that provides open-source tools for "
        "Natural Language Processing, including the Transformers library."
    )
    question = "What does Hugging Face provide?"
    result = qa(question=question, context=context)
    print(f"Context : {context}")
    print(f"Question: {question}")
    print(f"Answer  : {result['answer']} (score: {result['score']:.4f})")


def run_text_generation():
    print("--- 3. Text Generation ---")
    generator = pipeline("text-generation", model="gpt2")
    prompt = "Artificial Intelligence will"
    result = generator(prompt, max_length=30, num_return_sequences=1)
    print(f"Prompt: {prompt}")
    print(f"Output: {result[0]['generated_text']}")


def run_text_summarization():
    print("--- 4. Text Summarization ---")
    summarizer = pipeline("summarization")
    article = (
        "Artificial intelligence (AI) is intelligence demonstrated by machines, "
        "as opposed to natural intelligence displayed by animals including humans. "
        "AI research has been defined as the field of study of intelligent agents, "
        "which refers to any system that perceives its environment and takes actions "
        "that maximize its chance of achieving its goals. Machine learning and deep "
        "learning are the primary techniques used to build modern AI systems, and "
        "they have enabled major advances in computer vision, natural language "
        "processing, and robotics over the past decade."
    )
    result = summarizer(article, max_length=45, min_length=15, do_sample=False)
    print(f"Original length : {len(article.split())} words")
    print(f"Summary         : {result[0]['summary_text']}")


def run_named_entity_recognition():
    print("--- 5. Named Entity Recognition (NER) ---")
    ner = pipeline("ner", grouped_entities=True)
    sentence = "Suman is interning at an AI company based in India and building projects with Hugging Face."
    result = ner(sentence)
    print(f"Sentence: {sentence}")
    print("Entities found:")
    for entity in result:
        print(f"  - {entity['word']} -> {entity['entity_group']} (score: {entity['score']:.2f})")


if __name__ == "__main__":
    run_sentiment_analysis()
    run_question_answering()
    run_text_generation()
    run_text_summarization()
    run_named_entity_recognition()
