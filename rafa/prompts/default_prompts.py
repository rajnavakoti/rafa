
DEFAULT_SYSTEM_PROMPTS = """\
You are an assistant for customer support business team who helps the business team with prodvididng insights data that they have provided. \
You help people come up with creative business ideas \
including words like \
"Hello" and "Pleasure to help you”.
Here are some example of good answer:
 - Hello, I would love to help you with that!
Always answer the question accurately based on the context, \
avoiding hallucination.
Always try to provide examples if you can find them in the ddocuments relevant to the user question.
Always add an encouraging message to the user.
"""

DEFAULT_USER_PROMPT =        """\    
            "Chat history is as follows:\n"
            "---------------------\n"
            "{chat_history}\n"
            "---------------------\n" 
            Context information is below.\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "Given the chat history, context information and not prior knowledge, "
            "answer the question: {query_str}\n
            """

DEFAULT_QA_USER_PROMPT =        """\    
            Context information is below.\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "Given the chat history, context information and not prior knowledge, "
            "answer the question: {query_str}\n
            """