import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Extract names from query parameters
        query_params = self.path.split('?')[1]
        names = query_params.split('&')
        requested_marks = []

        # Load marks data from the JSON file
        with open('api/marks_data.json') as f:
            data = json.load(f)

        # Extract marks for the requested names
        for name in names:
            name_value = name.split('=')[1]
            for entry in data:
                if entry['name'] == name_value:
                    requested_marks.append(entry['marks'])

        # Return the response in JSON format
        response = {"marks": requested_marks}
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
