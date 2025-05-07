# Assignment Report

##  Objective
To build a chatbot that can answer frequently asked questions about products, orders, payments, warranty, and returns using a language model. The chatbot should be capable of handling multi-turn conversations and preserve context effectively.

---

## Multi-turn Conversation and Context Handling

To enable multi-turn conversations:
- I stored each user-bot interaction in a text file (`conversation_history.txt`).
- Every time the user inputs a query, the chatbot reads the **last 10 exchanges** from this file and includes them in the prompt to provide context.
- This method ensures that the chatbot has visibility over recent conversation turns, allowing it to respond contextually.

## Implementation and Testing

### 1. **Model Used**
- I used the Hugging Face `pipeline` with `google/flan-t5-base` for the chatbot.
- The FAQ data included in the prompt is form the assignment given
  
### 2. **Prompt Construction**
Each prompt includes:
- A stringified version of the FAQs.
- The last 10 user-chatbot exchanges.
- The current user query.

This helps the model generate more accurate and coherent replies.

### 3. **Testing Strategy**
I manually tested the chatbot through command-line interaction:
- Tested sequential queries with follow-ups.
- Asked out-of-scope questions to check fallback behavior.
- Verified persistence by restarting the program and seeing previous chat retained.

---

## Dependicies

```
pip install flask transformers
```
