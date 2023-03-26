"""
Chat.py
-----------------
Answers users question in the chat
"""

import openai
import os

secret_api_key = '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'
openai.api_key = secret_api_key


def Answer_Question(user_question):
    """
    Answer to questions in the chatbox
    :param user_question: Question of user in the chat
    """
    prompt = f"""User has asked {user_question}. Provide accurate clear answer."""

    answer_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.15,
        max_tokens=250,
        top_p=0.9,
    )
    answer = answer_response["choices"][0]["message"]["content"]
    return answer.strip()
