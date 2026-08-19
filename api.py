import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Import your orchestrator functions
from src.context_builder import LaunchContext
from src.generators.messaging_framework import generate_messaging_framework
from src.generators.sales_battlecard import generate_sales_battlecard
from src.generators.product_webpage import generate_product_webpage

load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow frontend to call this API

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

# Main generation endpoint
@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate required fields
        if not data or 'product' not in data or 'strategy' not in data or 'plan' not in data:
            return jsonify({'error': 'Missing required fields: product, strategy, plan'}), 400
        
        # Extract inputs
        product = data.get('product', '').strip()
        strategy = data.get('strategy', '').strip()
        plan = data.get('plan', '').strip()
        
        # Validate inputs aren't empty
        if not product or not strategy or not plan:
            return jsonify({'error': 'All fields must be non-empty'}), 400
        
        # Build context
        context = LaunchContext(
            product_brief=product,
            launch_strategy=strategy,
            launch_plan=plan
        )
        
        # Generate assets
        print("Generating messaging framework...")
        messaging_framework = generate_messaging_framework(context)
        
        print("Generating sales battlecard...")
        sales_battlecard = generate_sales_battlecard(context)
        
        print("Generating product webpage...")
        product_webpage = generate_product_webpage(context)
        
        # Return results as JSON
        return jsonify({
            'success': True,
            'messaging_framework': messaging_framework,
            'sales_battlecard': sales_battlecard,
            'product_webpage': product_webpage
        }), 200
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': f'Generation failed: {str(e)}'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)