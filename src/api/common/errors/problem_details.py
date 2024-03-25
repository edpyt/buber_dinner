from blacksheep import Content, Response
from pydantic import BaseModel


class ProblemDetails(BaseModel):
    message: str
    status: int


class ProblemResponse(Response):
    def __init__(self, problem_details: ProblemDetails) -> None:
        super().__init__(
            problem_details.status,
            content=Content(
                b"application/problem+json",
                problem_details.model_dump_json().encode("utf8"),
            ),
        )
