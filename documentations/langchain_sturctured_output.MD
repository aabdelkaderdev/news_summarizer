[Skip to main content](https://docs.langchain.com/oss/python/langchain/structured-output#content-area)

[Docs by LangChain home page![light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)](https://docs.langchain.com/)

![https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png](https://mintlify.s3.us-west-1.amazonaws.com/langchain-5e9cc07a/images/brand/langchain-icon.png)Open source

Search...

Ctrl K

Search...

Navigation

Core components

Structured output

[Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) [LangChain](https://docs.langchain.com/oss/python/langchain/overview) [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) [Integrations](https://docs.langchain.com/oss/python/integrations/providers/overview) [Learn](https://docs.langchain.com/oss/python/learn) [Reference](https://docs.langchain.com/oss/python/reference/overview) [Contribute](https://docs.langchain.com/oss/python/contributing/overview)

Python

- [Overview](https://docs.langchain.com/oss/python/langchain/overview)

##### Get started

- [Install](https://docs.langchain.com/oss/python/langchain/install)
- [Quickstart](https://docs.langchain.com/oss/python/langchain/quickstart)
- [Changelog](https://docs.langchain.com/oss/python/releases/changelog)
- [Philosophy](https://docs.langchain.com/oss/python/langchain/philosophy)

##### Core components

- [Agents](https://docs.langchain.com/oss/python/langchain/agents)
- [Models](https://docs.langchain.com/oss/python/langchain/models)
- [Messages](https://docs.langchain.com/oss/python/langchain/messages)
- [Tools](https://docs.langchain.com/oss/python/langchain/tools)
- [Short-term memory](https://docs.langchain.com/oss/python/langchain/short-term-memory)
- Streaming

- [Structured output](https://docs.langchain.com/oss/python/langchain/structured-output)

##### Middleware

- [Overview](https://docs.langchain.com/oss/python/langchain/middleware/overview)
- [Prebuilt middleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in)
- [Custom middleware](https://docs.langchain.com/oss/python/langchain/middleware/custom)

##### Advanced usage

- [Guardrails](https://docs.langchain.com/oss/python/langchain/guardrails)
- [Runtime](https://docs.langchain.com/oss/python/langchain/runtime)
- [Context engineering](https://docs.langchain.com/oss/python/langchain/context-engineering)
- [Model Context Protocol (MCP)](https://docs.langchain.com/oss/python/langchain/mcp)
- [Human-in-the-loop](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)
- Multi-agent

- [Retrieval](https://docs.langchain.com/oss/python/langchain/retrieval)
- [Long-term memory](https://docs.langchain.com/oss/python/langchain/long-term-memory)

##### Agent development

- [LangSmith Studio](https://docs.langchain.com/oss/python/langchain/studio)
- [Test](https://docs.langchain.com/oss/python/langchain/test)
- [Agent Chat UI](https://docs.langchain.com/oss/python/langchain/ui)

##### Deploy with LangSmith

- [Deployment](https://docs.langchain.com/oss/python/langchain/deploy)
- [Observability](https://docs.langchain.com/oss/python/langchain/observability)

On this page

- [Response format](https://docs.langchain.com/oss/python/langchain/structured-output#response-format)
- [Provider strategy](https://docs.langchain.com/oss/python/langchain/structured-output#provider-strategy)
- [Tool calling strategy](https://docs.langchain.com/oss/python/langchain/structured-output#tool-calling-strategy)
- [Custom tool message content](https://docs.langchain.com/oss/python/langchain/structured-output#custom-tool-message-content)
- [Error handling](https://docs.langchain.com/oss/python/langchain/structured-output#error-handling)
- [Multiple structured outputs error](https://docs.langchain.com/oss/python/langchain/structured-output#multiple-structured-outputs-error)
- [Schema validation error](https://docs.langchain.com/oss/python/langchain/structured-output#schema-validation-error)
- [Error handling strategies](https://docs.langchain.com/oss/python/langchain/structured-output#error-handling-strategies)

Structured output allows agents to return data in a specific, predictable format. Instead of parsing natural language responses, you get structured data in the form of JSON objects, [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/#basic-model-usage), or dataclasses that your application can use directly.

This page covers structured output with agents using `create_agent`. To use structured output directly on a model (outside of agents), see [Models - Structured output](https://docs.langchain.com/oss/python/langchain/models#structured-output).

LangChain’s [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) handles structured output automatically. The user sets their desired structured output schema, and when the model generates the structured data, it’s captured, validated, and returned in the `'structured_response'` key of the agent’s state.

Copy

```
def create_agent(
    ...
    response_format: Union[\
        ToolStrategy[StructuredResponseT],\
        ProviderStrategy[StructuredResponseT],\
        type[StructuredResponseT],\
        None,\
    ]
```

## [​](https://docs.langchain.com/oss/python/langchain/structured-output\#response-format)  Response format

Use `response_format` to control how the agent returns structured data:

- **`ToolStrategy[StructuredResponseT]`**: Uses tool calling for structured output
- **`ProviderStrategy[StructuredResponseT]`**: Uses provider-native structured output
- **`type[StructuredResponseT]`**: Schema type - automatically selects best strategy based on model capabilities
- **`None`**: Structured output not explicitly requested

When a schema type is provided directly, LangChain automatically chooses:

- `ProviderStrategy` if the model and provider chosen supports native structured output (e.g. [OpenAI](https://docs.langchain.com/oss/python/integrations/providers/openai), [Anthropic (Claude)](https://docs.langchain.com/oss/python/integrations/providers/anthropic), or [xAI (Grok)](https://docs.langchain.com/oss/python/integrations/providers/xai)).
- `ToolStrategy` for all other models.

Support for native structured output features is read dynamically from the model’s [profile data](https://docs.langchain.com/oss/python/langchain/models#model-profiles) if using `langchain>=1.1`. If data are not available, use another condition or specify manually:

Copy

```
custom_profile = {
    "structured_output": True,
    # ...
}
model = init_chat_model("...", profile=custom_profile)
```

If tools are specified, the model must support simultaneous use of tools and structured output.

The structured response is returned in the `structured_response` key of the agent’s final state.

## [​](https://docs.langchain.com/oss/python/langchain/structured-output\#provider-strategy)  Provider strategy

Some model providers support structured output natively through their APIs (e.g. OpenAI, xAI (Grok), Gemini, Anthropic (Claude)). This is the most reliable method when available.To use this strategy, configure a `ProviderStrategy`:

Copy

```
class ProviderStrategy(Generic[SchemaT]):
    schema: type[SchemaT]
    strict: bool | None = None
```

The `strict` param requires `langchain>=1.2`.

[​](https://docs.langchain.com/oss/python/langchain/structured-output#param-schema)

schema

required

The schema defining the structured output format. Supports:

- **Pydantic models**: `BaseModel` subclasses with field validation. Returns validated Pydantic instance.
- **Dataclasses**: Python dataclasses with type annotations. Returns dict.
- **TypedDict**: Typed dictionary classes. Returns dict.
- **JSON Schema**: Dictionary with JSON schema specification. Returns dict.

[​](https://docs.langchain.com/oss/python/langchain/structured-output#param-strict)

strict

Optional boolean parameter to enable strict schema adherence. Supported by some providers (e.g., [OpenAI](https://docs.langchain.com/oss/python/integrations/chat/openai) and [xAI](https://docs.langchain.com/oss/python/integrations/chat/xai)). Defaults to `None` (disabled).

LangChain automatically uses `ProviderStrategy` when you pass a schema type directly to [`create_agent.response_format`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) and the model supports native structured output:

Pydantic Model

Dataclass

TypedDict

JSON Schema

Copy

```
from pydantic import BaseModel, Field
from langchain.agents import create_agent

class ContactInfo(BaseModel):
    """Contact information for a person."""
    name: str = Field(description="The name of the person")
    email: str = Field(description="The email address of the person")
    phone: str = Field(description="The phone number of the person")

agent = create_agent(
    model="gpt-5",
    response_format=ContactInfo  # Auto-selects ProviderStrategy
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, (555) 123-4567"}]
})

print(result["structured_response"])
# ContactInfo(name='John Doe', email='john@example.com', phone='(555) 123-4567')
```

Provider-native structured output provides high reliability and strict validation because the model provider enforces the schema. Use it when available.

If the provider natively supports structured output for your model choice, it is functionally equivalent to write `response_format=ProductReview` instead of `response_format=ProviderStrategy(ProductReview)`.In either case, if structured output is not supported, the agent will fall back to a tool calling strategy.

## [​](https://docs.langchain.com/oss/python/langchain/structured-output\#tool-calling-strategy)  Tool calling strategy

For models that don’t support native structured output, LangChain uses tool calling to achieve the same result. This works with all models that support tool calling (most modern models).To use this strategy, configure a `ToolStrategy`:

Copy

```
class ToolStrategy(Generic[SchemaT]):
    schema: type[SchemaT]
    tool_message_content: str | None
    handle_errors: Union[\
        bool,\
        str,\
        type[Exception],\
        tuple[type[Exception], ...],\
        Callable[[Exception], str],\
    ]
```

[​](https://docs.langchain.com/oss/python/langchain/structured-output#param-schema-1)

schema

required

The schema defining the structured output format. Supports:

- **Pydantic models**: `BaseModel` subclasses with field validation. Returns validated Pydantic instance.
- **Dataclasses**: Python dataclasses with type annotations. Returns dict.
- **TypedDict**: Typed dictionary classes. Returns dict.
- **JSON Schema**: Dictionary with JSON schema specification. Returns dict.
- **Union types**: Multiple schema options. The model will choose the most appropriate schema based on the context.

[​](https://docs.langchain.com/oss/python/langchain/structured-output#param-tool-message-content)

tool\_message\_content

Custom content for the tool message returned when structured output is generated.
If not provided, defaults to a message showing the structured response data.

[​](https://docs.langchain.com/oss/python/langchain/structured-output#param-handle-errors)

handle\_errors

Error handling strategy for structured output validation failures. Defaults to `True`.

- **`True`**: Catch all errors with default error template
- **`str`**: Catch all errors with this custom message
- **`type[Exception]`**: Only catch this exception type with default message
- **`tuple[type[Exception], ...]`**: Only catch these exception types with default message
- **`Callable[[Exception], str]`**: Custom function that returns error message
- **`False`**: No retry, let exceptions propagate

Pydantic Model

Dataclass

TypedDict

JSON Schema

Union Types

Copy

```
from pydantic import BaseModel, Field
from typing import Literal
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class ProductReview(BaseModel):
    """Analysis of a product review."""
    rating: int | None = Field(description="The rating of the product", ge=1, le=5)
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the review")
    key_points: list[str] = Field(description="The key points of the review. Lowercase, 1-3 words each.")

agent = create_agent(
    model="gpt-5",
    tools=tools,
    response_format=ToolStrategy(ProductReview)
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Analyze this review: 'Great product: 5 out of 5 stars. Fast shipping, but expensive'"}]
})
result["structured_response"]
# ProductReview(rating=5, sentiment='positive', key_points=['fast shipping', 'expensive'])
```

### [​](https://docs.langchain.com/oss/python/langchain/structured-output\#custom-tool-message-content)  Custom tool message content

The `tool_message_content` parameter allows you to customize the message that appears in the conversation history when structured output is generated:

Copy

```
from pydantic import BaseModel, Field
from typing import Literal
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class MeetingAction(BaseModel):
    """Action items extracted from a meeting transcript."""
    task: str = Field(description="The specific task to be completed")
    assignee: str = Field(description="Person responsible for the task")
    priority: Literal["low", "medium", "high"] = Field(description="Priority level")

agent = create_agent(
    model="gpt-5",
    tools=[],
    response_format=ToolStrategy(
        schema=MeetingAction,
        tool_message_content="Action item captured and added to meeting notes!"
    )
)

agent.invoke({
    "messages": [{"role": "user", "content": "From our meeting: Sarah needs to update the project timeline as soon as possible"}]
})
```

Copy

```
================================ Human Message =================================

From our meeting: Sarah needs to update the project timeline as soon as possible
================================== Ai Message ==================================
Tool Calls:
  MeetingAction (call_1)
 Call ID: call_1
  Args:
    task: Update the project timeline
    assignee: Sarah
    priority: high
================================= Tool Message =================================
Name: MeetingAction

Action item captured and added to meeting notes!
```

Without `tool_message_content`, our final [`ToolMessage`](https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage) would be:

Copy

```
================================= Tool Message =================================
Name: MeetingAction

Returning structured response: {'task': 'update the project timeline', 'assignee': 'Sarah', 'priority': 'high'}
```

### [​](https://docs.langchain.com/oss/python/langchain/structured-output\#error-handling)  Error handling

Models can make mistakes when generating structured output via tool calling. LangChain provides intelligent retry mechanisms to handle these errors automatically.

#### [​](https://docs.langchain.com/oss/python/langchain/structured-output\#multiple-structured-outputs-error)  Multiple structured outputs error

When a model incorrectly calls multiple structured output tools, the agent provides error feedback in a [`ToolMessage`](https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage) and prompts the model to retry:

Copy

```
from pydantic import BaseModel, Field
from typing import Union
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class ContactInfo(BaseModel):
    name: str = Field(description="Person's name")
    email: str = Field(description="Email address")

class EventDetails(BaseModel):
    event_name: str = Field(description="Name of the event")
    date: str = Field(description="Event date")

agent = create_agent(
    model="gpt-5",
    tools=[],
    response_format=ToolStrategy(Union[ContactInfo, EventDetails])  # Default: handle_errors=True
)

agent.invoke({
    "messages": [{"role": "user", "content": "Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th"}]
})
```

Copy

```
================================ Human Message =================================

Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th
None
================================== Ai Message ==================================
Tool Calls:
  ContactInfo (call_1)
 Call ID: call_1
  Args:
    name: John Doe
    email: john@email.com
  EventDetails (call_2)
 Call ID: call_2
  Args:
    event_name: Tech Conference
    date: March 15th
================================= Tool Message =================================
Name: ContactInfo

Error: Model incorrectly returned multiple structured responses (ContactInfo, EventDetails) when only one is expected.
 Please fix your mistakes.
================================= Tool Message =================================
Name: EventDetails

Error: Model incorrectly returned multiple structured responses (ContactInfo, EventDetails) when only one is expected.
 Please fix your mistakes.
================================== Ai Message ==================================
Tool Calls:
  ContactInfo (call_3)
 Call ID: call_3
  Args:
    name: John Doe
    email: john@email.com
================================= Tool Message =================================
Name: ContactInfo

Returning structured response: {'name': 'John Doe', 'email': 'john@email.com'}
```

#### [​](https://docs.langchain.com/oss/python/langchain/structured-output\#schema-validation-error)  Schema validation error

When structured output doesn’t match the expected schema, the agent provides specific error feedback:

Copy

```
from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class ProductRating(BaseModel):
    rating: int | None = Field(description="Rating from 1-5", ge=1, le=5)
    comment: str = Field(description="Review comment")

agent = create_agent(
    model="gpt-5",
    tools=[],
    response_format=ToolStrategy(ProductRating),  # Default: handle_errors=True
    system_prompt="You are a helpful assistant that parses product reviews. Do not make any field or value up."
)

agent.invoke({
    "messages": [{"role": "user", "content": "Parse this: Amazing product, 10/10!"}]
})
```

Copy

```
================================ Human Message =================================

Parse this: Amazing product, 10/10!
================================== Ai Message ==================================
Tool Calls:
  ProductRating (call_1)
 Call ID: call_1
  Args:
    rating: 10
    comment: Amazing product
================================= Tool Message =================================
Name: ProductRating

Error: Failed to parse structured output for tool 'ProductRating': 1 validation error for ProductRating.rating
  Input should be less than or equal to 5 [type=less_than_equal, input_value=10, input_type=int].
 Please fix your mistakes.
================================== Ai Message ==================================
Tool Calls:
  ProductRating (call_2)
 Call ID: call_2
  Args:
    rating: 5
    comment: Amazing product
================================= Tool Message =================================
Name: ProductRating

Returning structured response: {'rating': 5, 'comment': 'Amazing product'}
```

#### [​](https://docs.langchain.com/oss/python/langchain/structured-output\#error-handling-strategies)  Error handling strategies

You can customize how errors are handled using the `handle_errors` parameter:**Custom error message:**

Copy

```
ToolStrategy(
    schema=ProductRating,
    handle_errors="Please provide a valid rating between 1-5 and include a comment."
)
```

If `handle_errors` is a string, the agent will _always_ prompt the model to re-try with a fixed tool message:

Copy

```
================================= Tool Message =================================
Name: ProductRating

Please provide a valid rating between 1-5 and include a comment.
```

**Handle specific exceptions only:**

Copy

```
ToolStrategy(
    schema=ProductRating,
    handle_errors=ValueError  # Only retry on ValueError, raise others
)
```

If `handle_errors` is an exception type, the agent will only retry (using the default error message) if the exception raised is the specified type. In all other cases, the exception will be raised.**Handle multiple exception types:**

Copy

```
ToolStrategy(
    schema=ProductRating,
    handle_errors=(ValueError, TypeError)  # Retry on ValueError and TypeError
)
```

If `handle_errors` is a tuple of exceptions, the agent will only retry (using the default error message) if the exception raised is one of the specified types. In all other cases, the exception will be raised.**Custom error handler function:**

Copy

```

from langchain.agents.structured_output import StructuredOutputValidationError
from langchain.agents.structured_output import MultipleStructuredOutputsError

def custom_error_handler(error: Exception) -> str:
    if isinstance(error, StructuredOutputValidationError):
        return "There was an issue with the format. Try again."
    elif isinstance(error, MultipleStructuredOutputsError):
        return "Multiple structured outputs were returned. Pick the most relevant one."
    else:
        return f"Error: {str(error)}"

agent = create_agent(
    model="gpt-5",
    tools=[],
    response_format=ToolStrategy(
                        schema=Union[ContactInfo, EventDetails],
                        handle_errors=custom_error_handler
                    )  # Default: handle_errors=True
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th"}]
})

for msg in result['messages']:
    # If message is actually a ToolMessage object (not a dict), check its class name
    if type(msg).__name__ == "ToolMessage":
        print(msg.content)
    # If message is a dictionary or you want a fallback
    elif isinstance(msg, dict) and msg.get('tool_call_id'):
        print(msg['content'])
```

On `StructuredOutputValidationError`:

Copy

```
================================= Tool Message =================================
Name: ToolStrategy

There was an issue with the format. Try again.
```

On `MultipleStructuredOutputsError`:

Copy

```
================================= Tool Message =================================
Name: ToolStrategy

Multiple structured outputs were returned. Pick the most relevant one.
```

On other errors:

Copy

```
================================= Tool Message =================================
Name: ToolStrategy

Error: <error message>
```

**No error handling:**

Copy

```
response_format = ToolStrategy(
    schema=ProductRating,
    handle_errors=False  # All errors raised
)
```

* * *

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/structured-output.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

[Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

Was this page helpful?

YesNo

[Frontend\\
\\
Previous](https://docs.langchain.com/oss/python/langchain/streaming/frontend) [Overview\\
\\
Next](https://docs.langchain.com/oss/python/langchain/middleware/overview)

Ctrl+I
