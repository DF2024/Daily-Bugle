from fastapi import Depends, HTTPException, status
from backend.auth.auth import get_current_user
from backend.models.user import User

def require_role(allowed_roles: list[str]):
    def role_checker(current_user: User = Depends(get_current_user)):
        role_name = current_user.token_role or (current_user.role_rel.name if current_user.role_rel else None)
        if role_name not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos para acceder a este recurso."
            )
        return current_user
    return role_checker