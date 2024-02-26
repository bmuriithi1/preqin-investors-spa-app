from fastapi import APIRouter

router = APIRouter(prefix="/auth")


@router.post("/token")
def create_token():
    # TODO: Set up token-based authenticate
    return {"access_token": "abcd", "token_type": "bearer"}


@router.get("/verify")
def verify_token():
    # TODO: Set up token verification
    pass
