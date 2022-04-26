from typing import Optional

from pydantic import BaseModel


class Achievements_List_Get(BaseModel):
    achv_name: str
    achv_req: int
    achv_is_limit: Optional[bool]
    achv_date_end_if_limit: Optional[str]


class Achievements_Limit_List_Get(BaseModel):
    achv_name: str
    achv_req: int
    achv_date_end_if_limit: str


class Complete_Achievements_List_Get(BaseModel):
    achv_name: str
    username: str
    receive_date: str


class Process_Achievements_List_Get(BaseModel):
    achv_name: str
    username: str
    achv_req: str
    achv_pass: str
    achv_is_limit: Optional[bool]
    achv_date_end_if_limit: Optional[str]