from datetime import timedelta

import jwt

from src.application.common.interfaces import DateTimeProvider, JwtTokenGenerator
from src.application.dto.user import UserDTO
from src.infrastructure.config.jwt import JWTConfig


class JwtTokenGeneratorImpl(JwtTokenGenerator):
    _dt_provider: DateTimeProvider
    _jwt_config: JWTConfig

    def generate_token(self, user: UserDTO) -> str:
        encoded_jwt: str = jwt.encode(
            {
                "sub": str(user.id),
                "given_name": user.first_name,
                "family_name": user.last_name,
                "exp": (
                    self._dt_provider.utc_now()
                    + timedelta(minutes=self._jwt_config.expiry_minutes)
                ).timestamp(),
            },
            self._jwt_config.jwt_secret,
        )
        return encoded_jwt
