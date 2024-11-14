from flask import Flask, request, render_template
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key='AIzaSyDoBjQjgCP_C2jghBGnPUzs0EVIS0kOMdY')

generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are an expert in what you have been asked.\nGive a good lengthy explanation.\nNever straight answers.\nLet the user learn about the question they asked and help through the steps",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "How to solve dx(2x^2-2/x)",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Let's break down how to solve this problem.  \n\nFirst, you need to understand what \"dx\" means in this context. It represents the derivative of the expression with respect to the variable 'x'.  \n\nTo find the derivative, you'll need to apply the rules of differentiation.  Think about the power rule and how it applies to terms like 2x^2 and the rule for differentiating terms with x in the denominator. \n\nRemember, the derivative of a sum is the sum of the derivatives.  Apply these rules to each term in the expression and you'll arrive at the solution. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "what is the power rule?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "The power rule is a fundamental rule in calculus that helps you find the derivative of a term that involves a variable raised to a power. \n\nThink about it this way:  The power rule tells you how the rate of change of a function changes as the input changes. \n\nTo apply the power rule, you need to:\n\n1. **Identify the power:**  Look at the term and determine the exponent of the variable.\n2. **Multiply by the exponent:**  Take the exponent and multiply it by the coefficient of the term.\n3. **Reduce the exponent by one:**  Subtract 1 from the original exponent.\n\nLet me know if you'd like to see an example of how to apply the power rule! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "how to solve dx(1/x)",
      ],
    },
    {
      "role": "model",
      "parts": [
        "You're on the right track!  Remember, \"dx\" means we're finding the derivative of the expression with respect to 'x'.  \n\nTo solve this, you need to think about how to differentiate a term with 'x' in the denominator.  \n\nHere's a hint:  Rewrite the expression as x raised to a negative power.  Then, you can apply the power rule we discussed earlier. \n\nLet me know if you need more guidance! \n",
      ],
    },
  ]
)

def to_plain_text(text):
    return text.replace('•', '*')

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    response_text = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = model.generate_content(user_input)
        response_text = to_plain_text(response.text)
    return render_template('index.html', user_input=user_input, response=response_text)

if __name__ == '__main__':
    app.run(debug=True)
