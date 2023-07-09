from sqlmodel import SQLModel, Field


class CertsBase(SQLModel):
    subject: str
    not_before: str
    not_after: str
    issuer: str
    extension_count: str
    subject_altName: str


class Certs(CertsBase, table=True):
    id: int = Field(default=None, primary_key=True)


class CertsCreate(CertsBase):
    pass
