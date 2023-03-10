from typing import TYPE_CHECKING, List

from app import schemas, models, database

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def _add_tables():
    return database.Model.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def createCreation(creation: schemas.CreateCreation, db: "Session") -> schemas.Creation:
    creation = models.Creation(**creation.dict())
    db.add(creation)
    db.commit()
    db.refresh(creation)
    return schemas.Creation.from_orm(creation)

async def getCreations(db: "Session") -> List[schemas.Creation]:
    creations = db.query(models.Creation).all()
    return list(map(schemas.Creation.from_orm, creations))

async def getCreation(creation_id: int, db: "Session"):
    contact = db.query(models.Creation).filter(models.Creation.id == creation_id).first()
    return contact


async def deleteCreation(creation: models.Creation, db: "Session"):
    db.delete(creation)
    db.commit()


async def updateCreation(
    creation_data: schemas.CreateCreation, creation: models.Creation, db: "Session"
) -> schemas.Creation:
    creation.type = creation_data.type
    creation.description = creation_data.description
    creation.image = creation_data.image
    creation.link = creation_data.link

    db.commit()
    db.refresh(creation)

    return schemas.Creation.from_orm(creation)