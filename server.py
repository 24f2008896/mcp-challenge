
import hashlib

from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_request

mcp = FastMCP("IITM Live MCP Challenge")


@mcp.tool
def solve_challenge() -> str:
    """Solve the current exam challenge using its HTTP header."""
    request = get_http_request()
    challenge = request.headers.get("X-Exam-Challenge")

    if not challenge:
        raise ValueError("Missing X-Exam-Challenge header")

    email = "24f2008896@ds.study.iitm.ac.in".strip().lower()
    message = f"{challenge}:{email}"

    return hashlib.sha256(message.encode("utf-8")).hexdigest()[:16]


app = mcp.http_app(stateless_http=True)
