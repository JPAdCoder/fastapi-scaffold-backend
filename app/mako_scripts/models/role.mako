"""
Time ${time}
Author ${author}
Email ${email}
"""

% for v in models_param["role_file_param"]["merged_import_pkg_list"]:
% if v["from"] != "null":
from ${v["from"]} import ${v["import"]}
% else:
import ${v["import"]}
% endif
% endfor


class Role(Base):
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    add_datetime = Column(DateTime, default=datetime.now)
    update_datetime = Column(DateTime, onupdate=datetime.now)

    __tablename__ = 'role'