from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

# Mock Data Response (Replace with actual scraping logic using BeautifulSoup/Requests)
# Since I cannot scrape UAF from here, this simulates the responses your HTML expects.
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # 1. Parse URL parameters
        parsed_path = urlparse(self.path)
        params = parse_qs(parsed_path.query)
        
        action = params.get('action', [''])[0]
        reg_no = params.get('registrationNumber', [''])[0]

        # 2. Set CORS Headers (CRITICAL for frontend access)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*') # Allow all origins
        self.send_header('Access-Control-Allow-Methods', 'GET,OPTIONS')
        self.end_headers()

        # 3. Handle Actions
        response_data = {"success": False, "message": "Invalid Action"}

        if action == "server_status":
            # Check LMS/ATS connectivity here in real implementation
            response_data = {
                "success": True,
                "lms_status": "online",
                "attnd_status": "online"
            }

        elif action == "scrape_single":
            if not reg_no:
                response_data = {"success": False, "message": "Registration Number Required"}
            else:
                # --- REPLACE THIS BLOCK WITH ACTUAL SCRAPING LOGIC ---
                # Example structure required by your frontend:
                response_data = {
                    "success": True,
                    "resultData": [
                        {
                            "StudentName": "Real Student", 
                            "RegistrationNo": reg_no,
                            "Semester": "Winter 2023",
                            "CourseCode": "CS-301",
                            "CourseTitle": "Data Structures",
                            "CreditHours": "3",
                            "Total": "52",
                            "Grade": "A"
                        },
                        {
                            "StudentName": "Real Student", 
                            "RegistrationNo": reg_no,
                            "Semester": "Winter 2023",
                            "CourseCode": "CS-302",
                            "CourseTitle": "OOP",
                            "CreditHours": "4",
                            "Total": "65",
                            "Grade": "A"
                        }
                    ]
                }
                # ---------------------------------------------------

        elif action == "scrape_attendance":
            if not reg_no:
                response_data = {"success": False, "message": "Registration Number Required"}
            else:
                # --- REPLACE WITH ATTENDANCE SCRAPING LOGIC ---
                response_data = {
                    "success": True,
                    "resultData": [
                        {
                            "CourseCode": "CS-405",
                            "CourseName": "Web Engineering",
                            "Totalmark": "45",
                            "Grade": "B",
                            "Semester": "Spring 2024"
                        }
                    ]
                }
                # ----------------------------------------------

        # 4. Send JSON Response
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def do_OPTIONS(self):
        # Handle pre-flight CORS requests
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.end_headers()
