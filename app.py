from flask import Flask, jsonify, request
from ctransformers import AutoModelForCausalLM
from langchain.prompts import PromptTemplate

# Initialize Flask app
app = Flask(__name__)

# Define function to get response from LLaMA model
def get_llama_response(input_text, timeComplexity, language):
    # Initialize the CTransformers model with the path to your local model
    llm = AutoModelForCausalLM(
        model='C:/Users/RAJKIRAN REDDY/Desktop/code-generator-app/codellama-13b.Q4_K_M.gguf',
        model_type='llama',
        config={'max_new_tokens': 500, 'temperature': 0.01}
    )
    
    # Define the prompt template
    template = (
        "Generate code for description:\n\n"
        "Description: '{input_text}'\n\n"
        "Time Complexity: {timeComplexity}\n\n"
        "in Programming Language: {language}\n\n"
    )

    # Use LangChain PromptTemplate to format prompt
    prompt = PromptTemplate(input_variables=["input_text", "timeComplexity", "language"], template=template)
    formatted_prompt = prompt.format(input_text=input_text, timeComplexity=timeComplexity, language=language)

    # Generate response from model
    response = llm(formatted_prompt)
    return response

# Define route to generate code
@app.route('/generate', methods=['POST'])
def generate_response():
    try:
        # Get JSON data from POST request
        data = request.json
        input_text = data.get('input_text')
        timeComplexity = data.get('timeComplexity')
        language = data.get('language')

        # Get the response from the LLaMA model
        response = get_llama_response(input_text, timeComplexity, language)

        # Return the response as JSON
        return jsonify({'response': response}), 200

    except Exception as e:
        print(f"Error generating response: {str(e)}")
        return jsonify({'error': 'Failed to generate response'}), 500

# Run the Flask app
if __name__ == '__main__':
    print("Starting Flask server on http://127.0.0.1:5000")
    app.run(debug=True)
