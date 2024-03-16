from dataclasses import asdict, dataclass
from json import dumps

from blacksheep import Content, Response


@dataclass(frozen=True)
class ProblemDetails:
    type: str
    title: str
    status: int


@dataclass(frozen=True)
class ProblemDetailsResponse:
    problem_details: ProblemDetails

    @property
    def result(self) -> Response:
        return Response(
            self.problem_details.status,
            content=Content(
                b"application/problem+json",
                dumps(asdict(self.problem_details)).encode("utf8"),
            ),
        )
