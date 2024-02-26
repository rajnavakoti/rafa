import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.ollama.services.ollama_chat_completion import OllamaChatCompletion
from semantic_kernel.connectors.ai.ollama.ollama_prompt_execution_settings import OllamaPromptExecutionSettings

kernel = sk.Kernel()
settings = OllamaPromptExecutionSettings
kernel.add_chat_service(
    "llama2",
    OllamaChatCompletion(ai_model_id="llama2:13b")
)

settings.ai_model_id = "llama2:13b"

prompt = """{{$input}}
Summarize the content above.
"""

summarize = kernel.create_semantic_function(prompt_template=prompt, max_tokens=2000, temperature=0.2, top_p=0.5,
                                            ai_model_id="llama2:13b")

input_text = """
Demo (ancient Greek poet)
From Wikipedia, the free encyclopedia
Demo or Damo (Greek: Δεμώ, Δαμώ; fl. c. AD 200) was a Greek woman of the Roman period, known for a single epigram, engraved upon the Colossus of Memnon, which bears her name. She speaks of herself therein as a lyric poetess dedicated to the Muses, but nothing is known of her life.[1]
Identity
"""

# Run your prompt
# Note: functions are run asynchronously
async def main():
    try:
        print(await summarize(input_text))  # => Robots must not harm humans.
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
