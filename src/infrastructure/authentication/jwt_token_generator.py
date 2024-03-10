from datetime import timedelta
from uuid import UUID

import jwt

from src.application.common.interfaces.authentication import (
    IJwtTokenGenerator,
)
from src.application.common.interfaces.services.dt_provider import (
    IDateTimeProvider,
)
from src.infrastructure.config.jwt import JWTConfig


class JwtTokenGenerator(IJwtTokenGenerator):
    _dt_provider: IDateTimeProvider
    _jwt_config: JWTConfig

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
                "exp": self._dt_provider.utc_now() +
                timedelta(minutes=self._jwt_config.expiry_minutes),
            },
            self._jwt_config.jwt_secret,
        )
        return encoded_jwt
