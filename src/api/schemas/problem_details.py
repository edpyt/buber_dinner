from blacksheep import Content, Response
from pydantic import BaseModel, Field


class ProblemDetails(BaseModel):
    type_: str = Field(alias="type")
    title: str
    status: int


class ProblemDetailsResponse(BaseModel):
    problem_details: ProblemDetails

    @property
    def result(self) -> Response:
        return Response(
            self.problem_details.status,
            content=Content(
                b"application/problem+json",
                self.problem_details.model_dump_json().encode("utf8"),
            ),
        )
