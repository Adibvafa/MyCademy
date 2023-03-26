"""
Summarize.py
-------------
Summarizes the created course
"""

import openai
import os

secret_api_key = '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'
openai.api_key = secret_api_key


def Create_Summary(paragraphs):
    short_paragraphs = []

    for paragraph in paragraphs:
        prompt = "Summarize and shorten as much as possible " + paragraph
        short_paragraph = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=70,
            top_p=1)
        short_paragraphs.append(
            short_paragraph["choices"][0]["message"]["content"].strip())

    summary = '\n'.join(short_paragraphs)
    return summary
