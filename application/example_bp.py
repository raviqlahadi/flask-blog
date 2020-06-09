from flask import Blueprint

example_bp = Blueprint(__name__, 'example_bp')

@example_bp.route('/')
def example():
    return 'this is from blueprint'