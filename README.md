# LangChain Prompts: Study Notes

This repository contains study notes and concepts regarding prompts and prompt engineering within the LangChain ecosystem.

## 1. What is a Prompt?
Prompts are the inputs, instructions, or queries provided to a model to guide its outputs. While prompts can be multimodal (image, sound, video), these notes focus specifically on **text-based prompts**.

There are two main categories of prompts:
* **Static Prompts:** Hardcoded plain text or strings typed by the user. They cannot be changed at runtime.
* **Dynamic Prompts:** Prompts that use placeholders or variables, allowing different inputs to be filled in later. 

## 2. Prompt Templates
For dynamic prompts, LangChain uses **Prompt Templates**. These provide a structured way to create prompts by inserting variables into predefined templates instead of hardcoding them.

### Advantages of Prompt Templates:
1. **Validation:** You can enable default validation using the `validate_template=True` flag when defining the prompt to catch missing variables early.
2. **Reusability & Storage:** They make prompts reusable, flexible, and easy to manage. You can easily save a prompt template as a JSON file and load it back when required.
3. **Ecosystem Integration:** They are highly optimized and perfectly suited for automated workflows within the LangChain ecosystem.

## 3. Model Invocation: Single-Turn vs. Multi-Turn

When a model is invoked, the interaction generally falls into one of two categories, depending on how messages are passed.

![Model Invocation Tree](image_07bc6f.jpg)

### A. Single Message (Single-Turn / Standalone Queries)
Used for one-off questions where previous context is not needed.
* **Static Message:** Handled using plain text strings.
* **Dynamic Message:** Handled using a standard `PromptTemplate` to fill in variables.

### B. List of Messages (Multi-Turn Conversations)
Used for chatbots and applications where the LLM must remember the context of the conversation. Instead of manually keeping track of an array of history (e.g., "User: ... AI: ..."), LangChain handles this automatically using structured Messages.

**LangChain Message Types:**
* `SystemMessage`: Instructions for the AI's behavior or persona.
* `HumanMessage`: The user's input or question.
* `AIMessage`: The model's previous responses.

For Multi-Turn conversations:
* **Static Messages:** We pass a static list of the message types above.
* **Dynamic Messages:** We use a **`ChatPromptTemplate`** to feed in placeholders dynamically. 

### MessagePlaceholder
If we need to feed an entire list of past messages (chat history) into a template at runtime, we use a **`MessagePlaceholder`**. This is a special placeholder in LangChain used inside `ChatPromptTemplates` to dynamically insert an array of messages, ensuring the model retains conversational context seamlessly.