"""
Time ${time}
Author ${author}
Email ${email}
"""

% for v in api_param["api_v1_api_file_param"]["merged_import_pkg_list"]:
% if v["from"] != "null":
from ${v["from"]} import ${v["import"]}
% else:
import ${v["import"]}
% endif
% endfor

api_router = APIRouter()
api_router.include_router(login.router, tags=["login(登录相关)"])
api_router.include_router(users.router, tags=["user(用户相关)"])
api_router.include_router(role.router, tags=["role(角色相关)"])
api_router.include_router(auth.router, tags=["auth(权限相关)"])
api_router.include_router(crud.router, tags=["crud(生成crud相关)"])