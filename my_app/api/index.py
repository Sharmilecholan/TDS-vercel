import json
from http.server import BaseHTTPRequestHandler

# Load the marks data from the JSON file
with open('api/marks_data.json', 'r') as file:
    marks_data = json.load(file)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS by adding the necessary headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
        self.end_headers()

        # Extract names from the query parameters
        query_params = self.path.split('?')[1].split('&')
        names = [param.split('=')[1] for param in query_params if param.startswith('name=')]

        # Collect the marks for the provided names
        marks_dict = {entry['name']: entry['marks'] for entry in marks_data}
        marks = [marks_dict.get(name, 0) for name in names]

        # Return the marks as a JSON response
        response = {
            "marks": marks
        }

        # Write the response
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
