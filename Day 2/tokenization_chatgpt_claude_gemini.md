# How Tokenization Works in ChatGPT, Claude, and Gemini

*A simple, beginner-friendly guide*

## 1. What is a token?

AI models do not read text exactly the way humans do. Before a model
processes text, a tokenizer breaks it into smaller pieces called
**tokens**. Each token is represented internally by a number.

A token might be: - a whole short word, such as `cat` - part of a longer
word, such as `token` + `ization` - punctuation or a space attached to
text - a piece of code - for multimodal models, a representation of
image, audio, or video content

**Important:** A token is not the same thing as a word, letter, or
character. The exact split depends on the model and its tokenizer.

### A simple mental picture

Text → tokenizer splits it into pieces → each piece gets a token ID →
the model processes those IDs → the model generates token IDs → the
tokenizer turns them back into readable text.

For example, the phrase `Tokenization is useful!` might be split into
pieces resembling:

`["Token", "ization", " is", " useful", "!"]`

This is only an illustration. It is **not** the guaranteed token split
used by ChatGPT, Claude, or Gemini.

## 2. Why do AI systems use tokens?

Tokenization helps models: 1. **Handle language efficiently.** Common
chunks can be represented as single tokens rather than many individual
characters. 2. **Handle unfamiliar words.** A rare word can be split
into smaller pieces instead of needing a token for every possible word.
3. **Process many kinds of text.** Numbers, punctuation, code, and
multiple languages can all be represented as token sequences. 4.
**Measure input and output.** Token counts are used for context limits
and, in API products, often for usage and pricing.

## 3. How tokenization generally works

Different tokenizers have different details, but a common approach is
based on **subword tokenization**.

A simplified explanation: 1. The tokenizer starts with text represented
as bytes or smaller units. 2. It uses a learned vocabulary of text
pieces. 3. Frequent or useful sequences can be represented by larger
pieces; unusual sequences may remain split into smaller pieces. 4. Each
resulting piece maps to a token ID.

One well-known method is **Byte Pair Encoding (BPE)**. In simple terms,
BPE learns which adjacent pieces often occur together and can merge them
into larger pieces. Some tokenizers use related or different techniques,
so it is not correct to assume that every AI platform uses the exact
same algorithm.

Token IDs are labels, not definitions. Two token IDs next to each other
numerically are not necessarily similar in meaning.

## 4. ChatGPT / OpenAI

### General approach

OpenAI models use model-specific tokenizers. OpenAI provides the
open-source **`tiktoken`** library for counting and inspecting tokens
for supported models. Its tokenization approach is based on BPE.

Different OpenAI models can use different encodings. For example,
`tiktoken` documents encodings such as `cl100k_base` and `o200k_base`.
Do not assume one encoding works for every model.

### What affects the token count?

-   The exact model and encoding
-   Spaces, punctuation, and formatting
-   Whether the text contains code, numbers, or uncommon words
-   The language being used
-   Extra request structure, tools, images, or other input types

A rough English-language estimate is **about 1 token per 4 characters**,
or around **¾ of a word**, but this is only a rule of thumb---not a
reliable count.

### How to count tokens

-   Try OpenAI's online tokenizer: https://platform.openai.com/tokenizer
-   For supported models, use `tiktoken`:
    https://github.com/openai/tiktoken
-   For API requests with tools, images, or structured content, use the
    relevant API counting/usage information rather than counting only
    the visible text.

## 5. Claude / Anthropic

### General approach

Claude also converts text into model tokens, but **Claude's tokenizer is
not the same as OpenAI's tokenizer**. Token boundaries and counts can
differ even when the text is identical.

Anthropic's documentation notes that tokenizer behavior can vary by
model generation. As a result, broad rules such as "one token equals
four characters" should be treated only as rough estimates. Some newer
Claude models may produce noticeably different counts from earlier
models.

### How to count tokens

For accurate API estimates, Anthropic provides a **token-counting
endpoint**. Use the same model you plan to call, because the count is
model-specific.

-   Claude documentation:
    https://platform.claude.com/docs/en/about-claude/glossary
-   Token counting guidance:
    https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/token-counting.md

**Practical tip:** Do not use OpenAI's `tiktoken` to obtain an exact
Claude token count. Use Anthropic's own counting method instead.

## 6. Gemini / Google

### General approach

Gemini converts input and output into tokens too. Google provides a
**`count_tokens`** capability in the Gemini API, which can count the
input for a particular model and request.

Gemini token counts can include more than ordinary text. Images, audio,
video, and documents may also contribute to token usage, and the way
they are counted depends on the model and input type.

Google's documentation gives a rough guide of about **4 characters per
token** for text and around **60--80 English words per 100 tokens**.
These are estimates, not universal rules.

### How to count tokens

-   Gemini token documentation:
    https://ai.google.dev/gemini-api/docs/tokens
-   Use the Gemini API's `count_tokens` method for a more accurate
    estimate for the input you intend to send.

## 7. Quick comparison

  -----------------------------------------------------------------------
  Platform                Tokenization in simple  Best way to count
                          terms                   accurately
  ----------------------- ----------------------- -----------------------
  ChatGPT / OpenAI        Model-specific          OpenAI tokenizer or
                          tokenizer; OpenAI       `tiktoken` for
                          provides `tiktoken` for supported models; use
                          supported models, using API usage/counting
                          BPE-based encodings     tools for full requests

  Claude / Anthropic      Uses Anthropic's own    Anthropic's
                          model-specific          token-counting endpoint
                          tokenizer; it can split with the target model
                          the same text           
                          differently from OpenAI 

  Gemini / Google         Uses Google's           Gemini API
                          model-specific          `count_tokens` with the
                          tokenizer; non-text     target model and input
                          inputs such as images,  
                          audio, and video can    
                          contribute tokens       
  -----------------------------------------------------------------------

**Main takeaway:** The same paragraph can have different token counts on
ChatGPT, Claude, and Gemini. A count from one platform should not be
treated as the exact count for another.

## 8. Why do the counts differ?

Imagine three translators who divide a sentence into chunks before
working on it. One might keep a common word together, another might
split it into two pieces, and another might divide punctuation
differently. The sentence is the same, but the number of pieces differs.

Tokenizers behave similarly. They have different vocabularies, training
choices, and model-specific rules. This is why token counts may differ
across providers---and sometimes across models from the same provider.

Counts can also differ more for: - languages that are less represented
in a tokenizer's vocabulary - emoji and unusual symbols - long or
uncommon names - programming code and unusual formatting - images,
audio, video, and other multimodal inputs

## 9. Tokens, context windows, and cost

These are related but different concepts:

-   **Input tokens:** Tokens in what you send the model, including
    relevant instructions and conversation history.
-   **Output tokens:** Tokens generated by the model.
-   **Context window:** The amount of input and generated content a
    model can handle in a single context. The limit varies by model.
-   **Price / usage:** API charges may depend on input and output token
    counts, and some services distinguish categories such as cached or
    reasoning tokens.

A short visible answer does not always mean the model used only a small
number of tokens. Some models may use additional internal reasoning
tokens, and a request can include instructions or structured data that
are not obvious in the final answer.

## 10. Common mistakes to avoid

-   **Mistake:** "One word always equals one token."\
    **Correction:** A word can be one token or several tokens.

-   **Mistake:** "Every platform counts tokens the same way."\
    **Correction:** Each model's tokenizer may split the same text
    differently.

-   **Mistake:** "A token count from a third-party website is exact for
    every model."\
    **Correction:** Exact counts require a tokenizer or counting API
    appropriate to the target model.

-   **Mistake:** "Only the prompt text counts."\
    **Correction:** Conversation structure, tool definitions, files, and
    multimodal inputs may also contribute.

-   **Mistake:** "A token is a unit of meaning."\
    **Correction:** A token is a text or input piece with an ID; meaning
    is learned by the model from patterns and context.

## 11. A practical workflow

If you are preparing a prompt for a specific platform:

1.  Choose the exact model you intend to use.
2.  Draft your prompt, including any system instructions or conversation
    history that will actually be sent.
3.  Use that provider's official tokenizer or token-counting API.
4.  Include relevant tools, files, images, or other inputs in the
    estimate when supported.
5.  Leave room for the model's response within the context limit.
6.  If cost matters, check the current pricing page for that exact model
    and token category.

## 12. Official references

-   **OpenAI tokenizer:** https://platform.openai.com/tokenizer
-   **OpenAI token counting help:**
    https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens
-   **OpenAI `tiktoken` project:** https://github.com/openai/tiktoken
-   **Anthropic / Claude glossary:**
    https://platform.claude.com/docs/en/about-claude/glossary
-   **Anthropic token-counting guidance:**
    https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/token-counting.md
-   **Google Gemini token documentation:**
    https://ai.google.dev/gemini-api/docs/tokens

*Documentation and model behavior can change. For exact token counts,
always use the official tool for the specific model and request.*
