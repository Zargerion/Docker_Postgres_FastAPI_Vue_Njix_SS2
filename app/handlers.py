from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

from app import schemas as _schemas, dependencies as _dependencies

from sqlalchemy.orm import Session


router = _fastapi.APIRouter()

@router.get('/')
def index():
    return {'status': 'OK'}

@router.post("/api/creations/", response_model=_schemas.Creation)
async def createCreation(creation: _schemas.CreateCreation, db: _orm.Session = _fastapi.Depends(_dependencies.get_db)):
    return await _dependencies.createCreation(creation=creation, db=db)

@router.get("/api/creations/", response_model=List[_schemas.Creation])
async def getCreations(db: "Session" = _fastapi.Depends(_dependencies.get_db)):
    return await _dependencies.getCreations(db=db)

@router.get("/api/creations/{creation_id}/", response_model=_schemas.Creation)
async def get_contact(
    creation_id: int, db: _orm.Session = _fastapi.Depends(_dependencies.get_db)
):
    creation = await _dependencies.getCreation(db=db, creation_id=creation_id)
    if creation is None:
        raise _fastapi.HTTPException(status_code=404, detail="Creation does not exist")

    return creation

@router.delete("/api/creations/{creation_id}/")
async def delete_contact(
    creation_id: int, db: _orm.Session = _fastapi.Depends(_dependencies.get_db)
):
    creation = await _dependencies.getCreation(db=db, creation_id=creation_id)
    if creation is None:
        raise _fastapi.HTTPException(status_code=404, detail="Contact does not exist")

    await _dependencies.deleteCreation(creation, db=db)

    return "Successfully deleted the creation."

@router.put("/api/creations/{creation_id}/", response_model=_schemas.Creation)
async def update_contact(
    creation_id: int,
    creation_data: _schemas.CreateCreation,
    db: _orm.Session = _fastapi.Depends(_dependencies.get_db),
):
    creation = await _dependencies.getCreation(db=db, creation_id=creation_id)
    if creation is None:
        raise _fastapi.HTTPException(status_code=404, detail="Contact does not exist")

    return await _dependencies.updateCreation(
        creation_data=creation_data, creation=creation, db=db
    )