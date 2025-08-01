import json

# Path to the notebook
notebook_path = "chapter 5_Control Flow/5_5_if_statement_extended.ipynb"

# Read the existing notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Create the comprehensive explanation cell
explanation_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "# Control Flow in Python - Understanding Decision Making\n\n",
        "## What is Control Flow?\n\n",
        "**Control Flow** is the order in which statements are executed in a program. It determines how your program makes decisions and which code blocks run under different conditions. Think of it as the \"brain\" of your program that decides what to do next based on the current situation.\n\n",
        "### Key Concepts:\n\n",
        "#### 1. **Sequential Flow**\n",
        "- Code executes from top to bottom, line by line\n",
        "- Each statement runs once, in order\n",
        "- The default behavior of any program\n\n",
        "#### 2. **Conditional Flow**\n",
        "- Programs make decisions based on conditions\n",
        "- Different code blocks execute based on whether conditions are True or False\n",
        "- Uses comparison and logical operators we learned earlier\n\n",
        "#### 3. **Types of Control Flow Structures**\n",
        "- **if statements**: Execute code only if a condition is True\n",
        "- **if-else statements**: Execute different code based on True/False conditions\n",
        "- **if-elif-else statements**: Handle multiple conditions with different outcomes\n",
        "- **Loops**: Repeat code blocks multiple times (while, for)\n",
        "- **Functions**: Organize and reuse code blocks\n\n",
        "### Why Control Flow Matters:\n",
        "- **Makes programs intelligent**: Programs can respond differently to different inputs\n",
        "- **Handles real-world scenarios**: Real applications need to make decisions\n",
        "- **Creates interactive experiences**: Users get different responses based on their actions\n",
        "- **Prevents errors**: Programs can check conditions before executing risky operations\n\n",
        "---\n\n",
        "## Notebook Summary: If Statements Extended\n\n",
        "This notebook covers **Python's if statements** and conditional logic, building on the comparison and logical operators you learned earlier.\n\n",
        "### What You'll Learn:\n\n",
        "#### 1. **Basic If Statements**\n",
        "- Simple conditional execution with `if`\n",
        "- Using boolean values directly (`if True:`)\n",
        "- Using comparison expressions (`if 3 > 2:`)\n",
        "- Code blocks and indentation\n\n",
        "#### 2. **If-Else Statements**\n",
        "- Providing alternative execution paths\n",
        "- Handling both True and False conditions\n",
        "- Using variables to control flow\n\n",
        "#### 3. **If-Elif-Else Statements**\n",
        "- Multiple condition checking with `elif`\n",
        "- Handling more than two possible outcomes\n",
        "- String comparison and matching\n",
        "- The importance of order in condition checking\n\n",
        "#### 4. **Key Concepts Covered**\n",
        "- **Indentation**: Python uses indentation to define code blocks\n",
        "- **Condition evaluation**: How Python evaluates True/False conditions\n",
        "- **String matching**: Comparing strings for equality\n",
        "- **Variable-based conditions**: Using variables to control program flow\n",
        "- **Multiple outcomes**: Handling complex decision trees\n\n",
        "#### 5. **Practical Applications**\n",
        "- User input validation\n",
        "- Menu systems and navigation\n",
        "- Data filtering and categorization\n",
        "- Error handling and edge cases\n",
        "- Game logic and scoring systems\n\n",
        "### Real-World Examples:\n",
        "- **Banking systems**: Different actions for different account types\n",
        "- **E-commerce**: Different shipping options based on location\n",
        "- **Games**: Different responses based on player actions\n",
        "- **Data processing**: Different handling for different data types\n\n",
        "---\n\n",
        "**Remember**: Control flow is what makes your programs \"smart\" and responsive to different situations!\n"
    ]
}

# Insert the explanation cell at the beginning
notebook['cells'].insert(0, explanation_cell)

# Write the modified notebook back to file
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"Successfully added comprehensive Control Flow explanation to {notebook_path}")
print("The explanation covers what Control Flow is, why it matters, and summarizes your if statement notebook!") 