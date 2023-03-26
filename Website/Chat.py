"""
Chat.py
-----------------
Answers users question in the chat
"""

import openai
openai.api_key = "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"


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
