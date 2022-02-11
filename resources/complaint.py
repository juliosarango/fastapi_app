import stat
from typing import List
from fastapi import APIRouter, dependencies, Depends
from starlette.requests import Request

from managers.complaint import ComplaintManager
from managers.auth import is_admin, is_approver, oauth2_scheme, is_complainer

from schemas.request.complaint import ComplaintIn
from schemas.response.complaint import ComplaintOut


router = APIRouter(tags=["Complaints"])


@router.get(
    path="/complaints",
    dependencies=[Depends(oauth2_scheme)],
    response_model=List[ComplaintOut],
)
async def get_complaints(request: Request):
    user = request.state.user
    return await ComplaintManager.get_complaints(user)


@router.post(
    path="/complaints",
    dependencies=[Depends(oauth2_scheme), Depends(is_complainer)],
    response_model=ComplaintOut,
)
async def create_complaint(request: Request, complaint_data: ComplaintIn):
    user = request.state.user
    return await ComplaintManager.create_complaint(complaint_data.dict(), user)

@router.delete(
  path="/complainst/{complaint_id}",
  dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
  status_code=204
)
async def delete_complaint(complaint_id: int):
  await ComplaintManager.delete_complaint(complaint_id)

@router.put(
    path="/complaints/{complaint_id}/approve",
    dependencies=[Depends(oauth2_scheme), Depends(is_approver)],
    status_code=204
)
async def approve_complaint(complaint_id: int):
    await ComplaintManager.approve_complaint(complaint_id)


@router.put(
    path="/complaints/{complaint_id}/reject",
    dependencies=[Depends(oauth2_scheme), Depends(is_approver)],
    status_code=204
)
async def approve_complaint(complaint_id: int):
    await ComplaintManager.reject_complaint(complaint_id)    