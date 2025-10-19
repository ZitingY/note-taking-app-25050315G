from flask import Blueprint, jsonify, request
from src.llm import extract_notes

generate_bp = Blueprint('generate', __name__)

@generate_bp.route('/generate', methods=['POST'])
def generate_note():
    try:
        data = request.json
        text = data.get('text')
        lang = data.get('language', 'English')
        
        if not text:
            return jsonify({'error': 'Missing text'}), 400
            
        generated_note = extract_notes(text, lang)
        return jsonify({'generated_note': generated_note})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
