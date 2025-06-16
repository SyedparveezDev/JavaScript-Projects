#!/usr/bin/env python3
"""
Simple HTTP server for development when Django is not available.
This serves static files and provides basic functionality.
"""

import http.server
import socketserver
import os
import json
from urllib.parse import urlparse, parse_qs

class IPOHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler for IPO app development server."""
    
    def do_GET(self):
        """Handle GET requests."""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Serve static files
        if path.startswith('/static/'):
            self.serve_static_file(path)
        elif path == '/' or path == '/home':
            self.serve_home_page()
        elif path == '/api/':
            self.serve_api_overview()
        elif path.startswith('/api/ipo'):
            self.serve_api_response()
        else:
            self.serve_placeholder_page(path)
    
    def serve_static_file(self, path):
        """Serve static files."""
        try:
            file_path = path[1:]  # Remove leading slash
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    content = f.read()
                
                # Set content type based on file extension
                if path.endswith('.css'):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/css')
                    self.end_headers()
                    self.wfile.write(content)
                else:
                    super().do_GET()
            else:
                self.send_error(404)
        except Exception:
            self.send_error(500)
    
    def serve_home_page(self):
        """Serve the home page."""
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>IPO Web App - Development Server</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
        </head>
        <body>
            <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
                <div class="container">
                    <a class="navbar-brand fw-bold" href="/">
                        <i class="bi bi-graph-up-arrow"></i> Bluestock IPO
                    </a>
                </div>
            </nav>
            
            <div class="container py-5">
                <div class="row justify-content-center">
                    <div class="col-md-8 text-center">
                        <h1 class="display-4 mb-4">
                            <i class="bi bi-tools"></i> Development Server
                        </h1>
                        <div class="alert alert-info">
                            <h4><i class="bi bi-info-circle"></i> Django Project Created Successfully!</h4>
                            <p class="mb-0">The IPO web application structure has been set up. To run the full Django application:</p>
                        </div>
                        
                        <div class="card mt-4">
                            <div class="card-header bg-primary text-white">
                                <h5><i class="bi bi-terminal"></i> Setup Instructions</h5>
                            </div>
                            <div class="card-body text-start">
                                <ol>
                                    <li><strong>Install Dependencies:</strong><br>
                                        <code>pip install -r requirements.txt</code>
                                    </li>
                                    <li><strong>Run Migrations:</strong><br>
                                        <code>python manage.py migrate</code>
                                    </li>
                                    <li><strong>Create Superuser:</strong><br>
                                        <code>python manage.py createsuperuser</code>
                                    </li>
                                    <li><strong>Start Django Server:</strong><br>
                                        <code>python manage.py runserver</code>
                                    </li>
                                </ol>
                            </div>
                        </div>
                        
                        <div class="row mt-4">
                            <div class="col-md-6">
                                <div class="card h-100">
                                    <div class="card-body">
                                        <h5><i class="bi bi-file-code"></i> Project Structure</h5>
                                        <ul class="list-unstyled text-start">
                                            <li>✅ Django project created</li>
                                            <li>✅ IPO app with models</li>
                                            <li>✅ REST API endpoints</li>
                                            <li>✅ Admin interface</li>
                                            <li>✅ Bootstrap templates</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="card h-100">
                                    <div class="card-body">
                                        <h5><i class="bi bi-list-check"></i> Features</h5>
                                        <ul class="list-unstyled text-start">
                                            <li>✅ IPO listings (Upcoming, Ongoing, Listed)</li>
                                            <li>✅ Search and filter functionality</li>
                                            <li>✅ Document upload (RHP/DRHP)</li>
                                            <li>✅ RESTful API</li>
                                            <li>✅ Responsive design</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="mt-4">
                            <a href="/api/" class="btn btn-outline-primary me-2">
                                <i class="bi bi-code"></i> API Overview
                            </a>
                            <a href="https://github.com/django/django" class="btn btn-outline-secondary" target="_blank">
                                <i class="bi bi-book"></i> Django Docs
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())
    
    def serve_api_overview(self):
        """Serve API overview."""
        api_data = {
            "message": "IPO Web App API",
            "version": "1.0.0",
            "endpoints": {
                "list_ipos": "/api/ipo/",
                "ipo_detail": "/api/ipo/<id>/",
                "admin_panel": "/admin/"
            },
            "features": [
                "Search and filter IPOs",
                "Get IPO details",
                "Upload documents",
                "Admin management"
            ],
            "status": "Development server - Install Django dependencies to run full application"
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(api_data, indent=2).encode())
    
    def serve_api_response(self):
        """Serve sample API response."""
        sample_data = {
            "count": 0,
            "results": [],
            "message": "No data available - Django server not running",
            "setup_required": True
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(sample_data, indent=2).encode())
    
    def serve_placeholder_page(self, path):
        """Serve placeholder page for undefined routes."""
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Page Not Found - IPO Web App</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
        </head>
        <body>
            <div class="container py-5 text-center">
                <h1 class="display-1"><i class="bi bi-exclamation-triangle text-warning"></i></h1>
                <h2>Page Not Found</h2>
                <p class="lead">The page <code>{path}</code> is not available in development mode.</p>
                <a href="/" class="btn btn-primary">
                    <i class="bi bi-house"></i> Go Home
                </a>
            </div>
        </body>
        </html>
        """
        
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())

def run_server(port=8000):
    """Run the development server."""
    with socketserver.TCPServer(("", port), IPOHandler) as httpd:
        print(f"🚀 IPO Development Server running at http://localhost:{port}")
        print("📁 Django project structure created successfully!")
        print("⚠️  Install Django dependencies to run the full application")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")

if __name__ == "__main__":
    run_server()
