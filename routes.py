from fastapi import APIRouter
from controllers.Model_controller import router as ML_router

router = APIRouter()

router.include_router(ML_router)