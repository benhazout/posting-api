from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..services import statistics
from .. import schemas

router = APIRouter(
    prefix='/statistics',
    tags=['Statistics']
)


@router.get('/topcreators', response_model=schemas.ShowTopCreators)
def top_creators(db: Session = Depends(get_db)):
    return statistics.top_creators(db)
