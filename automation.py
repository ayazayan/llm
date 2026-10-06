import llm

# Select the Gemini model to use
model = llm.get_model("gemini-flash-lite-latest")

# Full instruction for the below_zero task
full_prompt = """Write a Python function below_zero(ops). ops is a list of ints representing deposits and withdrawals on a bank account that starts with a balance of 0. Detect if at any point the balance goes below 0; if so return True, otherwise return False."""

# I made this a function so the automation is reusable. Instead of being tied
# to the below_zero task, I can pass in a different prompt and use the same code.
def run_full_prompt(prompt):
    response = model.prompt(prompt)
    print(response.text())

    # Count both the input and output tokens for the full-instruction run
    usage = response.usage()
    print(usage)
    total_tokens = usage.input + usage.output
    print("Total full-instruction tokens:", total_tokens)

# Step-by-step instructions for the second run
step_prompts = [
    "Write me a function below_zero to find out if an account ever goes below 0.",
    "The input's a list of ints representing transactions.",
    "The balance starts at 0.",
    "Return True if the balance ever goes below 0, otherwise False."
]

# I made the step-by-step run a function too, so I can reuse it with a
# different list of prompts while still keeping all prompts in one conversation.
def run_stepwise(prompts):
    conversation = model.conversation()
    total_tokens = 0

    # Send each instruction one after another (no manual action required between prompts)
    for prompt in prompts:
        step_response = conversation.prompt(prompt)
        print(step_response.text())
        print(step_response.usage())

        # Add the input and output tokens from this response to the running total
        usage = step_response.usage()
        total_tokens += usage.input + usage.output

    print("Total stepwise tokens:", total_tokens)

# Run both experiments to collect their responses and token usage
run_full_prompt(full_prompt)
run_stepwise(step_prompts)