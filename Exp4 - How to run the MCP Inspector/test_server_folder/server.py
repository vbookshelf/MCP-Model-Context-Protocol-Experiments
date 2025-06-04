import json
from typing import Dict
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("student_info")

# JSON data for student records
json_data = '''
{
  "students": [
    {
      "full_name": "John Smith",
      "student_id": "A123456",
      "date_of_birth": "1998-05-15"
    },
    {
      "full_name": "Emily Johnson",
      "student_id": "B789012",
      "date_of_birth": "2000-09-22"
    },
    {
      "full_name": "Michael Davis",
      "student_id": "C345678",
      "date_of_birth": "1999-03-08"
    },
    {
      "full_name": "Sophia Garcia",
      "student_id": "D901234",
      "date_of_birth": "2001-11-10"
    },
    {
      "full_name": "Ethan Wilson",
      "student_id": "E567890",
      "date_of_birth": "1997-07-04"
    }
  ]
}
'''

# Parse the JSON data
data = json.loads(json_data)

@mcp.tool()
def get_student_info(student_id: str) -> Dict[str, str]:
    """
    Retrieve student information by student ID.

    Args:
        student_id (str): The student ID to search for.

    Returns:
        Dict[str, str]: A dictionary containing the student's information
        if found, otherwise an empty dictionary.
    """
    for student in data["students"]:
        if student["student_id"] == student_id:
            return student
    return {}
	
	

if __name__ == "__main__":
    # Run the MCP server
    mcp.run(transport='stdio')
