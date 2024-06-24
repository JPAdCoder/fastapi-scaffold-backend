"""
Time ${time}
Author ${author}
Email ${email}
"""

% for v in schemas_param["init_file_param"]["merged_import_pkg_list"]:
% if v["from"] != "null":
from ${v["from"]} import ${v["import"]}
% else:
import ${v["import"]}
% endif
% endfor