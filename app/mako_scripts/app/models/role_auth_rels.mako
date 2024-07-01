"""
Time ${time}
Author ${author}
Email ${email}
"""

% for v in merged_import_pkg_list:
% if v["from"]:
from ${v["from"]} import ${v["import"]}
% else:
import ${v["import"]}
% endif
% endfor


class RoleAuthRels(Base):
    id = Column(String, primary_key=True, index=True)
    role_id = Column(String, index=True)
    auth_id = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    add_datetime = Column(DateTime, default=datetime.now)
    update_datetime = Column(DateTime, onupdate=datetime.now)

    __tablename__ = 'role_auth_rels'