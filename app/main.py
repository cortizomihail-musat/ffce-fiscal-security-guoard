from fastapi import FastAPI
from app.integrity import verify_log
from app.middleware import IntegrityGateMiddleware

app = FastAPI(title="FFCE FiscalSecurityGuard (MVP)")
app.add_middleware(IntegrityGateMiddleware)

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/audit/verify")
def audit_verify():
    return {"integrity_ok": verify_log()}
