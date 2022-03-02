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
    """Get complains 

    Get complaints for User. 
    - If user has role complainer, returns complaints created by this user.
    - If user has role aprover, returns complains in status pending

    The user have been authenticate!!!.

    Args:
        request (Request): Request with jwt token in headers

    Returns:
        array: Array list of complainst according to user role
    """

    user = request.state.user
    return await ComplaintManager.get_complaints(user)


@router.post(
    path="/complaints",
    dependencies=[Depends(oauth2_scheme), Depends(is_complainer)],
    response_model=ComplaintOut,
)
async def create_complaint(request: Request, complaint_data: ComplaintIn):

    """Create complaint

    Endpoint for create a complaint in the database. The user must have role complainter

    Returns:
        ComplaintOut: Return a ComplintOut schema
    """

    user = request.state.user
    return await ComplaintManager.create_complaint(complaint_data.dict(), user)


@router.delete(
    path="/complainst/{complaint_id}",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    status_code=204,
)
async def delete_complaint(complaint_id: int):
    """Delete complaints

    This endpoint delete a complaint. The user that require delete a complaint
    must have admin_role.

    Parameters:
    - complaint_id (int): Id of complaint that you want delete.
    """

    await ComplaintManager.delete_complaint(complaint_id)


@router.put(
    path="/complaints/{complaint_id}/approve",
    dependencies=[Depends(oauth2_scheme), Depends(is_approver)],
    status_code=204,
)
async def approve_complaint(complaint_id: int):
    """Approve complaint

    This endpoint make changes in a complaint register for change the status to approved

    User must have approver profile.

    Args:
        complaint_id (int): Id of complaint
    """

    await ComplaintManager.approve_complaint(complaint_id)


@router.put(
    path="/complaints/{complaint_id}/reject",
    dependencies=[Depends(oauth2_scheme), Depends(is_approver)],
    status_code=204,
)
async def approve_complaint(complaint_id: int):
    """Reject complaint

    This endpoint make changes in a complaint register for change the status to reject

    User must have approver profile.

    Args:
        complaint_id (int): Id of complaint
    """

    await ComplaintManager.reject_complaint(complaint_id)
