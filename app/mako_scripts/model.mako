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


class ${model_name}(${base_model_name}):
    %for v in columns:
    ${v["column_name"]} = Column(${v["column_attr"]})
    %endfor

    __tablename__ = "${table_name}"
    __table_args__ = {"comment": "${table_comment}"}
