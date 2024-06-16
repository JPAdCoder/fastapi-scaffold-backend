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


class CRUD${model_name}(${base_crud_class}[${model_name}, ${model_name}Create, ${model_name}Update, ${model_name}Page]):
    pass


${crud_obj} = CRUD${model_name}(${model_name}, ${model_name}Page)