from datetime import datetime, timedelta
from uuid import UUID

import jwt

from src.application.common.interfaces.authentication import (
    IJwtTokenGenerator,
)


class JwtTokenGenerator(IJwtTokenGenerator):
    def generate_token(
        self,
        user_id: UUID,
        first_name: str,
        last_name: str,
    ) -> str:
        encoded_jwt: str = jwt.encode(
            {
                "sub": str(user_id),
                "given_name": first_name,
                "family_name": last_name,
                "exp": datetime.now() + timedelta(days=1),  # noqa: DTZ005
            },
            "super-secret-key",
        )
        return encoded_jwt
