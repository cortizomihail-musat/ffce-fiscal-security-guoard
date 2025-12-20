from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import time
from typing import Optional, Set

from app.integrity import verify_log
from app.state import SYSTEM_STATE, lock

class IntegrityGateMiddleware(BaseHTTPMiddleware):
    """
    Middleware antifraudă:
    - verifică periodic integritatea audit_log.jsonl
    - dacă este compromis → blochează aplicația
    """

    def __init__(
        self,
        app,
        check_ttl_seconds: int = 5,
        allow_paths: Optional[Set[str]] = None,
    ):
        super().__init__(app)
        self.check_ttl_seconds = check_ttl_seconds
        self.allow_paths = allow_paths or {"/health", "/audit/verify"}
        self._last_check = 0.0
        self._last_result = True

    async def dispatch(self, request: Request, call_next):
        # Permite explicit rutele critice
        if request.url.path in self.allow_paths:
            return await call_next(request)

        now = time.time()

        # Verificare periodică (cache TTL)
        if now - self._last_check > self.check_ttl_seconds:
            self._last_result = verify_log()
            self._last_check = now

        if not self._last_result:
            return JSONResponse(
                status_code=503,
                content={
                    "error": "SYSTEM_LOCKED",
                    "reason": "Audit log integrity violation",
                    "action": "Contact authority / administrator",
                },
            )

        return await call_next(request)
